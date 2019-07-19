from toolz.curried import *
from collections import Counter
import json
import click
import pprint
from itertools import starmap
import pdb

# from toolz import join, merge
from itertools import filterfalse


def keyjoin(leftkey, leftseq, rightkey, rightseq):
    return starmap(merge, join(leftkey, leftseq, rightkey, rightseq))


@curry
def _hasattr(atr, obj):
    return atr in obj


@curry
def pushdown(role, key, remove, obj):
    # pprint.pprint({
    #     'role': role,
    #     'key' : key,
    #     'remove' : remove,
    #     'obj' : obj})
    key_val = obj[key]
    data = {}
    for k in obj:
        if k in remove:
            continue
        if role:
            data[ role + "!" + k] = obj[k]  #
        else:
            data[k] = obj[k]  #
    return data

def keys(obj):
    return list(obj.keys())

@curry
def mdissoc(fields, obj):
    # pprint.pprint({'fields':fields,'obj':obj})
    rt = dissoc(obj, *fields)
    # pprint.pprint({'fields':fields,'obj':obj, 'rt' : rt})
    return rt

def join_field(role_from, role_to, field_name, nodes, exclude_left=(), exclude_right=()):
    from_field_name = field_name
    if role_from:
        from_field_name = role_from + "!" + field_name
    to_field_name = role_to + "!_id"
    
    results = keyjoin(
            from_field_name,
            filterfalse(
                get_in(field_name),
                map(
                    pushdown(role_from, field_name, exclude_left),
                    filter(_hasattr(field_name), nodes),
                ),
            ),
            to_field_name,
            map(pushdown(role_to, "_id", exclude_right), nodes),
        )
    
    results = map(mdissoc((to_field_name, from_field_name)),results)
        
    return list(results)


def join_field_extra(role_from, role_to, from_field_name, to_field_name, nodes_from, nodes_to,
                     debug=True,
                     exclude_left=(),
                     exclude_right=()):
    """The new from field name  is the field that is generated in the new obj
the new to field is also prefixed by the role
    """
    new_from_field_name = from_field_name
    if role_from:
        new_from_field_name = role_from + "!" + from_field_name
        
    new_to_field_name = role_to + "!" + to_field_name
 
    left = list(filterfalse(
                get_in(from_field_name),
                map(
                    pushdown(role_from, from_field_name, exclude_left),
                    filter(_hasattr(from_field_name), nodes_from),
                ),
            ))
    right = list(       
        map(pushdown(role_to, to_field_name, exclude_right),
            nodes_to))

    if debug:
        pprint.pprint({
            "left examples" :left[0],
            "new_left_key" : new_from_field_name,
            "left_key" : from_field_name,
            "right example" : right[0],
            "right_key" :to_field_name,
            "new_right_key" :new_to_field_name})
        
    results = keyjoin(
            new_from_field_name,
            left,
            new_to_field_name,
            right,
        )
    results = map(mdissoc((new_to_field_name, new_from_field_name)),results)
    results_list = list(results)

    if debug:
        pprint.pprint({
            'results-len': len(results_list),
            'results-example' : results_list[0]})
    
    return results_list


def expand_types(name):
    def _expand(x):
        type_name = x['_type']
        x['_type_' + type_name] = type_name
        return x
    return map(_expand, name)

@click.command()
@click.argument("input-file", type=click.File("r"))
def main(input_file):
    nodes = json.load(input_file)["nodes"]

    types_list = join_field("typed",
                        "typed!type",
                        'type',
                         nodes)
    
    named_types = join_field_extra(
        #"named_typed",
        None,
        "typed!name",
        'typed!name',
        '_id',
        types_list,
        nodes,
        debug=False,
        exclude_right=('_string_len','_type'))

    for field in ('size','min', 'max'):
        path = 'typed!type!' + field
        named_types = join_field_extra(
            None,
            path,
            path,        
            '_id',
            named_types,
            nodes,
            debug=True,
            exclude_right = (
                'type',
                '_type',
            )
        )
       
    results = named_types
    pprint.pprint(frequencies(list(concat(map(keys, results)))))


if __name__ == "__main__":
    main()
