import gcc.tree.nodes
import gcc.tree.pprint2
import gcc.tree.tuast
from gcc.tree.ast import Something
from gcc.tree.attributes import (
    parser_node_rule,
    parser_rule,
    parser_simple_rule,
    parser_simple_rule_node,
)
from gcc.tree.utils import create_list, goto_initial  # , merge_list


@parser_simple_rule_node
def p_attr_accs(psr_val):
    "attrs : ATTR_ACCS NODE"


@parser_simple_rule_node
def p_attr_access(psr_val):
    "attrs : ATTR_ACCS ACC"


@parser_simple_rule_node
def p_attr_op0(psr_val):
    "attrs : OP0_ATTR NODE"


@parser_simple_rule_node
def p_attr_op1(psr_val):
    "attrs : OP1_ATTR NODE"


@parser_simple_rule_node
def p_attr_labl(psr_val):
    "attrs : ATTR_LABL NODE"


@parser_simple_rule_node
def p_attr_vars(psr_val):
    "attrs : ATTR_VARS NODE"


@parser_simple_rule_node
def p_attr_args(psr_val):
    "attrs : ATTR_ARGS NODE"


@parser_simple_rule_node
def p_attr_argt(psr_val):
    "attrs : ATTR_ARGT NODE"


@parser_simple_rule_node
def p_attr_base(psr_val):
    "attrs : ATTR_BASE NODE"


@parser_simple_rule_node
def p_attr_bases(psr_val):
    "attrs : ATTR_BASES NODE"


@parser_simple_rule_node
def p_attr_bases_hex(psr_val):
    "attrs : ATTR_BASES SOMEHEX4"


@parser_simple_rule_node
def p_attr_bases_int(psr_val):
    "attrs : ATTR_BASES SOMEINT2"


@parser_simple_rule_node
def p_attr_binf(psr_val):
    "attrs : ATTR_BINF NODE"


@parser_simple_rule_node
def p_attr_bpos(psr_val):
    "attrs : ATTR_BPOS NODE"


@parser_simple_rule_node
def p_attr_chan(psr_val):
    "attrs : ATTR_CHAN NODE"


@parser_simple_rule_node
def p_attr_clas(psr_val):
    "attrs : ATTR_CLAS NODE"


@parser_simple_rule_node
def p_attr_clnp(psr_val):
    "attrs : ATTR_CLNP NODE"


@parser_simple_rule_node
def p_attr_cls(psr_val):
    "attrs : ATTR_CLS NODE"


@parser_simple_rule_node
def p_attr_cnst(psr_val):
    "attrs : ATTR_CNST NODE"


@parser_simple_rule_node
def p_attr_cond(psr_val):
    "attrs : ATTR_COND NODE"


@parser_simple_rule_node
def p_attr_crnt(psr_val):
    "attrs : ATTR_CRNT NODE"


@parser_simple_rule_node
def p_attr_csts(psr_val):
    "attrs : ATTR_CSTS NODE"


@parser_simple_rule_node
def p_attr_ctor(psr_val):
    "attrs : ATTR_CTOR NODE"


@parser_simple_rule_node
def p_attr_dcls(psr_val):
    "attrs : ATTR_DCLS NODE"


@parser_simple_rule_node
def p_attr_decl(psr_val):
    "attrs : ATTR_DECL NODE"


@parser_simple_rule_node
def p_attr_domn(psr_val):
    "attrs : ATTR_DOMN NODE"


@parser_simple_rule_node
def p_attr_else(psr_val):
    "attrs : ATTR_ELSE NODE"


@parser_simple_rule_node
def p_attr_elts(psr_val):
    "attrs : ATTR_ELTS NODE"


@parser_simple_rule_node
def p_attr_expr(psr_val):
    "attrs : ATTR_EXPR NODE"


@parser_simple_rule_node
def p_attr_flds(psr_val):
    "attrs : ATTR_FLDS NODE"


