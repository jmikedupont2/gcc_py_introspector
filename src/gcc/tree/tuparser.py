"""
reader
"""

import ply.yacc as yacc  # Get the token map from the lexer.  This is required.

from gcc.tree.ast import *
import gcc.tree.nodes
import gcc.tree.tuast  # import Link
from gcc.tree.attributes import (
    parser_node_rule,
    parser_rule,
    parser_simple_rule,
)
from gcc.tree.generated_rules import *
from gcc.tree.generated_rules2 import *

# this first rule is synthetic and matches any nodes
from gcc.tree.symbol_table import declare_node, nodes_seen
from gcc.tree.tu import tokens
from gcc.tree.tu_attrs import *
from gcc.tree.utils import create_list, goto_initial  # , merge_list

start = "anynode"

# @parser_rule


def p_any_node(psr_val):
    "anynode : node "
    # the node declaration, top level
    psr_val[0] = psr_val[1].finished()

    #declare_node(psr_val[1])


# the first rule is important


@parser_rule
def p_node_id(psr_val):
    # the identifier node declaration
    "node : NODE HEXVAL attr_list"  # len_attrs
    psr_val[0] = Node(
        {
            "node": nodes.declare(psr_val[1]),
            "hexval": psr_val[2],
            "attr_list": psr_val[3],
        }
    )
    goto_initial(psr_val)  # begin the string group


@parser_node_rule
def p_node_constructor(psr_val):
    "node : NODE NTYPE_CONSTRUCTOR LEN idx_val_list"
    psr_val[0] = ConstructorList(
        node=psr_val[1],
        llen=psr_val[3],
        llist=psr_val[4],
        )


@parser_node_rule
def p_node_constructor_vals(psr_val):
    "node : NODE NTYPE_CONSTRUCTOR LEN val_list"
    psr_val[0] = gcc.tree.ast.Something(
        **{
            "__type__": "constructor",
            "node": psr_val[1],
            "idx_len": psr_val[3],
            "idx_list": psr_val[4],
        }
    )


@parser_node_rule
def p_node_constructor_empty(psr_val):
    "node : NODE NTYPE_CONSTRUCTOR LEN"
    psr_val[0] = gcc.tree.ast.Something(
        **{
            "__type__": "constructor",
            "node": psr_val[1],
            "idx_len": psr_val[3],
        }
    )


##########################################


@parser_rule
def p_operator_add(psr_val):
    "op_type : OPERATOR_ADD"
    psr_val[0] = gcc.tree.ast.Add()


