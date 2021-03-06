# import pprint
import json
import types

import yaml
from SPARQLWrapper import (
    ASK,
    CONSTRUCT,
    DESCRIBE,
    GET,
    JSON,
    JSONLD,
    N3,
    POST,
    SELECT,
    XML,
    SPARQLWrapper,
)
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed
from SPARQLWrapper.Wrapper import (
    _RDF_JSONLD,
    _RDF_N3,
    _RDF_POSSIBLE,
    _RDF_XML,
    _SPARQL_DEFAULT,
    _SPARQL_JSON,
    _SPARQL_POSSIBLE,
    _SPARQL_XML,
)

import prefix
from graphviz import Digraph


def array_type(**kwargs):
    return "array"


def result_decl(**kwargs):
    return "return"


def var_decl(**kwargs):
    # pprint.pprint(kwargs)
    return kwargs["name"]


def identifier_node(**kwargs):
    return kwargs["string"]


######################


def call_expr(**kwargs):
    return {"call": kwargs}


def decl_expr(**kwargs):
    #    pprint.pprint({"decl_expr" : kwargs})
    # return {"decl_expr" : kwargs}
    return None


def expr(**kwargs):
    #    pprint.pprint({"expr" : kwargs})
    return {"expr": kwargs}


def cond_expr(**kwargs):
    #    pprint.pprint({"cond_expr" : kwargs})
    return {"cond_expr": kwargs}


def ne_expr(**kwargs):
    #    pprint.pprint({"ne_expr" : kwargs})
    return {"ne_expr": kwargs}


def addr_expr(**kwargs):
    # pprint.pprint({"addr_expr" : kwargs})
    if "type" in kwargs:
        return kwargs["type"]
    else:
        return {"addr_expr": kwargs}


def modify_expr(**kwargs):
    #    pprint.pprint({"Modify":kwargs})
    return [kwargs["OP0"], "=", kwargs["OP1"]]


def truth_andif_expr(**kwargs):
    #    pprint.pprint({"truth_andif_expr" : kwargs})
    return {"truth_andif_expr": kwargs}


def nop_expr(**kwargs):
    #    pprint.pprint({"nop_expr" : kwargs})
    # return {"nop" : kwargs}
    return kwargs["OP0"]


def bind_expr(**kwargs):
    #    pprint.pprint({"bind_expr" : kwargs})
    return {"bind": kwargs}


def return_expr(**kwargs):
    #    pprint.pprint({"return_expr" : kwargs})
    return {"ret": kwargs}


def eq_expr(**kwargs):
    #    pprint.pprint({"eq_expr" : kwargs})
    return [kwargs["OP0"], "==", kwargs["OP1"]]


def void_type(**kwargs):
    return "void"


def pointer_type(**kwargs):
    #    pprint.pprint({"pointer_type" : kwargs})
    return {"ptr": kwargs}


def component_ref(**kwargs):
    #    pprint.pprint({"component_ref" : kwargs})
    return {"comp_ref": kwargs}


def OP0(**kwargs):
    return kwargs


def OP1(**kwargs):
    return kwargs


def vars(**kwargs):
    # pprint.pprint({"vars" : kwargs})
    return {"vars": kwargs}


def _type(**kwargs):
    return {"type": kwargs}


def integer_type(**kwargs):
    return "int"


def integer_cst(**kwargs):
    return kwargs["low"]


def size(**kwargs):
    return kwargs


def note(**kwargs):
    return kwargs


def low(**kwargs):
    # pprint.pprint({"low" : kwargs})
    return {"low": kwargs}


def body(**kwargs):
    # pprint.pprint({"body" : kwargs})
    return {"body": kwargs}


def used(**kwargs):
    return kwargs


def string(**kwargs):
    # pprint.pprint({"string" : kwargs})
    return {"string": kwargs}


def string_cst(**kwargs):
    # pprint.pprint({"string_cst" : kwargs})
    return '"' + kwargs["string"] + '"'


def srcp(**kwargs):
    return kwargs


def link(**kwargs):
    return kwargs


def fn(**kwargs):
    # pprint.pprint({"fn" : kwargs})
    return {"fn": kwargs}


def name(**kwargs):
    # pprint.pprint({"name" : kwargs})
    return {"name": kwargs}


def bpos(**kwargs):
    return kwargs


def algn(**kwargs):
    return kwargs


def field_decl(**kwargs):
    # pprint.pprint({"field_decl" : kwargs})
    if "name" in kwargs:
        return "[" + str(kwargs["name"]) + "]"
    else:
        return {"field_decl": kwargs}