@parser_simple_rule_node
def p_attr_fn(psr_val):
    "attrs : ATTR_FN NODE"


@parser_simple_rule_node
def p_attr_fncs(psr_val):
    "attrs : ATTR_FNCS NODE"


@parser_simple_rule_node
def p_attr_hdlr(psr_val):
    "attrs : ATTR_HDLR NODE"


@parser_simple_rule_node
def p_attr_high(psr_val):
    "attrs : ATTR_HIGH NODE"


@parser_simple_rule_node
def p_attr_high_int(psr_val):
    "attrs : ATTR_HIGH SOMEINT2 "


@parser_simple_rule_node
def p_attr_init(psr_val):
    "attrs : ATTR_INIT NODE"


@parser_simple_rule_node
def p_attr_inst(psr_val):
    "attrs : ATTR_INST NODE"


@parser_simple_rule_node
def p_attr_lang(psr_val):
    "attrs : ATTR_LANG NODE"


@parser_simple_rule_node
def p_attr_line(psr_val):
    "attrs : ATTR_LINE NODE"


@parser_simple_rule_node
def p_attr_low(psr_val):
    "attrs : ATTR_LOW NODE"


@parser_simple_rule_node
def p_attr_low_int(psr_val):
    "attrs : ATTR_LOW SOMEINT2"


@parser_simple_rule_node
def p_attr_low_hex(psr_val):
    "attrs : ATTR_LOW SOMEHEX4"


@parser_simple_rule_node
def p_attr_max(psr_val):
    "attrs : ATTR_MAX NODE"


@parser_simple_rule_node
def p_attr_mbr(psr_val):
    "attrs : ATTR_MBR NODE"


@parser_simple_rule_node
def p_attr_min(psr_val):
    "attrs : ATTR_MIN NODE"


@parser_simple_rule_node
def p_attr_name(psr_val):
    "attrs : ATTR_NAME NODE"


@parser_simple_rule_node
def p_attr_nmsp(psr_val):
    "attrs : ATTR_NMSP NODE"


@parser_simple_rule_node
def p_attr_note(psr_val):
    "attrs : ATTR_NOTE NODE"


@parser_simple_rule_node
def p_attr_note_member(psr_val):
    "attrs : ATTR_NOTE MEMBER"


@parser_simple_rule_node
def p_attr_nst(psr_val):
    "attrs : ATTR_NST NODE"


@parser_simple_rule_node
def p_attr_orig(psr_val):
    "attrs : ATTR_ORIG NODE"


@parser_simple_rule_node
def p_attr_parm(psr_val):
    "attrs : ATTR_PARM NODE"


@parser_simple_rule_node
def p_attr_prms(psr_val):
    "attrs : ATTR_PRMS NODE"


@parser_simple_rule_node
def p_attr_ptd(psr_val):
    "attrs : ATTR_PTD NODE"


@parser_simple_rule_node
def p_attr_purp(psr_val):
    "attrs : ATTR_PURP NODE"


@parser_simple_rule
def p_attr_qual(psr_val):
    "attrs : ATTR_QUAL QUAL"


@parser_simple_rule
def p_attr_qual2(psr_val):
    "attrs : ATTR_QUAL SOMEHEX4"


@parser_simple_rule_node
def p_attr_refd(psr_val):
    "attrs : ATTR_REFD NODE"


@parser_simple_rule_node
def p_attr_retn(psr_val):
    "attrs : ATTR_RETN NODE"


@parser_simple_rule_node
def p_attr_rslt(psr_val):
    "attrs : ATTR_RSLT NODE"


@parser_simple_rule_node
def p_attr_scpe(psr_val):
    "attrs : ATTR_SCPE NODE"


@parser_simple_rule
def p_attr_sign(psr_val):
    "attrs : ATTR_SIGN SIGNED"


@parser_simple_rule_node
def p_attr_size(psr_val):
    "attrs : ATTR_SIZE NODE"


