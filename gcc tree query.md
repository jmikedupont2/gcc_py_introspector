

```python
from toolz_graph import *

```


```python
import sys
import json
import pprint
from toolz.curried import *
```

The introspect-data-linux contains data from a parsed .tu file and cleaned up with scripts to normalize it. Later we will emit that clean json directly but for now it is the interface used.


```python
input_file = open("introspector-data-linux/linux_clean.json")
nodes = json.load(input_file)['nodes']
```

An example node, the _id is the node id, _type is the type of the field.
The other attributes are either refrences to nodes or literals, there is no denotation of the type of the field here, but the fieldnames are clearly defined.  


```python
def field_report(data):
    """Helper function to print out the fields in order of usage"""
    field_names_data = dict(frequencies(list(concat(map(keys, data)))))
    items = field_names_data.items()
    sorted_fields = list(map(first, list(reversed(sorted(items, key=nth(1))))))
    return sorted_fields

```


```python
pprint.pprint(nodes[0])
```

    {'_id': '1', '_type': 'type_decl', 'chain': '4', 'name': '2', 'type': '3'}



```python
field_report(nodes)

```




    ['_type',
     '_id',
     'type',
     'name',
     'srcp',
     'scpe',
     'OP0 :',
     'chain',
     'algn',
     'size',
     '_string_len',
     '_string',
     'valu',
     'chan',
     'OP1',
     'body',
     'link',
     'bpos',
     'retn',
     'prms',
     'used',
     'E0',
     'purp',
     'cnst',
     'E1',
     'fn',
     'value',
     'ptd',
     'argt',
     'E2',
     'expr',
     'tag',
     'unql',
     'flds',
     'mngl',
     'prec',
     'sign',
     'min',
     'max',
     'args',
     'labl',
     'E3',
     'init',
     'val',
     'vars',
     'elts',
     'domn',
     'E4',
     'qual',
     'E5',
     'csts',
     'OP2',
     'E6',
     'E7',
     'E8',
     'E9',
     'E10',
     'low',
     'E11',
     'E12',
     'decl',
     'E13',
     'E14',
     'E15',
     'idx',
     'E16',
     'E17',
     'E18',
     'E19',
     'E20',
     'E21',
     'E22',
     'E23',
     'E25',
     'E24',
     'E26',
     'E27',
     'E28',
     'E29',
     'E31',
     'E30',
     'E35',
     'E34',
     'E33',
     'E32',
     'E39',
     'E38',
     'E37',
     'E36',
     'cond',
     'E43',
     'E42',
     'E41',
     'E40',
     'E47',
     'E46',
     'E45',
     'E44',
     'E54',
     'E53',
     'E52',
     'E51',
     'E50',
     'E49',
     'E48',
     'E62',
     'E61',
     'E60',
     'E59',
     'E58',
     'E57',
     'E56',
     'E55',
     'refd',
     'E97',
     'E96',
     'E95',
     'E94',
     'E93',
     'E92',
     'E91',
     'E90',
     'E89',
     'E88',
     'E87',
     'E86',
     'E85',
     'E84',
     'E83',
     'E82',
     'E81',
     'E80',
     'E79',
     'E78',
     'E77',
     'E76',
     'E75',
     'E74',
     'E73',
     'E72',
     'E71',
     'E70',
     'E69',
     'E68',
     'E67',
     'E66',
     'E65',
     'E64',
     'E63']




```python
def join_field(role_from, role_to, field_name, nodes, exclude_left=(), exclude_right=()):
    from_field_name = field_name
    if role_from:
        from_field_name = role_from + "_" + field_name
    to_field_name = role_to + "__id"
    
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
    # leave in all the ids
    # results = map(mdissoc((to_field_name, from_field_name)),results)
        
    return list(results)
```

Now we have a list of nodes we can join the nodes with themselves on the field named `type`. We name things on the left typed and things on the right the `typed_type` meaning is is the type behind the typed object. This will give us a nice table structure


```python
types_list = join_field("typed",
                        "typed_type",
                        'type',
                         nodes)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-a6e00da2845d> in <module>
          2                         "typed_type",
          3                         'type',
    ----> 4                          nodes)
    

    <ipython-input-7-a52b4d661943> in join_field(role_from, role_to, field_name, nodes, exclude_left, exclude_right)
         11                 map(
         12                     pushdown(role_from, field_name, exclude_left),
    ---> 13                     filter(_hasattr(field_name), nodes),
         14                 ),
         15             ),


    NameError: name '_hasattr' is not defined



```python
names = join_field("named",
                        "name",
                        'name',
                         nodes)
```


```python
field_report(names)
```


```python
string_names= [x for x in names if 'name__string' in x]
string_names
```

This next block joins the names of things where the name itself is not a string,
some names type decls and the name of them is the actual string .
The actual string is represented here in the field 'name_name__string'
 


```python

names2 = join_field_extra(
            role_from=None,
            role_to="name",
            from_field_name="name_name",        
            to_field_name='_id',
            nodes_from=names,
            nodes_to=nodes,
            debug=True,
            exclude_right = (
                'type',
                '_type',
            )
        )
