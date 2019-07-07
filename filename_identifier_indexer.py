import json
import pprint

from filename_indexer import split_src_p, filter_nodes, RowIndexer, read_nodes, indexes

def read_strings():    
    return json.load(open('ID_TO_STR.idx.json'))

def read_rules():
    rules = { '_order' : ['_type','field.name'],
               '_type' : {} }
    
    node_types = json.load(open('NODE_TYPE_TO_TYPE_AND_FIELDNAME.idx.json'))
    for x in node_types:
        for y in node_types[x]:
            if y == 'identifier_node':
                for f in node_types[x][y]:
                    if f in ('_id') :
                        continue
                    if x not in rules['_type']:
                        rules['_type'][x]={'field.name' : { }}
                    if f not in rules['_type'][x]['field.name']:
                        rules['_type'][x]['field.name'][f] = { 'field.type' : y }
            
    return rules



def find_string(obj, rules, strings):
    #pprint.pprint(obj)
    #pprint.pprint(rules)
    if '_string' not in obj:
        obj['_string'] = "NOT FOUND" # default
        
    if obj['_type'] in rules['_type']:
        _type = obj['_type']
        for f in rules['_type'][_type]['field.name']:
            if f in obj:
                v = obj[f]
                if v in strings :
                    obj['_string'] = list(strings[v].keys())[0]
    pprint.pprint(obj)
    return obj
if __name__ == '__main__':
    strings = read_strings()
    rules = read_rules()
    nodes = [ find_string(split_src_p(obj), rules, strings) for obj in read_nodes() if filter_nodes(obj, 'srcp')]
    RowIndexer().build_indexes(
        index_defs={
            "FILENAME_LINE_NODE_TYPE_TO_STR": ['filename','line_number','_type', '_string','_id'],
        },
        data=nodes
    )
