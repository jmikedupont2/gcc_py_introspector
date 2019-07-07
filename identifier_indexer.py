import json
from filename_indexer import split_src_p, filter_nodes, RowIndexer, read_nodes, indexes

if __name__ == '__main__':
    # find identifiers for nodes
    nodes = [ obj for obj in read_nodes() if filter_nodes(obj, '_string') ]
    RowIndexer().build_indexes(
        index_defs={
            "ID_TO_STR": ['_id', '_string'],
        },
        data=nodes
    )