```

Here is a unique list of the strings used in the names


```python
set(map(get('name__string'),names2))
```


```python
scpe_list = join_field("scoped",
                        "scope",
                        'scpe',
                         nodes)
field_report(scpe_list)
```

Now we can merge the simple and complex names together into one list for lookup


```python
all_names = string_names + names2
sorted(field_report(all_names))
```


```python

def filter_nodes(role, field_name, nodes, excludes) :
    return list(filterfalse(
                get_in(field_name),
                map(
                    pushdown(role, field_name, excludes),
                    filter(_hasattr(field_name), nodes),
                ),
            ))
    
def join_field_extra(
    role_from, from_field_name, nodes_from,
    role_to,  to_field_name, nodes_to,
                     debug=True,
                     exclude_left=(),
                     exclude_right=()):
    """The new from field name  is the field that is generated in the new obj
the new to field is also prefixed by the role
    """
    new_from_field_name = from_field_name
    if role_from:
        new_from_field_name = role_from + "_" + from_field_name
    new_to_field_name = to_field_name
    if role_to :
        new_to_field_name = role_to + "_" + to_field_name
 
    left = filter_nodes(role_from, from_field_name, nodes_from, exclude_left)
    right =filter_nodes(role_to, to_field_name, nodes_to, exclude_right) 

    if debug:
        if left:
            pprint.pprint({
                "left examples" :left[0:3],
                "new_left_key" : new_from_field_name,
                "left_key" : from_field_name,
            })
        if right:
            pprint.pprint({
                 "right example" : right[0:3],
                "right_key" :to_field_name,
                "new_right_key" :new_to_field_name})
    if not right :
        raise Exception()
    if not left:
        raise Exception()
    results = keyjoin(
            new_from_field_name,
            left,
            new_to_field_name,
            right,
        )
    # results = map(mdissoc((new_to_field_name, new_from_field_name)),results)
    results_list = list(results)

    if debug:
        pprint.pprint({
            'results-len': len(results_list),
         })
        if len(results_list):
          pprint.pprint({
            'results-example' : results_list[0:3]})
    
    return results_list

```


```python
field_report(all_names)
```


```python
#field_report(all_names)
scope_name = join_field_extra(
            nodes_from=scpe_list,
            role_from=None,
            from_field_name='scope_name',
            role_to='scope_name',
    nodes_to=all_names,        
    to_field_name='name__id',            
    debug=True)
field_report(scope_name)

```


```python
scoped_name = join_field_extra(
            nodes_from=scpe_list,
            role_from=None,
            from_field_name='scoped_name',
            role_to='scoped_name',
    nodes_to=all_names,        
    to_field_name='name__id',                
    debug=True)
field_report(scoped_name)
```

now we join the scoped with the scope names


```python
scoped_scope = join_field_extra(
            nodes_from=scoped_name,
            role_from='left',
            from_field_name='scope__id',
         
    
            role_to='right',
            nodes_to=all_names,        
            to_field_name='named__id',                
    debug=True)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-3e96cf54463e> in <module>
          1 scoped_scope = join_field_extra(
    ----> 2             nodes_from=scoped_name,
          3             role_from='left',
          4             from_field_name='scope__id',
          5 


    NameError: name 'scoped_name' is not defined


now show some names


```python
simple_report = list({ 
   obj['left_scoped_name_named__type'] : obj['left_scoped_name_name__string'],
    obj['right_named__type'] : obj['right_name__string'],
} for obj in list(scoped_scope))

field_report(simple_report)
```

This next report shows you the contained object and the container object by type, we see a good distribution of objects


```python
simple_report2 = groupby(
   [ 'left_scoped_name_named__type' , 
    'right_named__type'] , list(scoped_scope))
set(simple_report2)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-b45f9816be73> in <module>
          1 simple_report2 = groupby(
          2    [ 'left_scoped_name_named__type' , 
    ----> 3     'right_named__type'] , list(scoped_scope))
          4 set(simple_report2)


    NameError: name 'scoped_scope' is not defined



```python
fields
```


```python
from IPython.display import HTML, display
```


```python

# fields = field_report(scoped_scope)
fields = string_fields

header = '</th><th>'.join(fields)

display(HTML(
   '<table><tr><th>{}</th></tr><tr>{}</tr></table>'.format(
       header, 
       '</tr><tr>'.join(
        '<td>{}</td>'.format('</td><td>'.join(str(row.get(k,'null')) for k in fields)) for row in scoped_scope)
       )))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-d4235b5dcae3> in <module>
          1 # fields = field_report(scoped_scope)
    ----> 2 fields = string_fields
          3 
          4 header = '</th><th>'.join(fields)
          5 


    NameError: name 'string_fields' is not defined



```python
 [x for x in field_report(scoped_scope) if x.endswith('string') or '__type' in x]

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-4a3206a1c2d4> in <module>
    ----> 1 [x for x in field_report(scoped_scope) if x.endswith('string') or '__type' in x]
    

    NameError: name 'scoped_scope' is not defined



```python

```