def statement_list(**kwargs):
    # pprint.pprint({"statement_list" : kwargs})
    r = []
    for x in sorted(kwargs.keys()):
        v = kwargs[x]
        if v:
            r.append(kwargs[x])
    # return {"stmts" : kwargs}
    return r


def E2(**kwargs):
    return kwargs


def E8(**kwargs):
    return kwargs


def E5(**kwargs):
    return kwargs


def E4(**kwargs):
    return kwargs


def E7(**kwargs):
    return kwargs


def E6(**kwargs):
    return kwargs


def E1(**kwargs):
    return kwargs


def E0(**kwargs):
    pprint.pprint(kwargs)
    return kwargs


def E3(**kwargs):
    return kwargs


def Unknown():
    return "Unknown"


def function_decl(**kwargs):
    if kwargs["body"] == "Unknown":
        pass
    else:
        # y=open('example.yaml','a')
        # j=open('example.json','a')
        # y.write(
        # print yaml.dump({"function": kwargs})
        # j.write(json.dumps({"function": kwargs},
        #                  sort_keys=True,
        #                  indent=4,
        #                  separators=(',', ': '))
        # )
        # y.close()
        # j.close()
        pprint.pprint({"function_decl": kwargs})
        return "Func(" + str(kwargs["name"]) + ")"


# special tree, name only
stree = {
    "exprs": {
        "node:addr_expr": {
            "fld:type": {
                "node:function_decl": "78"  # this could contain an entire function
            }
        }
    }
}

lookup = globals()


def decl_expr(**kwargs):
    pass


f = {}


def rec(x):
    t = "Unknown"

    if "rdf:type" in x:
        if x["rdf:type"]:
            t = x["rdf:type"]
            t = t.replace("node:", "")
        else:
            pass
        del x["rdf:type"]  # get rid of this
    args = {}

    for l in x:
        n = l.replace("fld:type", "ftype")
        n = n.replace("fld:", "")
        v = x[l]
        if type(v) is dict:
            # pass
            v2 = rec(v)
            args[n] = v2

        elif type(v) in str:
            if n in ("ntype", "type", "scpe", "chain"):
                pass
            elif v == "":
                pass
            else:
                if "link:" in v:
                    v = v.replace("link:", "")
                args[n] = v
        else:
            # print type(v)
            pass
    f = None
    if t in lookup:
        f = lookup[t]
    elif "_" + t in lookup:
        f = lookup["_" + t]

    return f(**args)