@parser_rule
def p_operator_and(psr_val):
    "op_type : OPERATOR_AND"
    psr_val[0] = gcc.tree.ast.Amp()
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_andassign(psr_val):
    "op_type : OPERATOR_ANDASSIGN"
    psr_val[0] = gcc.tree.ast.PlusEqual()
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_addr(psr_val):
    "op_type : OPERATOR_ADDR"
    psr_val[0] = gcc.tree.ast.Operator("&")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_assign(psr_val):
    "op_type : OPERATOR_ASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_call(psr_val):
    "op_type : OPERATOR_CALL"
    psr_val[0] = gcc.tree.ast.Operator("call")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_compound(psr_val):
    "op_type : OPERATOR_COMPOUND"
    psr_val[0] = gcc.tree.ast.Operator("compound")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_delete(psr_val):
    "op_type : OPERATOR_DELETE"
    psr_val[0] = gcc.tree.ast.Operator("delete")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_deref(psr_val):
    "op_type : OPERATOR_DEREF"
    psr_val[0] = gcc.tree.ast.Operator("deref")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_div(psr_val):
    "op_type : OPERATOR_DIV"
    psr_val[0] = gcc.tree.ast.Operator("/")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_divassign(psr_val):
    "op_type : OPERATOR_DIVASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("/=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_eq(psr_val):
    "op_type : OPERATOR_EQ"
    psr_val[0] = gcc.tree.ast.Operator("==")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_ge(psr_val):
    "op_type : OPERATOR_GE"
    psr_val[0] = gcc.tree.ast.Operator(">=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_gt(psr_val):
    "op_type : OPERATOR_GT"
    psr_val[0] = gcc.tree.ast.Operator(">")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_le(psr_val):
    "op_type : OPERATOR_LE"
    psr_val[0] = gcc.tree.ast.Operator("<=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_lnot(psr_val):
    "op_type : OPERATOR_LNOT"
    psr_val[0] = gcc.tree.ast.Operator("lnot")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_lshift(psr_val):
    "op_type : OPERATOR_LSHIFT"
    psr_val[0] = gcc.tree.ast.Operator("left_shift")


@parser_rule
def p_operator_lshiftassign(psr_val):
    "op_type : OPERATOR_LSHIFTASSIGN"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_lt(psr_val):
    "op_type : OPERATOR_LT"
    psr_val[0] = gcc.tree.ast.Operator("<")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_minus(psr_val):
    "op_type : OPERATOR_MINUS"
    psr_val[0] = gcc.tree.ast.Operator("-")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_minusassign(psr_val):
    "op_type : OPERATOR_MINUSASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("-=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_mult(psr_val):
    "op_type : OPERATOR_MULT"
    psr_val[0] = gcc.tree.ast.Operator("*")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_multassign(psr_val):
    "op_type : OPERATOR_MULTASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("*=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_ne(psr_val):
    "op_type : OPERATOR_NE"
    psr_val[0] = gcc.tree.ast.Operator("!=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_neg(psr_val):
    "op_type : OPERATOR_NEG"
    psr_val[0] = gcc.tree.ast.Operator("!")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_new(psr_val):
    "op_type : OPERATOR_NEW"
    psr_val[0] = gcc.tree.ast.Operator("new")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_or(psr_val):
    "op_type : OPERATOR_OR"
    psr_val[0] = gcc.tree.ast.Operator("or")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_orassign(psr_val):
    "op_type : OPERATOR_ORASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("orassign")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_plus(psr_val):
    "op_type : OPERATOR_PLUS"
    psr_val[0] = gcc.tree.ast.Operator("+")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_plusassign(psr_val):
    "op_type : OPERATOR_PLUSASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("+=")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_postdec(psr_val):
    "op_type : OPERATOR_POSTDEC"
    psr_val[0] = gcc.tree.ast.Operator("postdec")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_postinc(psr_val):
    "op_type : OPERATOR_POSTINC"
    psr_val[0] = gcc.tree.ast.Operator("postinc")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_predec(psr_val):
    "op_type : OPERATOR_PREDEC"
    psr_val[0] = gcc.tree.ast.Operator("predec")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_preinc(psr_val):
    "op_type : OPERATOR_PREINC"
    psr_val[0] = gcc.tree.ast.Operator("preinc")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_rshift(psr_val):
    "op_type : OPERATOR_RSHIFT"
    psr_val[0] = gcc.tree.ast.Operator("rshift")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_vecdelete(psr_val):
    "op_type : OPERATOR_VECDELETE"
    psr_val[0] = gcc.tree.ast.Operator("vecdelete")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_vecnew(psr_val):
    "op_type : OPERATOR_VECNEW"
    psr_val[0] = gcc.tree.ast.Operator("vecnew")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_xor(psr_val):
    "op_type : OPERATOR_XOR"
    psr_val[0] = gcc.tree.ast.Operator("xor")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_xorassign(psr_val):
    "op_type : OPERATOR_XORASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("xorassign")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_not(psr_val):
    "op_type : OPERATOR_NOT"
    psr_val[0] = gcc.tree.ast.Operator("not")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_pos(psr_val):
    "op_type : OPERATOR_POS"
    psr_val[0] = gcc.tree.ast.Operator("pos")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_ref(psr_val):
    "op_type : OPERATOR_REF"
    psr_val[0] = gcc.tree.ast.Operator("ref")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_rshiftassign(psr_val):
    "op_type : OPERATOR_RSHIFTASSIGN"
    psr_val[0] = gcc.tree.ast.Operator("rshiftassign")
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_subs(psr_val):
    "op_type : OPERATOR_SUBS"
    psr_val[0] = "subs"


# @parser_rule
def p_idx_val_item(psr_val):
    "idx_val_list : ATTR_IDX NODE ATTR_VAL NODE attr_list"
    nd = NodeRef(psr_val[2], "idx")
    nd2 = NodeRef(psr_val[4], "val")
    addr = psr_val[5]
    psr_val[0] = gcc.tree.ast.Something(
        **{
            # 'type' : 'idx_val',
            # 'val' : {
            # 'idx':psr_val[1],
            # 'idx_node': nd,
            # 'attrval': psr_val[3],
            # 'val_node': nd2,
            "addr": addr,
            # }
        }
    )
    # nd.ref(psr_val[0])
    # nd2.ref(psr_val[0])


def p_idx_val_short(psr_val):
    "idx_val_list : ATTR_IDX NODE ATTR_VAL NODE"
    nd = NodeRef(psr_val[2],'idx')
    nd2 = NodeRef(psr_val[4],'val')
    psr_val[0] = ConstructorItem(idx=nd, val=nd2)


def p_val_item2(psr_val):
    "val_list : ATTR_VAL NODE val_list"
    nd = NodeRef(psr_val[2], "val")
    val = psr_val[3]
    psr_val[0] = gcc.tree.ast.Something(**{"val_node": nd, "value": val})


def p_val_item(psr_val):
    "val_list : ATTR_VAL NODE attr_list"
    nd = NodeRef(psr_val[2], "val")
    attr = psr_val[3]
    psr_val[0] = gcc.tree.ast.Something(**{"idx_node": nd, "attr": attr})


# @parser_rule
def p_idx_val_item2(psr_val):
    "idx_val_list : ATTR_IDX NODE ATTR_VAL NODE idx_val_list"
    nd = NodeRef(psr_val[2], "idx")
    nd2 = NodeRef(psr_val[4], "val")
    alist = psr_val[5]
    psr_val[0] = ConstructorListChain(ConstructorItem(idx=nd, val=nd2),alist)



@parser_rule
def p_attr_list2(psr_val):
    "attr_list : str_attrs attr_list"
    psr_val[0] = StringAttrs(**{"strattrs": psr_val[1], "alist": psr_val[2]})


@parser_rule
def p_attr_list2_end(psr_val):
    "attr_list : str_attrs"
    psr_val[0] = StringAttrs(**{"strattrs": psr_val[1]})


@parser_rule
def p_attr_list4(psr_val):
    "attr_list : addr_attrs attr_list"
    psr_val[0] = gcc.tree.ast.Something(
        **{"addr_attrs": psr_val[1], "list": psr_val[2]}
    )


@parser_rule
def p_attr_list_end(psr_val):
    "attr_list : addr_attrs"
    psr_val[0] = gcc.tree.ast.Something(**{"addr_attrs": psr_val[1]})


# @parser_rule
def p_attr_lista(psr_val):
    "attr_list : attrs"
    psr_val[0] = AttrList(attr=psr_val[1])


# @parser_rule
def p_attr_list3(psr_val):
    "attr_list : type_attrs attr_list"

    psr_val[0] = AttrList(attr=psr_val[1],
                          _list=psr_val[2])


def p_attr_list(psr_val):
    "attr_list : attrs attr_list"
    psr_val[0] = List(attr=psr_val[1],_list=psr_val[2])


# @parser_rule
def p_attr_list3a(psr_val):
    "attr_list : type_attrs"
    psr_val[0] = psr_val[1]

def p_error(x):
    print(("error occur %s" % x))
    raise Exception(x)


parser = yacc.yacc()
