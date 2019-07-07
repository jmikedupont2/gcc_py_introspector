import json
import pprint

from filename_indexer import split_src_p, filter_nodes, RowIndexer, read_nodes, indexes
from filename_identifier_indexer import read_rules, find_string
def read_strings():    
    return json.load(open('ID_TO_STRING2.idx.json'))

def find_any_string(obj, rules, strings):
    if '_string' not in obj:
        obj['_string'] = "NOT FOUND" # default        
    for f in obj:
        v = obj[f]
        if v in strings :
            obj['_string'] = list(strings[v].keys())[0]
    return obj
if __name__ == '__main__':
    strings = read_strings()
    rules = read_rules()
    pprint.pprint(rules)
    nodes = [ find_any_string(split_src_p(obj), rules, strings) for obj in read_nodes() if filter_nodes(obj, 'srcp')]
    #pprint.pprint(nodes)
    RowIndexer().build_indexes(
        index_defs={
            "FILENAME_LINE_NODE_TYPE_TO_STR2": ['filename','line_number','_type', '_string','_id'],
        },
        data=nodes
    )
