import json
import pprint


class NodeDecl:
    """A node is declared in the tu file for the first time with an id and a node type"""

    def __init__(self, _id, _type, value):
        self._id = _id
        self._type = _type

    def to_json(self):
        #print((json.dumps(self.__dict__)))
        pass


class TypeDecl(NodeDecl):
    "type_decl"


class IdentifierNode(NodeDecl):
    """identifier_node"""


class IntegerType(NodeDecl):
    """integer_type"""


class IntegerCst(NodeDecl):
    """integer_cst"""


class RealType(NodeDecl):
    """real_type"""


class ComplexType(NodeDecl):
    """complex_type"""


class VoidType(NodeDecl):
    """void_type"""


class ArrayType(NodeDecl):
    """array_type"""


class RecordType(NodeDecl):
    """record_type"""


class AggrInitExpr(NodeDecl):
    """aggr_init_expr"""


class AlignofExpr(NodeDecl):
    """alignof_expr"""


class AsmExpr(NodeDecl):
    """asm_expr"""


class SaveExpr(NodeDecl):
    """save_expr"""


class ArrayRef(NodeDecl):
    """array_ref"""


class ArrowExpr(NodeDecl):
    """arrow_expr"""


class Baselink(NodeDecl):
    """baselink"""


class BindExpr(NodeDecl):
    """bind_expr"""


class Binfo(NodeDecl):
    """binfo"""


class BitAndExpr(NodeDecl):
    """bit_and_expr"""


class BitIorExpr(NodeDecl):
    """bit_ior_expr"""


class BitNotExpr(NodeDecl):
    """bit_not_expr"""


class BitXorExpr(NodeDecl):
    """bit_xor_expr"""


class BitFieldRef(NodeDecl):
    """bit_field_ref"""


class BooleanType(NodeDecl):
    """boolean_type"""


class BoundTemplateTemplateParm(NodeDecl):
    """bound_template_template_parm"""


class BreakStmt(NodeDecl):
    """break_stmt"""


class CallExpr(NodeDecl):
    """call_expr"""


class CaseLabelExpr(NodeDecl):
    """case_label_expr"""


class CastExpr(NodeDecl):
    """cast_expr"""


class ComponentRef(NodeDecl):
    """component_ref"""


class CompoundExpr(NodeDecl):
    """compound_expr"""


class ConvertExpr(NodeDecl):
    """convert_expr"""


class CondExpr(NodeDecl):
    """cond_expr"""


class ConstCastExpr(NodeDecl):
    """const_cast_expr"""


class ConstDecl(NodeDecl):
    """const_decl"""


class ContinueStmt(NodeDecl):
    """continue_stmt"""


class CtorInitializer(NodeDecl):
    """ctor_initializer"""


class DeclExpr(NodeDecl):
    """decl_expr"""


class DecltypeType(NodeDecl):
    """decltype_type"""


class DlExpr(NodeDecl):
    """dl_expr"""


class DoStmt(NodeDecl):
    """do_stmt"""


class DotstarExpr(NodeDecl):
    """dotstar_expr"""


class DynamicCastExpr(NodeDecl):
    """dynamic_cast_expr"""


class EnumeralType(NodeDecl):
    """enumeral_type"""


class EqExpr(NodeDecl):
    """eq_expr"""


class ErrorMark(NodeDecl):
    """error_mark"""


class ExprStmt(NodeDecl):
    """expr_stmt"""


class FieldDecl(NodeDecl):
    """field_decl"""


class ForStmt(NodeDecl):
    """for_stmt"""


class FunctionDecl(NodeDecl):
    """function_decl"""


class FunctionType(NodeDecl):
    """function_type"""


class GeExpr(NodeDecl):
    """ge_expr"""


class GotoExpr(NodeDecl):
    """goto_expr"""


class GtExpr(NodeDecl):
    """gt_expr"""


class Handler(NodeDecl):
    """handler"""


class IfStmt(NodeDecl):
    """if_stmt"""


class IndirectRef(NodeDecl):
    """indirect_ref"""


class LabelDecl(NodeDecl):
    """label_decl"""


class LangType(NodeDecl):
    """lang_type"""


class LeExpr(NodeDecl):
    """le_expr"""


class LshiftExpr(NodeDecl):
    """lshift_expr"""


class LtExpr(NodeDecl):
    """lt_expr"""


class LabelExpr(NodeDecl):
    """label_expr"""


class MemberRef(NodeDecl):
    """member_ref"""


class MemRef(NodeDecl):
    """mem_ref"""


class MethodType(NodeDecl):
    """method_type"""


class MinusExpr(NodeDecl):
    """minus_expr"""


class ModopExpr(NodeDecl):
    """modop_expr"""


class ModifyExpr(NodeDecl):
    """modify_expr"""


