# index/split up a json file
# jq -s "{nodes :.}" linux.json  > linux_jq.json
import json
import pprint
import sys
import re
import pdb
# defaultdict(default_factory[, ...]) --> dict with default factory
indexes = {}

ID_TO_NODE_TYPE = "ID_TO_NODE_TYPE"


def resolve_type(node_id):
    if isinstance(node_id, int):
        return "NATIVE_INTEGER"
    if isinstance(node_id, dict):
        if 'node' in node_id:
            return resolve_type(node_id['node'])
    if not isinstance(node_id, str):
        pprint.pprint({"debug_resolve": node_id})
        raise Exception(node_id)

    if node_id in indexes[ID_TO_NODE_TYPE]:
        return list(indexes[ID_TO_NODE_TYPE][node_id].keys())[0]
    else:
        return "ERROR {}".format(node_id)


def clean(obj):
    # pprint.pprint({"DEBUG START" : obj})
    names = ('_list', '_values')
    for n in names:
        if n in obj:
            l = obj[n]
            if n == '_values':
                l = l[0]  # some reason an array of arrays
            del obj[n]
            # pprint.pprint({"debug_l":l})
            if 'type_node' in l:
                # {'type_node': {'name': 'type', 'node': '11'}, 'value': '32'}
                obj['type'] = l['type_node']['node']
                obj['value'] = l['value']
            elif 'node' in l:
                # {'node': '151', 'name': 'type'}
                name = l['name']
                value = l['node']
                obj[name] = value
            else:
                for v in l:
                    if isinstance(v, str):
                        pprint.pprint({"debug_l": l})
                        raise Exception(l)
                    if 'node' in v:
                        # pprint.pprint({"DEBUG V": v})
                        name = v['name']
                        value = v['node']
                        obj[name] = value
                    else:
                        for name in v:
                            value = v[name]
                            obj[name] = value
    if obj is None:
        raise Exception()
    if '_string' in obj:
        v = obj['_string']
        m = re.match(r"(?P<value>.*)lngt: (?P<len>\d+)$", v)
        if m :
            v2 = m.group('value')
            ln = int(m.group('len'))
            obj['_string'] = v2[:ln]
            obj['_string_len'] = ln
    return obj


class Indexer:
    def create_index(self, data, schema):
        res = {}
        lenx = len(schema) - 1

        for obj in data:
            # pdb.set_trace()
            pos = 0
            cur = res
            for v in obj:
                if not isinstance(cur, dict):
                    pdb.set_trace()
                    pprint.pprint(cur)
                    raise Exception(cur)
                if not isinstance(v, str):
                    #v = v
                    pass
                if v in cur:
                    if pos == lenx:
                        # add
                        cur[v] = cur[v] + 1
                    else:
                        # recurse
                        cur = cur[v]
                else:
                    if pos == lenx:
                        cur[v] = 1
                    else:
                        cur[v] = {}
                    cur = cur[v]
                pos = pos + 1
        return res

    def build_index(self, index_name, field_list, data):
        print("Building" + index_name)
        results = []
        for obj in data:
            #obj = clean(obj)
            #pprint.pprint({"debug obj":obj})
            for res in self.index(obj, field_list):
                results.append(res)
                # now append the fields in order

            else:
                # in the case of the fields index we create an index entry(res)
                # for each node's field
                pass
            
        return results

    def build_indexes(self, index_defs, data):
        for idx in index_defs:
            idx_data = self.build_index(
                idx, index_defs[idx], data)
            print(pprint.pformat(idx_data)[0:200]) # just the first n chars for sample
            idx_idx = self.create_index(idx_data, index_defs[idx])
            print(pprint.pformat(idx_idx)[0:200]) # just the first n chars for sample
            indexes[idx] = idx_idx
            json.dump(idx_idx, open(idx + ".idx.json", 'w'),
                      indent=4, sort_keys=True)


class RowIndexer(Indexer):
    def index(self, obj, field_list):
        if obj is None:
            raise Exception("None object passed")
        res = []
        for f in field_list: # fields to index
            if f in obj:
                res.append(obj[f])
            else:
                pprint.pprint(obj)
                raise Exception(f)
        yield res


class FieldIndexer(Indexer):
    def index(self, obj, field_list):
        for fn in sorted(obj.keys()):
            res = []
            for f in field_list:  # fields to index
                if f in obj:
                    res.append(obj[f])
                elif f == 'field.name':
                    res.append(fn)
                elif f == 'field.type':
                    val = obj[fn]
                    val2 = resolve_type(val)
                    res.append(val2)
                elif f == 'field.id':
                    val = str(obj[fn])
                    res.append(val)

                else:
                    pprint.pprint(obj)
                    raise Exception(f)
            yield res

class CoOccurIndexer(Indexer):
    def index(self, obj, field_list):
        for fn in sorted(obj.keys()):
            for fn2 in sorted(obj.keys()):
                if fn == fn2:
                    continue
                res = []
                for f in field_list:  # fields to index
                    if f in obj:
                        res.append(obj[f])
                    elif f == 'field.name':
                        res.append(fn)
                    elif f == 'field.name2':
                        res.append(fn2)
                    elif f == 'field.type':
                        val = obj[fn]
                        val2 = resolve_type(val)
                        res.append(val2)
                    elif f == 'field.type2':
                        val = obj[fn2]
                        val2 = resolve_type(val)
                        res.append(val2)
                    elif f == 'field.id':
                        val = obj[fn]
                        res.append(val)
                    elif f == 'field.id2':
                        val = obj[fn2]
                        res.append(val)
                    else:
                        pprint.pprint(obj)
                        raise Exception(f)
                yield res


def read_nodes():
    return [ clean(obj) for obj in json.load(open(sys.argv[1]))['nodes']]

if __name__ == '__main__':
    nodes = read_nodes()
    if True:
        RowIndexer().build_indexes(
            index_defs={
                ID_TO_NODE_TYPE:  ['_id', '_type'],
                "NODE_TYPE_TO_ID": ['_type', '_id'],
            },
            data=nodes
        )

        # these indexs depend on the previous ones
        FieldIndexer().build_indexes(
            index_defs={
                "NODE_TYPE_LIST_OF_FIELDS":  ['_type', 'field.name'],
                # , 'field.id'
                "NODE_TYPE_TO_FIELD_NAME_AND_TYPE":  ['_type', 'field.name', 'field.type'],
                "NODE_TYPE_TO_TYPE_AND_FIELDNAME":  ['_type', 'field.type', 'field.name'],
                "NODE_TYPE_TO_TYPE_AND_FIELDNAME_AND_ID":  ['_type', 'field.type', 'field.name', '_id'],
            },
            data=nodes
        )


    # now we want the times each field occurs with another field, so all the pairs of fields
    CoOccurIndexer().build_indexes(
        index_defs={
            "NODE_TYPE_LIST_OF_FIELDS_CO":  ['_type', 'field.name', 'field.name2'],
        },
        data=nodes
    )

