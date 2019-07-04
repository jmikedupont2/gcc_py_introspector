# funcs = {}
import pprint
from functools import wraps

import ply.lex as lex

from gcc.tree.debug import debug, debug2, debug4
from gcc.tree.nodes import attrs, declare, reference
from gcc.tree.pprint2 import *
from gcc.tree.structure import generate_class
from gcc.tree.tnode import TNode
from gcc.tree.ast import Field


def get_value(x):
    # pprint.pprint({"get value":x})
    if "value" in x.__dict__:
        return x.value
    else:
        return None


def parser_rule(f):
    """
    parser rule
    """
    doc = f.__doc__
    @wraps(f)
    def wrapper(psr_val):
        r = f(psr_val)

        return r

    wrapper.doc = doc
    return wrapper



def parser_node_rule(f):
    """
    parser node rule
    """
    doc = f.__doc__
    # debug( 'Parser f', f, doc)
    # debug(pformat( dir(f)))
    # debug(pformat( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):

        anode_type = psr_val.slice[2].value.strip()
        node_id = declare(psr_val.slice[1])
        r = f(psr_val)
        cls = generate_class(anode_type)
        obj = cls(node_id, anode_type, [x.value for x in psr_val.slice[3:len(psr_val.slice)]]) # the rest of the slice
        psr_val[0] = obj

    wrapper.doc = doc
    return wrapper


def token_rule(f):
    """
    token rule
    """
    doc = f.__doc__

    # debug(pformat({
    #     'token decl function f': f,
    #     'doc': doc,
    #     'dict' : f.__dict__
    #     }))

    @wraps(f)
    def wrapper(tok):
        # debug(
        #     pformat(
        #         {
        #             "call function f": f,
        #             "doc": doc,
        #             "tok": tok,
        #             "lexpos": tok.lexpos,
        #             "lineno": tok.lineno,
        #             "type": tok.type,
        #             "value": tok.value,
        #             "dict": tok.__dict__,
        #         }
        #     )
        # )
        # debug(pformat2())
        # debug(pformat(dir(tok)))
        r = f(tok)
        if r is None:
            debug4(
                pformat(
                    {"none returned f": f, "doc": doc, "dict": f.__dict__}
                )
            )
            raise Exception("None returned")
        #else:
            #debug({"ret:": r})
        return r

    wrapper.doc = doc
    return wrapper


def register(name, theclass):
    registry[name] = theclass


# def node_type(name):

#     debug(pprint.pformat({
#         'decl node type function f': name,
#         'name' : name
#         }))
#         def __init__(self, theclass):
#             debug( {
#                 "init": self,
#                 "class": theclass,
#                 'name': name,
#                 })
#             registry[name]  =  theclass
#             #debug( "Created",self, theclass, name)
#         #     self.id_name= name
#         #     self.theclass = theclass
#         #     #node_type, node_id, psr_val
#         #     #self.obj = theclass()
#         #the_name = name
#     global  registry
#     # save this class
#     return SomeType


def report():
    debug("report")
    debug(pformat2(types))
    # debug(pformat2( funcs))




def parser_simple_rule(f):
    """
    parser simple rule
    """
    doc = f.__doc__
    # debug(pformat( dir(f)))
    # debug(pformat( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):
        field_name = psr_val.slice[1]
        field_value = psr_val.slice[2]
        psr_val[0] = Field(**{field_name.value: field_value.value})


    wrapper.doc = doc
    return wrapper


def parser_simple_rule_node(f):
    """
    parser simple rule
    """
    doc = f.__doc__
    # debug(pformat2( dir(f)))
    # debug(pformat2( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):
        field_name = psr_val.slice[1]
        field_value = psr_val.slice[2].value
        psr_val[0] = Field(**{field_name.value: field_value})


    wrapper.doc = doc
    return wrapper
