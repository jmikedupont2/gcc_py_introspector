import pprint
from splitter import RowIndexer, read_nodes, indexes

# show what nodes are on each line number for each file, create an annotated version of the file.
# read the source lines from the file and look for matching parts.
# try and determine the column numbers.
# extract field named srcp, split on :, first field is filename, second is line number
def split_src_p(obj):
    if 'srcp' in obj:
        val = obj['srcp']
        (filename, line_number) = val.split(':')
        obj['filename'] = filename
        obj['line_number'] = int(line_number)
    return obj
def filter_nodes(obj, field):
    if field in obj:
        return True
    else:
        return False

if __name__ == '__main__':
    nodes = read_nodes()
    #pprint.pprint(nodes)
    nodes = [ split_src_p(obj) for obj in nodes if filter_nodes(obj, 'srcp')]
    RowIndexer().build_indexes(
        index_defs={
            "FILENAME_LINE_NODE_TYPE_TO_ID": ['filename','line_number','_type', '_id'],
        },
        data=nodes
    )
