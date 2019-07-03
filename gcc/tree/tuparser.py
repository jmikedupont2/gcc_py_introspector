"""
reader
"""
from gcc.tree.generated_rules2 import *
from gcc.tree.generated_rules import *
from gcc.tree.tu_attrs import *
import gcc.tree.nodes
from gcc.tree.utils import goto_initial, create_list  # , merge_list
import gcc.tree.tuast  # import Link
from gcc.tree.tu import tokens
import ply.yacc as yacc  # Get the token map from the lexer.  This is required.
import gcc.tree.pprint2
import pprint
from gcc.tree.attributes import parser_rule, parser_node_rule, parser_simple_rule

# this first rule is synthetic and matches any nodes
from gcc.tree.symbol_table import nodes_seen, declare_node


class StringAttrs:
    def __init__(self, strattrs, alist=None):
        self.string = strattrs
        self._list = alist


class List:
    def __init__(self, attrs, _list):
        self.attrs = attrs
        self._list = list

    def collapse(self):
        # todo
        ""


start = "anynode"

# @parser_rule


def p_any_node(psr_val):
    "anynode : node "
    # the node declaration
    psr_val[0] = psr_val[1]

    declare_node(psr_val[1])


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
    psr_val[0] = {
        "__type__": "constructor",
        "node": psr_val[1],
        "idx_len": psr_val[3],
        "idx_list": psr_val[4],
    }


# pprint.pprint(psr_val[0])


@parser_node_rule
def p_node_constructor_vals(psr_val):
    "node : NODE NTYPE_CONSTRUCTOR LEN val_list"
    psr_val[0] = {
        "__type__": "constructor",
        "node": psr_val[1],
        "idx_len": psr_val[3],
        "idx_list": psr_val[4],
    }


# pprint.pprint(psr_val[0])


@parser_node_rule
def p_node_constructor_empty(psr_val):
    "node : NODE NTYPE_CONSTRUCTOR LEN"
    psr_val[0] = {"__type__": "constructor", "node": psr_val[1], "idx_len": psr_val[3]}


# pprint.pprint(psr_val[0])


##########################################


@parser_rule
def p_operator_add(psr_val):
    "op_type : OPERATOR_ADD"
    psr_val[0] = "+"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_and(psr_val):
    "op_type : OPERATOR_AND"
    psr_val[0] = "&"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_andassign(psr_val):
    "op_type : OPERATOR_ANDASSIGN"
    psr_val[0] = "+="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_addr(psr_val):
    "op_type : OPERATOR_ADDR"
    psr_val[0] = "&"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_assign(psr_val):
    "op_type : OPERATOR_ASSIGN"
    psr_val[0] = "="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_call(psr_val):
    "op_type : OPERATOR_CALL"
    psr_val[0] = "call"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_compound(psr_val):
    "op_type : OPERATOR_COMPOUND"
    psr_val[0] = "compound"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_delete(psr_val):
    "op_type : OPERATOR_DELETE"
    psr_val[0] = "delete"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_deref(psr_val):
    "op_type : OPERATOR_DEREF"
    psr_val[0] = "deref"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_div(psr_val):
    "op_type : OPERATOR_DIV"
    psr_val[0] = "/"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_divassign(psr_val):
    "op_type : OPERATOR_DIVASSIGN"
    psr_val[0] = "/="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_eq(psr_val):
    "op_type : OPERATOR_EQ"
    psr_val[0] = "=="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_ge(psr_val):
    "op_type : OPERATOR_GE"
    psr_val[0] = ">="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_gt(psr_val):
    "op_type : OPERATOR_GT"
    psr_val[0] = ">"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_le(psr_val):
    "op_type : OPERATOR_LE"
    psr_val[0] = "<="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_lnot(psr_val):
    "op_type : OPERATOR_LNOT"
    psr_val[0] = "lnot"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_lshift(psr_val):
    "op_type : OPERATOR_LSHIFT"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_lshiftassign(psr_val):
    "op_type : OPERATOR_LSHIFTASSIGN"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_lt(psr_val):
    "op_type : OPERATOR_LT"
    psr_val[0] = "<"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_minus(psr_val):
    "op_type : OPERATOR_MINUS"
    psr_val[0] = "-"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_minusassign(psr_val):
    "op_type : OPERATOR_MINUSASSIGN"
    psr_val[0] = "-="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_mult(psr_val):
    "op_type : OPERATOR_MULT"
    psr_val[0] = "*"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_multassign(psr_val):
    "op_type : OPERATOR_MULTASSIGN"
    psr_val[0] = "*="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_ne(psr_val):
    "op_type : OPERATOR_NE"
    psr_val[0] = "!="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_neg(psr_val):
    "op_type : OPERATOR_NEG"
    psr_val[0] = "!"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_new(psr_val):
    "op_type : OPERATOR_NEW"
    psr_val[0] = "new"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_or(psr_val):
    "op_type : OPERATOR_OR"
    psr_val[0] = "or"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_orassign(psr_val):
    "op_type : OPERATOR_ORASSIGN"
    psr_val[0] = "orassign"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_plus(psr_val):
    "op_type : OPERATOR_PLUS"
    psr_val[0] = "+"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_plusassign(psr_val):
    "op_type : OPERATOR_PLUSASSIGN"
    psr_val[0] = "+="
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_postdec(psr_val):
    "op_type : OPERATOR_POSTDEC"
    psr_val[0] = "postdec"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_postinc(psr_val):
    "op_type : OPERATOR_POSTINC"
    psr_val[0] = "postinc"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_predec(psr_val):
    "op_type : OPERATOR_PREDEC"
    psr_val[0] = "predec"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_preinc(psr_val):
    "op_type : OPERATOR_PREINC"
    psr_val[0] = "preinc"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_rshift(psr_val):
    "op_type : OPERATOR_RSHIFT"
    psr_val[0] = "rshift"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_vecdelete(psr_val):
    "op_type : OPERATOR_VECDELETE"
    psr_val[0] = "vecdelete"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_vecnew(psr_val):
    "op_type : OPERATOR_VECNEW"
    psr_val[0] = "vecnew"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_xor(psr_val):
    "op_type : OPERATOR_XOR"
    psr_val[0] = "xor"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_xorassign(psr_val):
    "op_type : OPERATOR_XORASSIGN"
    psr_val[0] = "xorassign"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_not(psr_val):
    "op_type : OPERATOR_NOT"
    psr_val[0] = "not"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_pos(psr_val):
    "op_type : OPERATOR_POS"
    psr_val[0] = "pos"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_ref(psr_val):
    "op_type : OPERATOR_REF"
    psr_val[0] = "ref"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_rshiftassign(psr_val):
    "op_type : OPERATOR_RSHIFTASSIGN"
    psr_val[0] = "rshiftassign"
    # psr_val[0] = operator_base(psr_val)


