from toolz.curried import *
from collections import Counter
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

@curry
def attach_name(field_name, obj):
    target =  obj[field_name + '_obj']
    value =  obj['_id_obj']    
    target[field_name]= value
    return target

def keys(obj):
    return list(obj.keys())

def join_field(field_name, nodes):
    results = map(
        attach_name(field_name), 
        keyjoin(
        field_name,
        filterfalse(
            get_in(field_name),
            map(pushdown('_'+ field_name, field_name),
                filter(_hasattr(field_name),nodes)
            )
        ),
        '_id',
        map(pushdown('_node','_id'),
            nodes)
    ))
    return results

def explode(x):
    for y in x:
        yield y 
def foo(*args):
    res = Counter()
    for y in args:
        if not y:
            continue
        for x in y:
            v = res[x]
            
            #print(x, v)
            res[x] += v + 1
    return res
    
@click.command()
@click.argument('input-file', type=click.File('r'))
def main (input_file):
    data = json.load(input_file)
    nodes = data['nodes']

    #unql = join_field('unql',nodes)
    name = join_field('name',nodes)
    pprint.pprint(frequencies(list(concat(map(keys,name)))))

if __name__ == '__main__':
    main()
