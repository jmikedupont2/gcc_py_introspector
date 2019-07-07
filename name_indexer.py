import json
import pprint
from filename_indexer import split_src_p, filter_nodes
from splitter import FieldIndexer, read_nodes, indexes
from filename_identifier_indexer import read_rules, find_string, read_strings

def read_name_rules():
    rules = { '_order' : ['_type','field.name'],
               '_type' : {} }    
    node_types = json.load(open('NODE_TYPE_TO_TYPE_AND_FIELDNAME.idx.json'))
    for x in node_types:
        for y in node_types[x]:
            for f in node_types[x][y]:
                if f not in ('name') :
                    continue
                if x not in rules['_type']:
                    rules['_type'][x]={'field.name' : { }}
                if f not in rules['_type'][x]['field.name']:
                    rules['_type'][x]['field.name'][f] = { 'field.type' : y }
    return rules

def find_name(obj, rules, strings):
    """use the newly created name index to resolve names"""
    if '_string' not in obj:
        obj['_string'] = "NOT FOUND" # default
        
    if obj['_type'] in rules['_type']:
        _type = obj['_type']
        for f in rules['_type'][_type]['field.name']:
            if f in obj:
                v = obj[f]
                if v in strings :
                    obj['_string'] = list(indexes["ID_TO_NAME"][v].keys())[0]
        
    return obj

if __name__ == '__main__':
    strings = read_strings()
    rules = read_rules()
    rules2 = read_name_rules()
    pprint.pprint(rules)
    pprint.pprint(rules2)
    nodes = [ obj for obj in read_nodes() if filter_nodes(obj, 'name') ]

    FieldIndexer().build_indexes(
        index_defs={
            "ID_TO_NAME": ['_id', 'name'], 
        },
        data=nodes
    )
    nodes = [ find_string(obj, rules2, strings) for obj in nodes ]
    nodes = [ find_string(find_string(obj, rules2, strings), rules, strings) for obj in nodes ]
    FieldIndexer().build_indexes(
        index_defs={
            "ID_TO_STRING2": ['_id', '_string'], 
        },
        data=nodes
    )