@parser_simple_rule_node
def p_attr_spcs(psr_val):
    "attrs : ATTR_SPCS NODE"


@parser_simple_rule
def p_attr_srcp(psr_val):
    "attrs : ATTR_SRCP BUILTIN_FILE"


@parser_simple_rule
def p_attr_srcp_hxx(psr_val):
    "attrs : ATTR_SRCP HXX_FILE"


@parser_simple_rule_node
def p_attr_sts(psr_val):
    "attrs : ATTR_STS NODE"


@parser_simple_rule
def p_attr_tag(psr_val):
    "attrs : ATTR_TAG STRUCT"


@parser_simple_rule_node
def p_attr_then(psr_val):
    "attrs : ATTR_THEN NODE"


@parser_simple_rule_node
def p_attr_unql(psr_val):
    "attrs : ATTR_UNQL NODE"


@parser_simple_rule
def p_attr_used(psr_val):
    "attrs : ATTR_USED SOMEINT2"
    goto_initial(psr_val)  # go back


@parser_simple_rule
def p_attr_used_hex(psr_val):
    "attrs : ATTR_USED SOMEHEX4"
    goto_initial(psr_val)  # go back


@parser_simple_rule_node
def p_attr_val(psr_val):
    "attrs : ATTR_VAL NODE"


@parser_simple_rule_node
def p_attr_idx(psr_val):
    "attrs : ATTR_IDX NODE"


@parser_simple_rule_node
def p_attr_valu(psr_val):
    "attrs : ATTR_VALU NODE"


@parser_simple_rule_node
def p_attr_vfld(psr_val):
    "attrs : ATTR_VFLD NODE"


@parser_simple_rule_node
def p_attr_OP(psr_val):
    "attrs : ATTR_OP NODE"


@parser_simple_rule_node
def p_attr_En(psr_val):
    "attrs : ATTR_En NODE"


class Addr:
    def __init__(self, addr):
        self.addr = addr


@parser_simple_rule
def p_attrs_addr(psr_val):
    "addr_attrs :  ADDR_ATTR SOMEINT"
    psr_val[0] = Addr(**{"addr": psr_val[2]})


@parser_simple_rule
def p_attrs_op0(psr_val):
    #           1     2     3
    "attrs :  OP0_ATTR op_type"


@parser_simple_rule
def p_attrs_op1(psr_val):
    "attrs :  OP1_ATTR op_type"


@parser_simple_rule
def p_attrs_spec2(psr_val):
    #            1          2        3        4
    "attrs :  SPEC_ATTR SPEC_REGISTER "


@parser_simple_rule
def p_attrs_spec3(psr_val):
    #            1          2        3        4
    "attrs :  SPEC_ATTR SPEC_VALU"


def p_attrs_spec4(psr_val):
    #            1          2        3        4
    "attrs :  SPEC_ATTR SPEC_VALU SPEC_VALU"
    psr_val[0] = Something(**{"spec": psr_val[2], "spec2": psr_val[3]})


# @parser_rule
def p_attrs_note(psr_val):
    "attrs :  ATTR_NOTE ARTIFICIAL"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


