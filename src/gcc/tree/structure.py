"""
gcc.tree.structure defines the structures in the model.
generates classes and provides lists of types.
"""
import gcc.tree.types


def generate_class(anode_type):
    new_name = "".join([a.title() for a in anode_type.split("_")])
    #c = '\n\nclass {}(NodeDecl):\n    """{}"""\n'.format(new_name, anode_type)
    # if not hasattr(gcc.tree.types, new_name):
    #     with open("classes.txt", "a") as fo:
    #         fo.write(c + "\n")
    #         # print(c)
    #         # setattr(gcc.tree.types, new_name, eval(c))
    # return None
    # else:
    return getattr(gcc.tree.types, new_name)


NODE_NAMES = """
addr_expr
aggr_init_expr
alignof_expr
array_ref
array_type
arrow_expr
asm_expr
baselink
bind_expr
binfo
bit_and_expr
bit_field_ref
bit_ior_expr
bit_not_expr
bit_xor_expr
boolean_type
bound_template_template_parm
break_stmt
call_expr
case_label_expr
cast_expr
complex_type
component_ref
compound_expr
compound_literal_expr
cond_expr
const_cast_expr
const_decl
constructor
continue_stmt
convert_expr
ctor_initializer
decl_expr
decltype_type
dl_expr
do_stmt
dotstar_expr
dynamic_cast_expr
enumeral_type
eq_expr
error_mark
expr_stmt
field_decl
float_expr
for_stmt
function_decl
function_type
ge_expr
goto_expr
gt_expr
handler
identifier_node
if_stmt
indirect_ref
integer_cst
integer_type
label_decl
label_expr
lang_type
le_expr
lrotate_expr
lshift_expr
lt_expr
max_expr
member_ref
mem_ref
method_type
min_expr
minus_expr
modify_expr
modop_expr
mult_expr
namespace_decl
ne_expr
negate_expr
nop_expr
nw_expr
offset_type
overload
parm_decl
plus_expr
pointer_bounds_type
pointer_plus_expr
pointer_type
postdecrement_expr
postincrement_expr
predecrement_expr
predict_expr
preincrement_expr
ptrmem_cst
rdiv_expr
real_cst
real_type
record_type
reference_type
reinterpret_cast_expr
result_decl
return_expr
rshift_expr
save_expr
scope_ref
sizeof_expr
statement_list
static_cast_expr
string_cst
switch_expr
switch_stmt
tag_defn
target_expr
template_decl
template_id_expr
template_parm_index
template_template_parm
template_type_parm
throw_expr
trait_expr
translation_unit_decl
tree_list
tree_vec
trunc_div_expr
trunc_mod_expr
truth_and_expr
truth_andif_expr
truth_not_expr
truth_or_expr
truth_orif_expr
try_block
type_decl
typeid_expr
typename_type
typeof_type
union_type
using_decl
using_stmt
var_decl
vector_type
void_type
while_stmt"""

NODE_TYPES = [x.strip() for x in NODE_NAMES.split("\n")]

# cut -d: -f1 ~/experiments/linux/tools/perf/util/header.c.001t.tu | cut  "-d " -f3 | sort -u
if __name__ == "__main__":
    for y in NODE_TYPES:
        print(("'{}'".format(y)))
        generate_class(y)