class MultExpr(NodeDecl):
    """mult_expr"""


class NamespaceDecl(NodeDecl):
    """namespace_decl"""


class NeExpr(NodeDecl):
    """ne_expr"""


class NegateExpr(NodeDecl):
    """negate_expr"""


class NopExpr(NodeDecl):
    """nop_expr"""


class NwExpr(NodeDecl):
    """nw_expr"""


class OffsetType(NodeDecl):
    """offset_type"""


class Overload(NodeDecl):
    """overload"""


class ParmDecl(NodeDecl):
    """parm_decl"""


class PlusExpr(NodeDecl):
    """plus_expr"""


class PointerType(NodeDecl):
    """pointer_type"""


class PointerBoundsType(NodeDecl):
    """pointer_bounds_type"""


class PointerPlusExpr(NodeDecl):
    """pointer_plus_expr"""


class PostdecrementExpr(NodeDecl):
    """postdecrement_expr"""


class PostincrementExpr(NodeDecl):
    """postincrement_expr"""


class PredecrementExpr(NodeDecl):
    """predecrement_expr"""


class PreincrementExpr(NodeDecl):
    """preincrement_expr"""


class PredictExpr(NodeDecl):
    """predict_expr"""


class PtrmemCst(NodeDecl):
    """ptrmem_cst"""


class RealCst(NodeDecl):
    """real_cst"""


class ResultDecl(NodeDecl):
    """result_decl"""


class ReferenceType(NodeDecl):
    """reference_type"""


class ReinterpretCastExpr(NodeDecl):
    """reinterpret_cast_expr"""


class ReturnExpr(NodeDecl):
    """return_expr"""


class RshiftExpr(NodeDecl):
    """rshift_expr"""


class ScopeRef(NodeDecl):
    """scope_ref"""


class SizeofExpr(NodeDecl):
    """sizeof_expr"""


class StatementList(NodeDecl):
    """statement_list"""


class StaticCastExpr(NodeDecl):
    """static_cast_expr"""


class StringCst(NodeDecl):
    """string_cst"""


class SwitchStmt(NodeDecl):
    """switch_stmt"""


class SwitchExpr(NodeDecl):
    """switch_expr"""


class TagDefn(NodeDecl):
    """tag_defn"""


class TargetExpr(NodeDecl):
    """target_expr"""


class TemplateDecl(NodeDecl):
    """template_decl"""


class TemplateIdExpr(NodeDecl):
    """template_id_expr"""


class TemplateParmIndex(NodeDecl):
    """template_parm_index"""


class TemplateTemplateParm(NodeDecl):
    """template_template_parm"""


class TemplateTypeParm(NodeDecl):
    """template_type_parm"""


class ThrowExpr(NodeDecl):
    """throw_expr"""


class TraitExpr(NodeDecl):
    """trait_expr"""


class TranslationUnitDecl(NodeDecl):
    """translation_unit_decl"""


class TreeList(NodeDecl):
    """tree_list"""


class TreeVec(NodeDecl):
    """tree_vec"""


class TruncDivExpr(NodeDecl):
    """trunc_div_expr"""


class TruncModExpr(NodeDecl):
    """trunc_mod_expr"""


class TruthAndExpr(NodeDecl):
    """truth_and_expr"""


class TruthOrExpr(NodeDecl):
    """truth_or_expr"""


class TruthAndifExpr(NodeDecl):
    """truth_andif_expr"""


class TruthNotExpr(NodeDecl):
    """truth_not_expr"""


class TruthOrifExpr(NodeDecl):
    """truth_orif_expr"""


class TryBlock(NodeDecl):
    """try_block"""


class TypeidExpr(NodeDecl):
    """typeid_expr"""


class TypenameType(NodeDecl):
    """typename_type"""


class TypeofType(NodeDecl):
    """typeof_type"""


class UnionType(NodeDecl):
    """union_type"""


class UsingDecl(NodeDecl):
    """using_decl"""


class UsingStmt(NodeDecl):
    """using_stmt"""


class VarDecl(NodeDecl):
    """var_decl"""


class VectorType(NodeDecl):
    """vector_type"""


class WhileStmt(NodeDecl):
    """while_stmt"""


class RdivExpr(NodeDecl):
    """rdiv_expr"""


class MinExpr(NodeDecl):
    """min_expr"""


class MaxExpr(NodeDecl):
    """max_expr"""


class LrotateExpr(NodeDecl):
    """lrotate_expr"""


class FloatExpr(NodeDecl):
    """float_expr"""


class Constructor(NodeDecl):
    """constructor"""


class CompoundLiteralExpr(NodeDecl):
    """compound_literal_expr"""


class AddrExpr(NodeDecl):
    """addr_expr """