# @parser_rule
def p_attrs_note_opge(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_GE"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_note_opeq(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_EQ"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_note_opnot(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_LNOT"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_note_op_subs(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_SUBS"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_note_opgt(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_GT"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_note_ople(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_LE"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_note_oplt(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_LT"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_note_opne(psr_val):
    "attrs :  ATTR_NOTE OPERATOR_NE"
    psr_val[0] = Something(**{"note": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


# @parser_rule
def p_attrs_note_pt(psr_val):
    "attrs :  ATTR_NOTE PSEUDO TMPL"
    psr_val[0] = Something(**{"note": psr_val[1], "ntype": "pseudo_tmpl"})
    gcc.tree.nodes.attrs(psr_val[0])


# @parser_rule
def p_attrs_member(psr_val):
    "attrs : MEMBER"
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    psr_val[0] = Something(**{"member": psr_val[1]})
    gcc.tree.nodes.attrs(psr_val[0])


def p_attr_bitfield_single(psr_val):
    # this looks like a bug : @10519  field_decl       name: @10537   type: @10538   scpe: @10431 srcp: tcp.h:93                chain: @10539 bitfield       size: @10540   algn: 1 bpos: @757     addr: 7f81279f75f0
    "attrs : SPEC_VALU"
    psr_val[0] = Something(**{"note": "bitfield"})


def p_attr_spec_single(psr_val):
    # this looks like a bug : @8314   record_type      name: @10257   size: @20      algn: 8 spec           tag : struct   flds: @10258 fncs: @10259   binf: @10260
    "attrs : SPEC"
    psr_val[0] = Something(**{"note": "spec"})


@parser_simple_rule_node
def p_attr_mngl(psr_val):
    "attrs : ATTR_MNGL NODE"
    # psr_val[0] = 'mngl'


@parser_simple_rule_node
def p_attr_chain(psr_val):
    "attrs : ATTR_CHAIN NODE"
    # psr_val[0] = 'chain'


@parser_simple_rule
def p_attrs_link(psr_val):
    "attrs :  ATTR_LINK LINK"


@parser_simple_rule
def p_attrs_body(psr_val):
    "attrs :  ATTR_BODY LINK"


@parser_simple_rule_node
def p_attrs_body2(psr_val):
    "attrs :  ATTR_BODY NODE"


@parser_simple_rule
def p_attrs_prec(psr_val):
    #           1     2         3
    "attrs :  ATTR_PREC SOMEINT2"
    goto_initial(psr_val)  # begin the string group


@parser_simple_rule
def p_attrs_prec2(psr_val):
    #           1     2         3
    "attrs :  ATTR_PREC SOMEHEX4"
    goto_initial(psr_val)  # begin the string group


@parser_simple_rule
def p_attrs_algn(psr_val):
    #           1     2         3
    "attrs :  ATTR_ALGN SOMEINT"
    goto_initial(psr_val)  # begin the string group


@parser_simple_rule
def p_attrs_algn2(psr_val):
    #           1     2         3
    "attrs :  ATTR_ALGN SOMEHEX4"
    goto_initial(psr_val)  # begin the string group


def p_attrs_strg_empty(psr_val):
    "str_attrs : STRG "  # no string....
    m = psr_val[1]
    if m:
        # print "simple string list '%s'" % m
        if isinstance(m, str):
            psr_val[0] = Something(**{"string_val": m})
        else:
            psr_val[0] = Something(**{"string_val": m.val})
        gcc.tree.nodes.attrs(psr_val[0])
    goto_initial(psr_val)


def p_attrs_addrs2(psr_val):
    "addr_attrs : ADDR_ATTR SOMEHEX3"
    m = psr_val[2]
    if m:
        # print "address is set to", m
        psr_val[0] = Something(**{"addr": m})
        gcc.tree.nodes.attrs(psr_val[0])
    goto_initial(psr_val)


def p_attrs_addrs3(psr_val):
    "addr_attrs : ADDR_ATTR SOMEHEX4"
    m = psr_val[2]
    if m:
        # print "address is set to", m
        psr_val[0] = Something(**{"addr": m})
        gcc.tree.nodes.attrs(psr_val[0])
    goto_initial(psr_val)


def p_attrs_type6(psr_val):
    #           type_     2     3
    "type_attrs : TYPE_ATTR NODE INT SOMEINT2"
    goto_initial(psr_val)  # go back
    # print 'finished TYPE_ATTR NODE'
    # psr_val[0] = std_attrs(psr_val)
    nd = psr_val[2]
    field_value = gcc.tree.nodes.reference(nd, "type")
    psr_val[0] = Something(
        **{
            # 'type': 'type',
            # 'val': {
            # 'type' : nd,
            "type_name": "int",
            "type_value": psr_val[4]
            # }
        }
    )
    gcc.tree.nodes.attrs(psr_val[0])


# @parser_rule
def p_attrs_type3(psr_val):
    #           type_     2     3
    "type_attrs : TYPE_ATTR NODE INT SOMEHEX2"
    goto_initial(psr_val)  # go back
    # print 'finished TYPE_ATTR NODE'
    # psr_val[0] = std_attrs(psr_val)
    nd = gcc.tree.nodes.reference(psr_val[2], "type")
    psr_val[0] = Something(
        **{
            # 'type': 'type',
            # 'val': {
            # 'type': psr_val[2],
            "type_name": "int",
            "type_value": psr_val[4]
            # }
        }
    )
    # nd.ref(psr_val[0])
    gcc.tree.nodes.attrs(psr_val[0])


# @parser_rule
def p_attrs_type3b(psr_val):
    #           type_     2     3
    "type_attrs : TYPE_ATTR NODE INT SOMEHEX3"
    goto_initial(psr_val)  # go back
    # print 'finished TYPE_ATTR NODE'
    # psr_val[0] = std_attrs(psr_val)
    # psr_val[0] = [psr_val[1],psr_val[2],psr_val[3],psr_val[4]]
    nd = gcc.tree.nodes.reference(psr_val[2], "type")
    psr_val[0] = Something(
        **{
            # 'type': 'type',
            # 'val' : {
            # 'type': psr_val[2],
            "type_name": "int",
            "type_value": psr_val[4]
            # }
        }
    )
    # nd.ref(psr_val[0])

    gcc.tree.nodes.attrs(psr_val[0])


def p_attrs_type4b(psr_val):
    #           type_     2     3
    "type_attrs : TYPE_ATTR NODE INT SOMEHEX4"
    goto_initial(psr_val)  # go back
    # print 'finished TYPE_ATTR NODE'
    # psr_val[0] = std_attrs(psr_val)
    # psr_val[0] = [psr_val[1],psr_val[2],psr_val[3],psr_val[4]]
    nd = gcc.tree.nodes.reference(psr_val[2], "type")
    psr_val[0] = Something(
        **{
            # 'type': 'type',
            # 'val' : {
            # 'type': psr_val[2],
            "type_name": "int",
            "type_value": psr_val[4]
            # }
        }
    )
    # nd.ref(psr_val[0])
    gcc.tree.nodes.attrs(psr_val[0])


# @parser_rule
def p_attrs_type5(psr_val):
    #           type_     2     3
    "type_attrs : TYPE_ATTR NODE"  # len_attrs
    # print 'finished TYPE_ATTR NODE'
    # goto_initial(psr_val)  # go back
    # psr_val[0] = std_attrs(psr_val)
    nd = gcc.tree.nodes.reference(psr_val[2], "type")
    psr_val[0] = Something(**{"type": "type", "val": {"type": psr_val[2]}})
    # nd.ref( psr_val[0])
    gcc.tree.nodes.attrs(psr_val[0])


# parser_rule
def p_attrs_strg3(psr_val):
    "str_attrs : STRG SOMESTRG"
    m = psr_val[2]
    if m:
        # print "simple string '%s'" % m
        psr_val[0] = Something(**{"string": gcc.tree.tuast.String2(m)})
    goto_initial(psr_val)
    gcc.tree.nodes.attrs(psr_val[0])


# @parser_rule
def p_attrs_addrs(psr_val):
    "addr_attrs : ADDR_ATTR HEXVAL"
    m = psr_val[2]
    # if m:
    # print "address is set to", m
    # psr_val[0] = [tuast.String(m)]
    # print 'after hexval'
    goto_initial(psr_val)
    psr_val[0] = Something(**{"addr": m})
    gcc.tree.nodes.attrs({"addr": m})


@parser_simple_rule_node
def p_attr_valu_real(psr_val):
    "attrs : ATTR_VALU REALVALUE"