tree = {
    "exprs": {
        "node:addr_expr": {
            "fld:OP0": {"node:pointer_type": "90"},
            "fld:type": {
                # u'node:function_decl': u'78', this could contain an entire function
                "node:string_cst": "9",
                "node:var_decl": "3",
            },
        },
        "node:array_ref": {
            "fld:OP0": {"node:component_ref": "3"},
            "fld:OP1": {"node:var_decl": "3"},
        },
        "node:bind_expr": {
            "fld:body": {
                "node:return_expr": "30",
                "node:statement_list": "24",
            },
            "fld:vars": {"node:var_decl": "21"},
        },
        "node:bit_and_expr": {
            "fld:OP0": {
                "node:array_ref": "1",
                "node:component_ref": "2",
                "node:convert_expr": "4",
                "node:nop_expr": "3",
                "node:parm_decl": "2",
                "node:plus_expr": "3",
            },
            "fld:OP1": {
                "node:bit_not_expr": "1",
                "node:integer_cst": "13",
                "node:var_decl": "1",
            },
        },
        "node:bit_ior_expr": {
            "fld:OP0": {
                "node:array_ref": "1",
                "node:bit_and_expr": "3",
                "node:bit_ior_expr": "1",
                "node:nop_expr": "1",
            },
            "fld:OP1": {
                "node:bit_and_expr": "2",
                "node:lshift_expr": "3",
                "node:var_decl": "1",
            },
        },
        "node:bit_not_expr": {"fld:OP0": {"node:var_decl": "1"}},
        "node:call_expr": {
            "fld:E0": {
                "node:ge_expr": "6",
                "node:integer_cst": "10",
                "node:nop_expr": "23",
                "node:parm_decl": "18",
                "node:var_decl": "7",
            },
            "fld:E1": {
                "node:integer_cst": "12",
                "node:nop_expr": "13",
                "node:parm_decl": "8",
                "node:var_decl": "2",
            },
            "fld:E2": {
                "node:integer_cst": "8",
                "node:parm_decl": "6",
                "node:var_decl": "2",
            },
            "fld:E3": {"node:integer_cst": "5", "node:parm_decl": "2"},
            "fld:fn": {"node:addr_expr": "76", "node:parm_decl": "1"},
        },
        "node:case_label_expr": {
            "fld:low": {"node:integer_cst": "4"},
            "fld:name": {"node:label_decl": "5"},
        },
        "node:component_ref": {
            "fld:OP0": {"node:indirect_ref": "25", "node:var_decl": "1"},
            "fld:OP1": {"node:field_decl": "26"},
        },
        "node:compound_expr": {
            "fld:OP0": {"node:modify_expr": "2"},
            "fld:OP1": {"node:integer_cst": "2"},
        },
        "node:cond_expr": {
            "fld:OP0": {
                "node:eq_expr": "12",
                "node:gt_expr": "2",
                "node:le_expr": "2",
                "node:lt_expr": "2",
                "node:ne_expr": "28",
                "node:truth_andif_expr": "14",
                "node:truth_orif_expr": "4",
            },
            "fld:OP1": {
                "node:bind_expr": "2",
                "node:call_expr": "16",
                "node:cond_expr": "1",
                "node:convert_expr": "2",
                "node:goto_expr": "12",
                "node:modify_expr": "9",
                "node:nop_expr": "5",
                "node:statement_list": "17",
            },
            "fld:OP2": {
                "node:call_expr": "4",
                "node:cond_expr": "3",
                "node:goto_expr": "12",
                "node:integer_cst": "2",
                "node:nop_expr": "6",
                "node:parm_decl": "2",
                "node:return_expr": "1",
            },
        },
        "node:const_decl": {  # u'fld:chain': {u'node:const_decl': u'462',
            #               u'node:type_decl': u'26'},
            "fld:cnst": {"node:integer_cst": "488"},
            "fld:name": {"node:identifier_node": "488"},
            # u'fld:scpe': {u'node:translation_unit_decl': u'488'}
        },
        "node:convert_expr": {
            "fld:OP0": {
                "node:addr_expr": "1",
                "node:call_expr": "1",
                "node:parm_decl": "9",
                "node:rshift_expr": "3",
            }
        },
        "node:eq_expr": {
            "fld:OP0": {
                "node:call_expr": "2",
                "node:nop_expr": "16",
                "node:parm_decl": "1",
                "node:var_decl": "6",
            },
            "fld:OP1": {
                "node:integer_cst": "12",
                "node:nop_expr": "7",
                "node:parm_decl": "6",
            },
        },
        "node:field_decl": {
            # u'fld:bpos': {u'node:integer_cst': u'562'},
            # u'fld:chain': {u'node:field_decl': u'427'},
            "fld:name": {"node:identifier_node": "545"},
            "fld:orig": {"node:field_decl": "2"},
            # u'fld:size': {u'node:integer_cst': u'562'}
        },
        "node:function_decl": {
            "fld:args": {"node:parm_decl": "45"},
            "fld:body": {"node:bind_expr": "51"},
            # u'fld:chain': {u'node:function_decl': u'3059',
            #               u'node:type_decl': u'3',
            #               u'node:var_decl': u'19'},
            "fld:mngl": {"node:identifier_node": "528"},
            "fld:name": {"node:identifier_node": "3082"},
            # u'fld:scpe': {u'node:translation_unit_decl': u'2767'}
        },
        "node:ge_expr": {
            "fld:OP0": {"node:component_ref": "6"},
            "fld:OP1": {"node:component_ref": "6"},
        },
        "node:goto_expr": {"fld:labl": {"node:label_decl": "46"}},
        "node:gt_expr": {
            "fld:OP0": {"node:var_decl": "2"},
            "fld:OP1": {"node:integer_cst": "2"},
        },
        "node:indirect_ref": {
            "fld:OP0": {
                "node:call_expr": "2",
                "node:nop_expr": "3",
                "node:parm_decl": "38",
                "node:pointer_plus_expr": "18",
                "node:postincrement_expr": "7",
                "node:var_decl": "15",
            }
        },
        "node:label_decl": {
            "fld:name": {"node:identifier_node": "1"},
            # u'fld:scpe': {u'node:function_decl': u'47'}
        },
        "node:label_expr": {"fld:name": {"node:label_decl": "42"}},
        "node:le_expr": {
            "fld:OP0": {
                "node:nop_expr": "1",
                "node:parm_decl": "1",
                "node:plus_expr": "2",
            },
            "fld:OP1": {"node:integer_cst": "4"},
        },
        "node:lshift_expr": {
            "fld:OP0": {"node:bit_and_expr": "3", "node:integer_cst": "3"},
            "fld:OP1": {"node:bit_and_expr": "3", "node:integer_cst": "3"},
        },
        "node:lt_expr": {
            "fld:OP0": {"node:var_decl": "2"},
            "fld:OP1": {"node:integer_cst": "1", "node:var_decl": "1"},
        },
        "node:modify_expr": {
            "fld:OP0": {
                "node:array_ref": "2",
                "node:indirect_ref": "11",
                "node:parm_decl": "1",
                "node:result_decl": "50",
                "node:var_decl": "49",
            },
            "fld:OP1": {
                "node:bit_and_expr": "1",
                "node:bit_ior_expr": "4",
                "node:call_expr": "18",
                "node:compound_expr": "2",
                "node:cond_expr": "14",
                "node:convert_expr": "4",
                "node:indirect_ref": "1",
                "node:integer_cst": "34",
                "node:modify_expr": "1",
                "node:ne_expr": "3",
                "node:nop_expr": "6",
                "node:parm_decl": "2",
                "node:plus_expr": "1",
                "node:pointer_plus_expr": "1",
                "node:postincrement_expr": "1",
                "node:preincrement_expr": "1",
                "node:trunc_div_expr": "1",
                "node:var_decl": "18",
            },
        },
        "node:mult_expr": {
            "fld:OP0": {"node:nop_expr": "2", "node:var_decl": "1"},
            "fld:OP1": {"node:integer_cst": "2", "node:parm_decl": "1"},
        },
        "node:ne_expr": {
            "fld:OP0": {
                "node:bit_and_expr": "3",
                "node:call_expr": "9",
                "node:component_ref": "1",
                "node:modify_expr": "2",
                "node:nop_expr": "25",
                "node:parm_decl": "1",
                "node:var_decl": "18",
            },
            "fld:OP1": {"node:integer_cst": "48", "node:parm_decl": "11"},
        },
        "node:nop_expr": {
            "fld:OP0": {
                "node:addr_expr": "13",
                "node:array_ref": "1",
                "node:bit_ior_expr": "1",
                "node:call_expr": "7",
                "node:component_ref": "2",
                "node:convert_expr": "3",
                "node:indirect_ref": "40",
                "node:modify_expr": "3",
                "node:mult_expr": "3",
                "node:nop_expr": "3",
                "node:parm_decl": "24",
                "node:plus_expr": "3",
                "node:postincrement_expr": "3",
                "node:var_decl": "31",
            }
        },
        "node:parm_decl": {
            "fld:chain": {"node:parm_decl": "48"},
            "fld:name": {"node:identifier_node": "93"},
            # u'fld:scpe': {u'node:function_decl': u'93'},
            # u'fld:size': {u'node:integer_cst': u'93'}
        },
        "node:plus_expr": {
            "fld:OP0": {
                "node:nop_expr": "2",
                "node:parm_decl": "6",
                "node:var_decl": "2",
            },
            "fld:OP1": {"node:integer_cst": "9", "node:var_decl": "1"},
        },
        "node:pointer_plus_expr": {
            "fld:OP0": {"node:indirect_ref": "2", "node:parm_decl": "17"},
            "fld:OP1": {"node:integer_cst": "1", "node:nop_expr": "18"},
        },
        "node:postdecrement_expr": {
            "fld:OP0": {"node:var_decl": "1"},
            "fld:OP1": {"node:integer_cst": "1"},
        },
        "node:postincrement_expr": {
            "fld:OP0": {
                "node:component_ref": "6",
                "node:indirect_ref": "1",
                "node:parm_decl": "2",
                "node:var_decl": "3",
            },
            "fld:OP1": {"node:integer_cst": "12"},
        },
        "node:preincrement_expr": {
            "fld:OP0": {"node:parm_decl": "3", "node:var_decl": "9"},
            "fld:OP1": {"node:integer_cst": "12"},
        },
        "node:result_decl": {
            # u'fld:scpe': {u'node:function_decl': u'49'},
            #                  u'fld:size': {u'node:integer_cst': u'49'}
        },
        "node:return_expr": {"fld:expr": {"node:modify_expr": "50"}},
        "node:rshift_expr": {
            "fld:OP0": {"node:parm_decl": "3"},
            "fld:OP1": {"node:integer_cst": "3"},
        },
        "node:statement_list": {
            "fld:E0": {
                "node:call_expr": "4",
                "node:case_label_expr": "1",
                "node:decl_expr": "21",
                "node:goto_expr": "2",
                "node:modify_expr": "14",
            },
            "fld:E1": {
                "node:call_expr": "4",
                "node:case_label_expr": "1",
                "node:cond_expr": "7",
                "node:decl_expr": "8",
                "node:goto_expr": "12",
                "node:label_expr": "4",
                "node:modify_expr": "4",
                "node:postincrement_expr": "1",
                "node:switch_expr": "1",
            },
            "fld:E10": {
                "node:cond_expr": "2",
                "node:label_expr": "1",
                "node:modify_expr": "2",
            },
            "fld:E11": {
                "node:call_expr": "1",
                "node:cond_expr": "1",
                "node:modify_expr": "1",
                "node:postdecrement_expr": "1",
                "node:return_expr": "1",
            },
            "fld:E12": {
                "node:cond_expr": "1",
                "node:goto_expr": "1",
                "node:modify_expr": "1",
                "node:return_expr": "1",
            },
            "fld:E13": {
                "node:case_label_expr": "1",
                "node:label_expr": "1",
                "node:modify_expr": "1",
            },
            "fld:E14": {"node:call_expr": "1", "node:cond_expr": "2"},
            "fld:E15": {"node:label_expr": "1", "node:return_expr": "1"},
            "fld:E16": {"node:return_expr": "1"},
            "fld:E2": {
                "node:call_expr": "2",
                "node:case_label_expr": "1",
                "node:cond_expr": "3",
                "node:convert_expr": "1",
                "node:decl_expr": "2",
                "node:goto_expr": "2",
                "node:label_expr": "8",
                "node:modify_expr": "4",
                "node:preincrement_expr": "2",
                "node:return_expr": "6",
            },
            "fld:E3": {
                "node:call_expr": "2",
                "node:cond_expr": "4",
                "node:decl_expr": "2",
                "node:label_expr": "3",
                "node:modify_expr": "4",
                "node:preincrement_expr": "6",
            },
            "fld:E4": {
                "node:call_expr": "2",
                "node:cond_expr": "6",
                "node:decl_expr": "1",
                "node:label_expr": "7",
                "node:modify_expr": "1",
                "node:preincrement_expr": "3",
                "node:return_expr": "1",
            },
            "fld:E5": {
                "node:call_expr": "1",
                "node:cond_expr": "7",
                "node:goto_expr": "3",
                "node:label_expr": "4",
                "node:modify_expr": "5",
            },
            "fld:E6": {
                "node:call_expr": "1",
                "node:cond_expr": "3",
                "node:goto_expr": "1",
                "node:label_expr": "10",
                "node:modify_expr": "3",
                "node:return_expr": "2",
            },
            "fld:E7": {
                "node:bind_expr": "1",
                "node:case_label_expr": "1",
                "node:cond_expr": "3",
                "node:goto_expr": "1",
                "node:label_expr": "1",
                "node:modify_expr": "3",
                "node:return_expr": "6",
            },
            "fld:E8": {
                "node:cond_expr": "3",
                "node:label_expr": "2",
                "node:modify_expr": "2",
                "node:return_expr": "1",
            },
            "fld:E9": {"node:cond_expr": "4", "node:modify_expr": "1"},
        },
        "node:switch_expr": {
            "fld:body": {"node:statement_list": "1"},
            "fld:cond": {"node:var_decl": "1"},
        },
        "node:tree_list": {
            "fld:chan": {"node:tree_list": "2714"},
            "fld:purp": {"node:identifier_node": "488"},
            "fld:valu": {"node:integer_cst": "488"},
        },
        "node:trunc_div_expr": {
            "fld:OP0": {"node:nop_expr": "3", "node:plus_expr": "1"},
            "fld:OP1": {"node:integer_cst": "4"},
        },
        "node:truth_andif_expr": {
            "fld:OP0": {
                "node:eq_expr": "1",
                "node:ne_expr": "13",
                "node:truth_andif_expr": "6",
            },
            "fld:OP1": {
                "node:eq_expr": "2",
                "node:le_expr": "2",
                "node:ne_expr": "15",
                "node:truth_and_expr": "1",
            },
        },
        "node:truth_orif_expr": {
            "fld:OP0": {"node:eq_expr": "4", "node:truth_orif_expr": "2"},
            "fld:OP1": {"node:eq_expr": "6"},
        },
        "node:type_decl": {  # u'fld:chain': {u'node:const_decl': u'26',
            #               u'node:function_decl': u'5',
            #               u'node:type_decl': u'460'},
            "fld:name": {"node:identifier_node": "318"},
            # u'fld:scpe': {u'node:translation_unit_decl': u'449'}
        },
        "node:var_decl": {  # u'fld:chain': {u'node:function_decl': u'18',
            #               u'node:label_decl': u'1',
            #               u'node:var_decl': u'106'},
            "fld:init": {
                "node:indirect_ref": "3",
                "node:integer_cst": "6",
                "node:lshift_expr": "3",
                "node:trunc_div_expr": "3",
                "node:var_decl": "2",
            },
            "fld:name": {"node:identifier_node": "146"},
            # u'fld:scpe': {u'node:function_decl': u'34',
            #              u'node:translation_unit_decl': u'112'},
            # u'fld:size': {u'node:integer_cst': u'134'}
        },
        "node:enumeral_type": {
            # {u'fld:csts': {u'node:tree_list': u'31'},
            "fld:max": {"node:integer_cst": "31"},
            "fld:min": {"node:integer_cst": "31"},
            "fld:name": {"node:identifier_node": "9", "node:type_decl": "5"},
            "fld:size": {"node:integer_cst": "31"},
            # u'fld:unql': {u'node:enumeral_type': u'5'}
        },
        "node:integer_type": {
            "fld:max": {"node:integer_cst": "188"},
            "fld:min": {"node:integer_cst": "188"},
            "fld:name": {
                "node:identifier_node": "2",
                "node:type_decl": "157",
            },
            "fld:size": {"node:integer_cst": "188"},
            # u'fld:unql': {u'node:integer_type': u'144'}
        },
    },
    "types": {
        "node:array_ref": {"fld:type": {"node:integer_type": "3"}},
        "node:array_type": {
            "fld:domn": {"node:integer_type": "49"},
            "fld:elts": {
                "node:integer_type": "36",
                "node:pointer_type": "7",
                "node:record_type": "14",
            },
            "fld:name": {"node:type_decl": "8"},
            # u'fld:size': {u'node:integer_cst': u'49'},
            "fld:unql": {"node:array_type": "12"},
        },
        "node:bind_expr": {"fld:type": {"node:void_type": "54"}},
        "node:bit_and_expr": {"fld:type": {"node:integer_type": "15"}},
        "node:bit_ior_expr": {"fld:type": {"node:integer_type": "6"}},
        "node:bit_not_expr": {"fld:type": {"node:integer_type": "1"}},
        "node:boolean_type": {
            "fld:name": {"node:type_decl": "1"},
            "fld:size": {"node:integer_cst": "1"},
        },
        "node:call_expr": {
            "fld:type": {
                "node:integer_type": "46",
                "node:pointer_type": "12",
                "node:real_type": "1",
                "node:void_type": "18",
            }
        },
        "node:case_label_expr": {"fld:type": {"node:void_type": "5"}},
        "node:complex_type": {
            "fld:name": {"node:type_decl": "4"},
            "fld:size": {"node:integer_cst": "5"},
        },
        "node:component_ref": {
            "fld:type": {
                "node:array_type": "3",
                "node:enumeral_type": "1",
                "node:integer_type": "2",
                "node:pointer_type": "20",
            }
        },
        "node:compound_expr": {"fld:type": {"node:integer_type": "2"}},
        "node:cond_expr": {
            "fld:type": {
                "node:integer_type": "11",
                "node:pointer_type": "3",
                "node:void_type": "50",
            }
        },
        "node:const_decl": {"fld:type": {"node:enumeral_type": "488"}},
        "node:convert_expr": {
            "fld:type": {
                "node:integer_type": "11",
                "node:pointer_type": "2",
                "node:void_type": "1",
            }
        },
        "node:decl_expr": {"fld:type": {"node:void_type": "34"}},
        "node:enumeral_type": {
            "fld:csts": {"node:tree_list": "31"},
            # u'fld:max': {u'node:integer_cst': u'31'},
            # u'fld:min': {u'node:integer_cst': u'31'},
            # u'fld:name': {u'node:identifier_node': u'9',
            #              u'node:type_decl': u'5'},
            # u'fld:size': {u'node:integer_cst': u'31'},
            "fld:unql": {"node:enumeral_type": "5"},
        },
        "node:eq_expr": {"fld:type": {"node:integer_type": "25"}},
        "node:field_decl": {
            # u'fld:scpe': {u'node:record_type': u'459',
            #                               u'node:union_type': u'103'},
            "fld:type": {
                "node:array_type": "42",
                "node:enumeral_type": "4",
                "node:integer_type": "290",
                "node:pointer_type": "169",
                "node:real_type": "2",
                "node:record_type": "29",
                "node:union_type": "26",
            }
        },
        "node:function_decl": {"fld:type": {"node:function_type": "3082"}},
        "node:function_type": {
            "fld:name": {"node:type_decl": "45"},
            "fld:prms": {"node:tree_list": "1102"},
            "fld:retn": {
                "node:boolean_type": "22",
                "node:complex_type": "13",
                "node:integer_type": "487",
                "node:pointer_type": "310",
                "node:real_type": "66",
                "node:record_type": "4",
                "node:vector_type": "58",
                "node:void_type": "154",
            },
            "fld:size": {"node:integer_cst": "1114"},
            "fld:unql": {"node:function_type": "51"},
        },
        "node:ge_expr": {"fld:type": {"node:integer_type": "6"}},
        "node:goto_expr": {"fld:type": {"node:void_type": "46"}},
        "node:gt_expr": {"fld:type": {"node:integer_type": "2"}},
        "node:indirect_ref": {
            "fld:type": {
                "node:integer_type": "47",
                "node:pointer_type": "11",
                "node:record_type": "25",
            }
        },
        "node:integer_cst": {
            "fld:type": {
                "node:integer_type": "455",
                "node:pointer_type": "12",
            }
        },
        "node:integer_type": {
            "fld:max": {"node:integer_cst": "188"},
            "fld:min": {"node:integer_cst": "188"},
            "fld:name": {
                "node:identifier_node": "2",
                "node:type_decl": "157",
            },
            "fld:size": {"node:integer_cst": "188"},
            "fld:unql": {"node:integer_type": "144"},
        },
        "node:label_decl": {"fld:type": {"node:void_type": "47"}},
        "node:label_expr": {"fld:type": {"node:void_type": "42"}},
        "node:le_expr": {"fld:type": {"node:integer_type": "4"}},
        "node:lshift_expr": {"fld:type": {"node:integer_type": "6"}},
        "node:lt_expr": {"fld:type": {"node:integer_type": "2"}},
        "node:modify_expr": {
            "fld:type": {
                "node:integer_type": "76",
                "node:pointer_type": "36",
                "node:real_type": "1",
            }
        },
        "node:mult_expr": {"fld:type": {"node:integer_type": "3"}},
        "node:ne_expr": {"fld:type": {"node:integer_type": "59"}},
        "node:nop_expr": {
            "fld:type": {
                "node:integer_type": "103",
                "node:pointer_type": "34",
            }
        },
        "node:parm_decl": {
            "fld:argt": {
                "node:integer_type": "49",
                "node:pointer_type": "44",
            },
            "fld:type": {
                "node:integer_type": "49",
                "node:pointer_type": "44",
            },
        },
        "node:plus_expr": {"fld:type": {"node:integer_type": "10"}},
        "node:pointer_plus_expr": {"fld:type": {"node:pointer_type": "19"}},
        "node:pointer_type": {
            "fld:name": {"node:type_decl": "17"},
            "fld:ptd": {
                "node:array_type": "7",
                "node:function_type": "77",
                "node:integer_type": "40",
                "node:pointer_type": "18",
                "node:real_type": "6",
                "node:record_type": "129",
                "node:union_type": "2",
                "node:vector_type": "3",
                "node:void_type": "9",
            },
            "fld:size": {"node:integer_cst": "291"},
            "fld:unql": {"node:pointer_type": "62"},
        },
        "node:postdecrement_expr": {"fld:type": {"node:integer_type": "1"}},
        "node:postincrement_expr": {
            "fld:type": {"node:integer_type": "1", "node:pointer_type": "11"}
        },
        "node:preincrement_expr": {
            "fld:type": {"node:integer_type": "7", "node:pointer_type": "5"}
        },
        "node:real_type": {
            "fld:name": {"node:type_decl": "9"},
            "fld:size": {"node:integer_cst": "9"},
            "fld:unql": {"node:real_type": "2"},
        },
        "node:record_type": {
            "fld:flds": {"node:field_decl": "177"},
            "fld:name": {
                "node:identifier_node": "89",
                "node:type_decl": "69",
            },
            "fld:size": {"node:integer_cst": "177"},
            "fld:unql": {"node:record_type": "79"},
        },
        "node:reference_type": {
            "fld:refd": {"node:pointer_type": "1"},
            "fld:size": {"node:integer_cst": "1"},
        },
        "node:result_decl": {
            "fld:type": {
                "node:integer_type": "41",
                "node:pointer_type": "7",
                "node:real_type": "1",
            }
        },
        "node:return_expr": {"fld:type": {"node:void_type": "51"}},
        "node:rshift_expr": {"fld:type": {"node:integer_type": "3"}},
        "node:string_cst": {"fld:type": {"node:array_type": "9"}},
        "node:switch_expr": {"fld:type": {"node:integer_type": "1"}},
        "node:tree_list": {
            "fld:valu": {
                "node:boolean_type": "9",
                "node:complex_type": "12",
                "node:enumeral_type": "15",
                "node:integer_type": "811",
                "node:pointer_type": "1227",
                "node:real_type": "89",
                "node:record_type": "3",
                "node:reference_type": "3",
                "node:union_type": "6",
                "node:vector_type": "105",
                "node:void_type": "4",
            }
        },
        "node:trunc_div_expr": {"fld:type": {"node:integer_type": "4"}},
        "node:truth_and_expr": {"fld:type": {"node:integer_type": "1"}},
        "node:truth_andif_expr": {"fld:type": {"node:integer_type": "20"}},
        "node:truth_orif_expr": {"fld:type": {"node:integer_type": "6"}},
        "node:type_decl": {
            "fld:type": {
                "node:array_type": "8",
                "node:boolean_type": "1",
                "node:complex_type": "5",
                "node:enumeral_type": "31",
                "node:function_type": "45",
                "node:integer_type": "161",
                "node:pointer_type": "17",
                "node:real_type": "8",
                "node:record_type": "167",
                "node:union_type": "48",
                "node:void_type": "2",
            }
        },
        "node:union_type": {
            "fld:flds": {"node:field_decl": "50"},
            "fld:name": {"node:identifier_node": "5", "node:type_decl": "13"},
            "fld:size": {"node:integer_cst": "50"},
            "fld:unql": {"node:union_type": "14"},
        },
        "node:var_decl": {
            "fld:type": {
                "node:array_type": "14",
                "node:integer_type": "95",
                "node:pointer_type": "30",
                "node:record_type": "7",
            }
        },
        "node:vector_type": {
            "fld:size": {"node:integer_cst": "12"},
            "fld:unql": {"node:vector_type": "1"},
        },
        "node:void_type": {
            "fld:name": {"node:type_decl": "5"},
            "fld:unql": {"node:void_type": "4"},
        },
    },
}