@parser_rule
def p_operator_subs(psr_val):
    "op_type : OPERATOR_SUBS"
    psr_val[0] = "subs"


# @parser_rule
def p_idx_val_item(psr_val):
    "idx_val_list : ATTR_IDX NODE ATTR_VAL NODE attr_list"
    nd = gcc.tree.nodes.reference(psr_val[2], "idx")
    nd2 = gcc.tree.nodes.reference(psr_val[4], "val")
    addr = psr_val[5]
    psr_val[0] = {
        # 'type' : 'idx_val',
        # 'val' : {
        # 'idx':psr_val[1],
        # 'idx_node': nd,
        # 'attrval': psr_val[3],
        # 'val_node': nd2,
        "addr": addr,
        # }
    }
    # nd.ref(psr_val[0])
    # nd2.ref(psr_val[0])


def p_idx_val_short(psr_val):
    "idx_val_list : ATTR_IDX NODE ATTR_VAL NODE"
    nd = gcc.tree.nodes.reference(psr_val[2], "idx")
    nd2 = gcc.tree.nodes.reference(psr_val[4], "val")
    psr_val[0] = {"idx": nd, "val": nd2}


def p_val_item2(psr_val):
    "val_list : ATTR_VAL NODE val_list"
    nd = gcc.tree.nodes.reference(psr_val[2], "val")
    val = psr_val[3]
    psr_val[0] = {
        # 'type' : 'val',
        # 'val' : {
        "val_node": nd,
        "value": val,
        # }
    }


def p_val_item(psr_val):
    "val_list : ATTR_VAL NODE attr_list"
    nd = gcc.tree.nodes.reference(psr_val[2], "val")
    attr = psr_val[3]
    psr_val[0] = {
        # 'type' : 'val',
        # 'val' : {
        "idx_node": nd,
        "attr": attr,
        # }
    }


# @parser_rule
def p_idx_val_item2(psr_val):
    "idx_val_list : ATTR_IDX NODE ATTR_VAL NODE idx_val_list"
    nd = gcc.tree.nodes.reference(psr_val[2], "idx")
    nd2 = gcc.tree.nodes.reference(psr_val[4], "val")
    alist = psr_val[5]
    psr_val[0] = {
        # 'type' : 'idx_val',
        # 'val' : {
        # 'idx':psr_val[1],
        "idx_node": nd,
        "val_node": nd2,
        "list": alist,
    }


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
    psr_val[0] = {"addr_attrs": psr_val[1], "list": psr_val[2]}


@parser_rule
def p_attr_list_end(psr_val):
    "attr_list : addr_attrs"
    psr_val[0] = {"addr_attrs": psr_val[1]}


# @parser_rule
def p_attr_lista(psr_val):
    "attr_list : attrs"
    psr_val[0] = psr_val[1]


# @parser_rule
def p_attr_list3(psr_val):
    "attr_list : type_attrs attr_list"
    # psr_val[0] = {'type_attrs'psr_val[1],psr_val[2]{
    psr_val[0] = List(
        **{
            # '__type__':'attr_list',
            "attrs": psr_val[1],
            "_list": psr_val[2],
        }
    ).collapse()


def p_attr_list(psr_val):
    "attr_list : attrs attr_list"
    # pprint.pprint({'psr_val':psr_val.slice})
    # pprint.pprint({'psr_val1':psr_val[1]})
    # pprint.pprint({'psr_val2':psr_val[2]})
    psr_val[0] = List(
        **{"attrs": psr_val[1], "_list": psr_val[2]}  # '__type__':'attr_list',
    ).collapse()


# @parser_rule
def p_attr_list3a(psr_val):
    "attr_list : type_attrs"
    # pprint.pprint({'psr_val':psr_val.slice})
    # pprint.pprint({'psr_val1':psr_val[1]})

    psr_val[0] = psr_val[1]


def p_error(x):
    print(("error occur %s" % x))
    raise Exception(x)


parser = yacc.yacc()
