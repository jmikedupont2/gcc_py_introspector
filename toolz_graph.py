from toolz.curried import *
import json
import click
import pprint
from itertools import starmap
#from toolz import join, merge
from itertools import filterfalse

def keyjoin(leftkey, leftseq, rightkey, rightseq):
    return starmap(merge, join(leftkey, leftseq, rightkey, rightseq))

@curry
def _hasattr(atr, obj):    
    return atr in obj

@curry
def pushdown(collection, key, obj):
    key_val =  obj[key]
    return {
        key : key_val,
        key + "_obj" : obj
    }

@click.command()
@click.argument('input-file', type=click.File('r'))
def main (input_file):
    data = json.load(input_file)
    nodes = data['nodes']
    #out_degrees = countby(apply(get_in(['_type'])),  nodes)

    unql = keyjoin('unql',
                   filterfalse(get_in('unql'),
                               map(pushdown('_unql', 'unql'),filter(_hasattr('unql'),nodes))),
                                      '_id',
                                      map(pushdown('_node','_id'),nodes))
    pprint.pprint(list(unql))
    
if __name__ == '__main__':
    main()
