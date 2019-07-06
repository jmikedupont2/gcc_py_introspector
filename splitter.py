# index/split up a json file
# jq -s "{nodes :.}" linux.json  > linux_jq.json
import json
import pdb
import pprint
import sys

#defaultdict(default_factory[, ...]) --> dict with default factory
indexes= {}

ID_TO_NODE_TYPE = "ID_TO_NODE_TYPE"
def resolve_type(node_id):
    if isinstance(node_id, int):
        return "NATIVE_INTEGER"
    if isinstance(node_id, dict):
        if 'node' in node_id :
            return resolve_type(node_id['node'])
    if not isinstance(node_id, str):
        pprint.pprint({"debug_resolve":node_id})
        raise Exception(v)

    if node_id in indexes[ID_TO_NODE_TYPE]:
        return list(indexes[ID_TO_NODE_TYPE][node_id].keys())[0]
    else:
        return "ERROR {}".format(node_id)

def create_index(data, schema):
    res = {}
    lenx = len(schema) -1

    for obj in data:
        #pdb.set_trace()
        pos = 0
        cur = res
        for v in obj:
            if not isinstance(v, str):
                v = str(v)
                #pprint.pprint({"debug_index":v})
                #raise Exception(v)

            if v in cur:
                if pos == lenx :
                    # add
                    cur[v] = cur[v] + 1
                else:
                    #recurse
                    cur = cur[v]
            else:
                if pos == lenx :
                    cur[v] = 1
                else:
                    cur[v] = {}
                cur = cur[v]
            pos = pos + 1
    return res

def clean(obj):
    # pprint.pprint({"DEBUG START" : obj})
    names = ('_list','_values')
    for n in names:
        if n in obj:
            l = obj[n]
            if n =='_values':
                l = l[0] # some reason an array of arrays
            del obj[n]
            # pprint.pprint({"debug_l":l})

            if 'type_node' in l:
                # {'type_node': {'name': 'type', 'node': '11'}, 'value': '32'}
                obj['type']=l['type_node']['node']
                obj['value']=l['value']
            elif 'node' in l:
                # {'node': '151', 'name': 'type'}
                name = l['name']
                value = l['node']
                obj[name]= value
            else:
                for v in l:
                    if isinstance(v, str):
                        pprint.pprint({"debug_l":l})
                        raise Exception(l)
                    if 'node' in v:
                        #pprint.pprint({"DEBUG V": v})
                        name = v['name']
                        value = v['node']
                        obj[name]= value
                    else:
                        for name in v:
                            value = v[name]
                            obj[name] = value
    return obj



def build_index(nodes, fields, index_name, field_list, data):
    print ("Building" +  index_name)
    results = []
    for obj in data:
        obj = clean(obj)
        # pprint.pprint({"debug obj":obj})

        if not fields : # just index the nodes
            res = []
            for f in field_list: # fields to index
                if f in obj:
                    res.append(obj[f])
                else:
                    pprint.pprint(obj)
                    raise Exception(f)
            results.append(res)
            # now append the fields in order

        else:
            # in the case of the fields index we create an index entry(res)
            # for each node's field

            for fn in sorted(obj.keys()):
                res = []
                for f in field_list: # fields to index
                    if f in obj:
                        res.append(obj[f])
                    elif f =='field.name':
                        res.append(fn)
                    elif f =='field.type':
                        val = obj[fn]
                        val2 = resolve_type(val)
                        res.append(val2)
                    elif f =='field.id':
                        val = obj[fn]
                        res.append(val)

                    else:
                        pprint.pprint(obj)
                        raise Exception(f)
                results.append(res)

    return results



def build_indexes( nodes, fields, index_defs, data):
    for idx in index_defs :
        idx_data = build_index(nodes, fields, idx, index_defs[idx], data)
        idx_idx = create_index(idx_data, index_defs[idx])
        #print(pprint.pformat(idx_idx)[0:200]) # just the first n chars for sample
        indexes[idx]= idx_idx
        json.dump(idx_idx, open(idx + ".idx.json",'w'), indent=4, sort_keys=True)

def read_nodes():
    return json.load(open(sys.argv[1]))['nodes']

nodes =     read_nodes()
build_indexes (
    nodes=True,
    fields=False,
    index_defs={
        ID_TO_NODE_TYPE :  ['_id' , '_type'],
        "NODE_TYPE_TO_ID" : ['_type' , '_id' ],
    },
    data=nodes
)

# these indexs depend on the previous ones
build_indexes (
    nodes=True,
    fields=True,
    index_defs={
        "NODE_TYPE_LIST_OF_FIELDS" :  ['_type' , 'field.name'  ],
        "NODE_TYPE_TO_FIELD_NAME_AND_TYPE" :  [ '_type', 'field.name', 'field.type' ], # , 'field.id'
    },
    data=nodes
)


# now we want the times each field occurs with another field, so all the pairs of fields