f = {}
skip = {"fld:source_file": 1}  # dont need this in the document


def query(s):
    results = prefix.q(
        """  
SELECT ?a ?p ?o ?t  WHERE {
    <%s> ?p ?o.
    optional {
       ?o rdf:type ?t.
    }
}
    """
        % s
    )
    d = {}
    dt = {}
    for x in results["results"]["bindings"]:
        v = prefix.clean(x["o"]["value"])
        t = None
        if "t" in x:
            t = prefix.clean(x["t"]["value"])
        else:
            # pprint.pprint(x)
            pass  # have no node type

        k = x["p"]["value"]
        k = prefix.clean(k)
        if k not in d:
            if k not in skip:
                d[k] = v  # the value of the field
                dt[k] = t  # the domain type of the field object
        else:
            # d[k]=[d[k],v]
            raise Exception("duplicate")

    return d, dt


# recurse
def recurse(s, deep=True):
    # print "RECURSE for %s\n" % s
    d, dt = query(s)
    # pprint.pprint({"Got from db":d})
    if "rdf:type" not in d:
        return d
    if not deep:
        return d
    st = d["rdf:type"]
    # print "st" + str(st)
    # pprint.pprint(dt)
    found = False

    for k in d:
        r = None  # result of the field
        ot = dt[k]
        v = d[k]
        u = prefix.tg + v

        if type(st) is dict:
            raise Exception("")
            pprint.pprint({"k": k, "ot": ot, "st": st})
            # pprint.pprint(dt)
            pass  # no type
        elif not ot:  # no type, a literal
            if k.startswith("fld:"):
                r = prefix.clean(v)  # just a literal
                found = True
            else:
                r = v  # we need to store the type field
                found = True

        elif st in tree["exprs"]:
            if k in tree["exprs"][st]:
                if ot in tree["exprs"][st][k]:
                    r = recurse(u)
                    found = True
                else:
                    pass  # skip

        if not found:
            if st in stree["exprs"]:
                if k in stree["exprs"][st]:
                    if ot in stree["exprs"][st][k]:
                        r = recurse(u, False)
                        # pprint.pprint(r)
                        found = True
                    else:
                        pass

        if not found:
            # just get one level of info for types and such
            r = recurse(u, False)

        d[k] = r

    return d


# print out what field types occur
def start():
    t = {}
    results = prefix.q(
        """  
SELECT ?a  WHERE {
  ?a fld:srcp 'eval.c:216'.
  ?a fld:name  [ fld:string 'parse_command'].
  ?a rdf:type nt:function_decl.
}
"""
    )
    for x in results["results"]["bindings"]:
        print((x["a"]["value"]))
        r = recurse(x["a"]["value"])
        pprint.pprint(rec(r))


start()
