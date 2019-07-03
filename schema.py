import pprint

d = {
    "addr_expr ": {
        "attrs_addr": 3197,
        "nid": 3197,
        "refs_OP0": {
            "array_ref": 5,
            "component_ref": 43,
            "function_decl": 1644,
            "parm_decl": 22,
            "string_cst": 1062,
            "var_decl": 421,
        },
        "refs_type": {"pointer_type": 3197},
        "type": 3197,
    },
    "array_ref": {
        "attrs_addr": 187,
        "nid": 187,
        "refs_OP0": {"component_ref": 64, "var_decl": 123},
        "refs_OP1": {"component_ref": 1, "integer_cst": 121, "var_decl": 65},
        "refs_type": {"integer_type": 122, "pointer_type": 1, "record_type": 64},
        "type": 187,
    },
    "array_type": {
        "attrs_addr": 1009,
        "nid": 1009,
        "refs_domn": {"integer_type": 967},
        "refs_elts": {"integer_type": 737, "pointer_type": 81, "record_type": 191},
        "refs_name": {"type_decl": 90},
        "refs_size": {"integer_cst": 956},
        "refs_unql": {"array_type": 124},
        "type": 1009,
    },
    "bind_expr": {
        "attrs_addr": 756,
        "nid": 756,
        "refs_body": {
            "call_expr": 1,
            "cond_expr": 63,
            "convert_expr": 2,
            "return_expr": 353,
            "statement_list": 337,
        },
        "refs_type": {"void_type": 756},
        "refs_vars": {"var_decl": 321},
        "type": 756,
    },
    "bit_and_expr": {
        "attrs_addr": 323,
        "nid": 323,
        "refs_OP0": {
            "array_ref": 11,
            "bit_field_ref": 1,
            "bit_not_expr": 1,
            "call_expr": 1,
            "component_ref": 32,
            "convert_expr": 62,
            "lshift_expr": 33,
            "modify_expr": 2,
            "nop_expr": 96,
            "parm_decl": 41,
            "rshift_expr": 3,
            "var_decl": 40,
        },
        "refs_OP1": {
            "bit_not_expr": 11,
            "integer_cst": 293,
            "plus_expr": 4,
            "var_decl": 15,
        },
        "refs_type": {"integer_type": 323},
        "type": 323,
    },
    "bit_field_ref": {
        "attrs_addr": 1,
        "nid": 1,
        "refs_OP0": {"mem_ref": 1},
        "refs_OP1": {"integer_cst": 1},
        "refs_OP2": {"integer_cst": 1},
        "refs_type": {"integer_type": 1},
        "type": 1,
    },
    "bit_ior_expr": {
        "attrs_addr": 127,
        "nid": 127,
        "refs_OP0": {
            "array_ref": 11,
            "bit_and_expr": 33,
            "bit_ior_expr": 12,
            "component_ref": 20,
            "indirect_ref": 10,
            "nop_expr": 11,
            "save_expr": 1,
            "var_decl": 29,
        },
        "refs_OP1": {
            "bit_and_expr": 55,
            "component_ref": 2,
            "integer_cst": 53,
            "parm_decl": 1,
            "var_decl": 16,
        },
        "refs_type": {"integer_type": 127},
        "type": 127,
    },
    "bit_not_expr": {
        "attrs_addr": 12,
        "nid": 12,
        "refs_OP0": {"component_ref": 1, "var_decl": 11},
        "refs_type": {"integer_type": 12},
        "type": 12,
    },
    "bit_xor_expr": {
        "attrs_addr": 1,
        "nid": 1,
        "refs_OP0": {"lshift_expr": 1},
        "refs_OP1": {"var_decl": 1},
        "refs_type": {"integer_type": 1},
        "type": 1,
    },
    "boolean_type": {
        "attrs_addr": 12,
        "nid": 12,
        "refs_name": {"type_decl": 12},
        "refs_size": {"integer_cst": 12},
        "type": 12,
    },
    "call_expr": {
        "attrs_addr": 1654,
        "nid": 1654,
        "refs_E": {
            "addr_expr ": 243,
            "bit_and_expr": 1,
            "call_expr": 22,
            "component_ref": 70,
            "cond_expr": 44,
            "convert_expr": 29,
            "eq_expr": 2,
            "ge_expr": 66,
            "indirect_ref": 53,
            "integer_cst": 764,
            "minus_expr": 6,
            "mult_expr": 2,
            "ne_expr": 1,
            "nop_expr": 1623,
            "parm_decl": 505,
            "plus_expr": 38,
            "pointer_plus_expr": 5,
            "trunc_mod_expr": 1,
            "truth_or_expr": 1,
            "var_decl": 472,
        },
        "refs_fn": {"addr_expr ": 1643, "parm_decl": 11},
        "refs_type": {
            "integer_type": 1109,
            "pointer_type": 281,
            "real_type": 11,
            "void_type": 253,
        },
        "type": 1654,
    },
    "case_label_expr": {
        "attrs_addr": 154,
        "nid": 154,
        "refs_low": {"integer_cst": 142},
        "refs_name": {"label_decl": 154},
        "refs_type": {"void_type": 154},
        "type": 154,
    },
    "complex_type": {
        "attrs_addr": 60,
        "nid": 60,
        "refs_name": {"type_decl": 48},
        "refs_size": {"integer_cst": 60},
        "type": 60,
    },
    "component_ref": {
        "attrs_addr": 1302,
        "nid": 1302,
        "refs_OP0": {
            "array_ref": 64,
            "component_ref": 46,
            "indirect_ref": 1151,
            "var_decl": 41,
        },
        "refs_OP1": {"field_decl": 1302},
        "refs_type": {
            "array_type": 99,
            "integer_type": 666,
            "pointer_type": 478,
            "record_type": 36,
            "union_type": 23,
        },
        "type": 1302,
    },
    "compound_expr": {
        "attrs_addr": 109,
        "nid": 109,
        "refs_OP0": {"compound_expr": 3, "modify_expr": 105, "save_expr": 1},
        "refs_OP1": {
            "call_expr": 1,
            "integer_cst": 29,
            "le_expr": 62,
            "modify_expr": 15,
            "ne_expr": 1,
            "postincrement_expr": 1,
        },
        "refs_type": {"integer_type": 106, "pointer_type": 2, "void_type": 1},
        "type": 109,
    },
    "cond_expr": {
        "attrs_addr": 1754,
        "nid": 1754,
        "refs_OP0": {
            "compound_expr": 63,
            "eq_expr": 359,
            "ge_expr": 6,
            "gt_expr": 34,
            "integer_cst": 3,
            "le_expr": 67,
            "lt_expr": 55,
            "ne_expr": 633,
            "truth_and_expr": 192,
            "truth_andif_expr": 178,
            "truth_or_expr": 9,
            "truth_orif_expr": 155,
        },
        "refs_OP1": {
            "addr_expr ": 1,
            "bind_expr": 30,
            "call_expr": 128,
            "component_ref": 6,
            "cond_expr": 61,
            "convert_expr": 53,
            "goto_expr": 215,
            "indirect_ref": 1,
            "integer_cst": 13,
            "modify_expr": 233,
            "negate_expr": 61,
            "nop_expr": 62,
            "parm_decl": 9,
            "postincrement_expr": 4,
            "return_expr": 105,
            "statement_list": 766,
            "var_decl": 6,
        },
        "refs_OP2": {
            "call_expr": 76,
            "compound_expr": 1,
            "cond_expr": 48,
            "convert_expr": 3,
            "goto_expr": 180,
            "integer_cst": 21,
            "modify_expr": 71,
            "nop_expr": 101,
            "parm_decl": 23,
            "pointer_plus_expr": 1,
            "postincrement_expr": 1,
            "return_expr": 13,
            "statement_list": 58,
            "var_decl": 4,
        },
        "refs_type": {"integer_type": 170, "pointer_type": 55, "void_type": 1511},
        "type": 1754,
    },
    "const_decl": {
        "attrs_addr": 6323,
        "nid": 6358,
        "refs_chain": {"const_decl": 5907, "type_decl": 451},
        "refs_cnst": {"integer_cst": 6358},
        "refs_name": {"identifier_node": 6358},
        "refs_scpe": {"translation_unit_decl": 6358},
        "refs_type": {"enumeral_type": 6358},
        "type": 6358,
    },
    "constructor": {
        "attrs_addr": 55,
        "nid": 55,
        "refs_idx": {"field_decl": 50, "integer_cst": 5},
        "refs_val": {"constructor": 3, "integer_cst": 51, "nop_expr": 1},
        "type": 55,
    },
    "convert_expr": {
        "attrs_addr": 631,
        "nid": 631,
        "refs_OP0": {
            "call_expr": 444,
            "component_ref": 10,
            "indirect_ref": 4,
            "parm_decl": 79,
            "rshift_expr": 51,
            "var_decl": 43,
        },
        "refs_type": {"integer_type": 226, "void_type": 405},
        "type": 631,
    },
    "decl_expr": {
        "attrs_addr": 968,
        "nid": 968,
        "refs_type": {"void_type": 968},
        "type": 968,
    },
    "enumeral_type": {
        "attrs_addr": 484,
        "nid": 484,
        "refs_csts": {"tree_list": 484},
        "refs_max": {"integer_cst": 484},
        "refs_min": {"integer_cst": 484},
        "refs_name": {"identifier_node": 176, "type_decl": 33},
        "refs_size": {"integer_cst": 484},
        "refs_unql": {"enumeral_type": 33},
        "type": 484,
    },
    "eq_expr": {
        "attrs_addr": 861,
        "nid": 861,
        "refs_OP0": {
            "array_ref": 12,
            "bit_and_expr": 21,
            "call_expr": 22,
            "component_ref": 66,
            "indirect_ref": 328,
            "modify_expr": 128,
            "nop_expr": 4,
            "parm_decl": 33,
            "target_expr": 29,
            "var_decl": 218,
        },
        "refs_OP1": {
            "call_expr": 2,
            "component_ref": 4,
            "indirect_ref": 2,
            "integer_cst": 737,
            "nop_expr": 3,
            "parm_decl": 90,
            "var_decl": 23,
        },
        "refs_type": {"integer_type": 861},
        "type": 861,
    },
    "field_decl": {
        "attrs_addr": 9998,
        "nid": 9998,
        "refs_bpos": {"integer_cst": 9998},
        "refs_chain": {"field_decl": 7791},
        "refs_name": {"identifier_node": 9954},
        "refs_scpe": {"record_type": 9228, "union_type": 770},
        "refs_size": {"integer_cst": 9987},
        "refs_type": {
            "array_type": 938,
            "enumeral_type": 121,
            "integer_type": 5773,
            "pointer_type": 1996,
            "real_type": 11,
            "record_type": 928,
            "union_type": 231,
        },
        "type": 9998,
    },
    "function_decl": {
        "attrs_addr": 31565,
        "nid": 30940,
        "refs_args": {"parm_decl": 496},
        "refs_body": {"bind_expr": 525, "statement_list": 1},
        "refs_chain": {"function_decl": 31355, "type_decl": 36, "var_decl": 158},
        "refs_mngl": {"identifier_node": 6268},
        "refs_name": {"identifier_node": 31565},
        "refs_scpe": {"translation_unit_decl": 27321},
        "refs_type": {"function_type": 26936},
        "type": 31565,
    },
    "function_type": {
        "attrs_addr": 11503,
        "nid": 11503,
        "refs_name": {"type_decl": 44},
        "refs_prms": {"tree_list": 11365},
        "refs_retn": {
            "boolean_type": 240,
            "complex_type": 156,
            "enumeral_type": 33,
            "integer_type": 6172,
            "pointer_bounds_type": 24,
            "pointer_type": 2028,
            "real_type": 713,
            "record_type": 55,
            "union_type": 11,
            "vector_type": 696,
            "void_type": 1375,
        },
        "refs_size": {"integer_cst": 11503},
        "refs_unql": {"function_type": 118},
        "type": 11503,
    },
    "ge_expr": {
        "attrs_addr": 86,
        "nid": 86,
        "refs_OP0": {
            "component_ref": 69,
            "indirect_ref": 1,
            "modify_expr": 3,
            "parm_decl": 1,
            "preincrement_expr": 1,
            "var_decl": 11,
        },
        "refs_OP1": {
            "component_ref": 66,
            "integer_cst": 9,
            "parm_decl": 6,
            "var_decl": 5,
        },
        "refs_type": {"integer_type": 86},
        "type": 86,
    },
    "goto_expr": {
        "attrs_addr": 957,
        "nid": 957,
        "refs_labl": {"label_decl": 957},
        "refs_type": {"void_type": 957},
        "type": 957,
    },
    "gt_expr": {
        "attrs_addr": 59,
        "nid": 59,
        "refs_OP0": {
            "component_ref": 4,
            "modify_expr": 4,
            "nop_expr": 16,
            "plus_expr": 5,
            "pointer_plus_expr": 11,
            "var_decl": 19,
        },
        "refs_OP1": {
            "component_ref": 4,
            "integer_cst": 21,
            "nop_expr": 1,
            "plus_expr": 2,
            "pointer_plus_expr": 22,
            "var_decl": 9,
        },
        "refs_type": {"integer_type": 59},
        "type": 59,
    },
    "identifier_node": {"attrs_string": 54205, "nid": 54407, "type": 54407},
    "indirect_ref": {
        "attrs_addr": 2891,
        "nid": 2891,
        "refs_OP0": {
            "call_expr": 56,
            "component_ref": 3,
            "indirect_ref": 72,
            "nop_expr": 101,
            "parm_decl": 544,
            "pointer_plus_expr": 917,
            "postincrement_expr": 78,
            "preincrement_expr": 1,
            "var_decl": 1119,
        },
        "refs_type": {"integer_type": 1092, "pointer_type": 644, "record_type": 1155},
        "type": 2891,
    },
    "integer_cst": {
        "attrs_addr": 6403,
        "attrs_type": 3694,
        "attrs_type_name": 6403,
        "attrs_type_size": 6403,
        "nid": 6403,
        "refs_type": {"integer_type": 2653, "pointer_type": 56},
        "type": 6403,
    },
    "integer_type": {
        "attrs_addr": 2953,
        "nid": 2953,
        "refs_max": {"integer_cst": 2942},
        "refs_min": {"integer_cst": 2947},
        "refs_name": {"identifier_node": 24, "type_decl": 2392},
        "refs_size": {"integer_cst": 2943},
        "refs_unql": {"integer_type": 2236},
        "type": 2953,
    },
    "label_decl": {
        "attrs_addr": 771,
        "attrs_note": 771,
        "nid": 771,
        "refs_scpe": {"function_decl": 771},
        "refs_type": {"void_type": 771},
        "type": 771,
    },
    "label_expr": {
        "attrs_addr": 617,
        "nid": 617,
        "refs_name": {"label_decl": 617},
        "refs_type": {"void_type": 617},
        "type": 617,
    },
    "le_expr": {
        "attrs_addr": 136,
        "nid": 136,
        "refs_OP0": {
            "call_expr": 11,
            "component_ref": 13,
            "modify_expr": 8,
            "nop_expr": 1,
            "parm_decl": 1,
            "plus_expr": 23,
            "var_decl": 79,
        },
        "refs_OP1": {"integer_cst": 134, "parm_decl": 2},
        "refs_type": {"integer_type": 136},
        "type": 136,
    },
    "lshift_expr": {
        "attrs_addr": 70,
        "nid": 70,
        "refs_OP0": {
            "integer_cst": 33,
            "mult_expr": 1,
            "nop_expr": 22,
            "parm_decl": 11,
            "var_decl": 3,
        },
        "refs_OP1": {"bit_and_expr": 33, "integer_cst": 36, "trunc_mod_expr": 1},
        "refs_type": {"integer_type": 70},
        "type": 70,
    },
    "lt_expr": {
        "attrs_addr": 76,
        "nid": 76,
        "refs_OP0": {
            "call_expr": 4,
            "component_ref": 3,
            "modify_expr": 4,
            "plus_expr": 2,
            "var_decl": 63,
        },
        "refs_OP1": {
            "component_ref": 2,
            "cond_expr": 1,
            "integer_cst": 13,
            "parm_decl": 4,
            "var_decl": 56,
        },
        "refs_type": {"integer_type": 76},
        "type": 76,
    },
    "mem_ref": {"attrs_addr": 1, "nid": 1, "refs_type": {"record_type": 1}, "type": 1},
    "minus_expr": {
        "attrs_addr": 260,
        "nid": 260,
        "refs_OP0": {
            "convert_expr": 1,
            "indirect_ref": 1,
            "integer_cst": 5,
            "nop_expr": 248,
            "var_decl": 5,
        },
        "refs_OP1": {"convert_expr": 4, "nop_expr": 250, "parm_decl": 1, "var_decl": 5},
        "refs_type": {"integer_type": 260},
        "type": 260,
    },
    "modify_expr": {
        "attrs_addr": 2919,
        "nid": 2919,
        "refs_OP0": {
            "array_ref": 55,
            "component_ref": 294,
            "indirect_ref": 224,
            "parm_decl": 24,
            "result_decl": 616,
            "var_decl": 1706,
        },
        "refs_OP1": {
            "array_ref": 33,
            "bit_and_expr": 43,
            "bit_ior_expr": 100,
            "bit_xor_expr": 1,
            "call_expr": 418,
            "component_ref": 95,
            "compound_expr": 28,
            "cond_expr": 177,
            "convert_expr": 70,
            "eq_expr": 7,
            "indirect_ref": 72,
            "integer_cst": 821,
            "lshift_expr": 1,
            "minus_expr": 187,
            "modify_expr": 63,
            "mult_expr": 5,
            "ne_expr": 40,
            "nop_expr": 266,
            "parm_decl": 51,
            "plus_expr": 50,
            "pointer_plus_expr": 38,
            "postincrement_expr": 11,
            "preincrement_expr": 1,
            "target_expr": 1,
            "trunc_div_expr": 11,
            "truth_and_expr": 1,
            "truth_andif_expr": 8,
            "truth_orif_expr": 1,
            "var_decl": 319,
        },
        "refs_type": {
            "integer_type": 1905,
            "pointer_type": 859,
            "real_type": 11,
            "record_type": 6,
            "void_type": 138,
        },
        "type": 2919,
    },
    "mult_expr": {
        "attrs_addr": 203,
        "nid": 203,
        "refs_OP0": {
            "component_ref": 1,
            "nop_expr": 163,
            "parm_decl": 9,
            "var_decl": 30,
        },
        "refs_OP1": {"integer_cst": 191, "nop_expr": 1, "parm_decl": 11},
        "refs_type": {"integer_type": 203},
        "type": 203,
    },
    "ne_expr": {
        "attrs_addr": 1069,
        "nid": 1069,
        "refs_OP0": {
            "array_ref": 1,
            "bit_and_expr": 115,
            "bit_ior_expr": 4,
            "call_expr": 140,
            "component_ref": 134,
            "indirect_ref": 123,
            "modify_expr": 62,
            "nop_expr": 2,
            "parm_decl": 37,
            "target_expr": 46,
            "truth_and_expr": 1,
            "var_decl": 404,
        },
        "refs_OP1": {"integer_cst": 1056, "nop_expr": 4, "parm_decl": 1, "var_decl": 8},
        "refs_type": {"integer_type": 1069},
        "type": 1069,
    },
    "negate_expr": {
        "attrs_addr": 61,
        "nid": 61,
        "refs_OP0": {"target_expr": 61},
        "refs_type": {"integer_type": 61},
        "type": 61,
    },
    "nop_expr": {
        "attrs_addr": 3680,
        "nid": 3680,
        "refs_OP0": {
            "addr_expr ": 1300,
            "array_ref": 13,
            "bit_ior_expr": 11,
            "call_expr": 101,
            "component_ref": 189,
            "convert_expr": 35,
            "indirect_ref": 773,
            "minus_expr": 4,
            "modify_expr": 33,
            "mult_expr": 168,
            "nop_expr": 38,
            "parm_decl": 202,
            "plus_expr": 125,
            "pointer_plus_expr": 14,
            "postincrement_expr": 38,
            "preincrement_expr": 3,
            "target_expr": 1,
            "var_decl": 632,
        },
        "refs_type": {"integer_type": 1525, "pointer_type": 2155},
        "type": 3680,
    },
    "parm_decl": {
        "attrs_addr": 1004,
        "nid": 1004,
        "refs_argt": {"integer_type": 449, "pointer_type": 555},
        "refs_chain": {"parm_decl": 508},
        "refs_name": {"identifier_node": 1004},
        "refs_scpe": {"function_decl": 1004},
        "refs_size": {"integer_cst": 1004},
        "refs_type": {"integer_type": 449, "pointer_type": 555},
        "type": 1004,
    },
    "plus_expr": {
        "attrs_addr": 291,
        "nid": 291,
        "refs_OP0": {
            "array_ref": 4,
            "call_expr": 4,
            "component_ref": 5,
            "cond_expr": 2,
            "convert_expr": 23,
            "lshift_expr": 2,
            "minus_expr": 2,
            "mult_expr": 6,
            "nop_expr": 66,
            "parm_decl": 70,
            "plus_expr": 15,
            "var_decl": 92,
        },
        "refs_OP1": {
            "convert_expr": 2,
            "integer_cst": 243,
            "nop_expr": 3,
            "parm_decl": 1,
            "plus_expr": 5,
            "var_decl": 37,
        },
        "refs_type": {"integer_type": 291},
        "type": 291,
    },
    "pointer_bounds_type": {
        "attrs_addr": 12,
        "nid": 12,
        "refs_name": {"identifier_node": 12},
        "refs_size": {"integer_cst": 12},
        "type": 12,
    },
    "pointer_plus_expr": {
        "attrs_addr": 1008,
        "nid": 1008,
        "refs_OP0": {
            "component_ref": 4,
            "indirect_ref": 42,
            "nop_expr": 216,
            "parm_decl": 66,
            "var_decl": 680,
        },
        "refs_OP1": {
            "bit_and_expr": 22,
            "integer_cst": 750,
            "nop_expr": 225,
            "plus_expr": 11,
        },
        "refs_type": {"pointer_type": 1008},
        "type": 1008,
    },
    "pointer_type": {
        "attrs_addr": 4503,
        "nid": 4503,
        "refs_name": {"type_decl": 249},
        "refs_ptd": {
            "array_type": 237,
            "function_type": 1144,
            "integer_type": 735,
            "pointer_type": 403,
            "real_type": 71,
            "record_type": 1750,
            "union_type": 22,
            "vector_type": 36,
            "void_type": 105,
        },
        "refs_size": {"integer_cst": 4503},
        "refs_unql": {"pointer_type": 994},
        "type": 4503,
    },
    "postdecrement_expr": {
        "attrs_addr": 2,
        "nid": 2,
        "refs_OP0": {"var_decl": 2},
        "refs_OP1": {"integer_cst": 2},
        "refs_type": {"integer_type": 2},
        "type": 2,
    },
    "postincrement_expr": {
        "attrs_addr": 244,
        "nid": 244,
        "refs_OP0": {
            "component_ref": 66,
            "indirect_ref": 11,
            "parm_decl": 25,
            "var_decl": 142,
        },
        "refs_OP1": {"integer_cst": 244},
        "refs_type": {"integer_type": 97, "pointer_type": 147},
        "type": 244,
    },
    "predict_expr": {
        "attrs_addr": 135,
        "nid": 135,
        "refs_type": {"void_type": 135},
        "type": 135,
    },
    "preincrement_expr": {
        "attrs_addr": 39,
        "nid": 39,
        "refs_OP0": {"parm_decl": 11, "var_decl": 28},
        "refs_OP1": {"integer_cst": 39},
        "refs_type": {"integer_type": 4, "pointer_type": 35},
        "type": 39,
    },
    "real_type": {
        "attrs_addr": 108,
        "nid": 108,
        "refs_name": {"type_decl": 108},
        "refs_size": {"integer_cst": 108},
        "refs_unql": {"real_type": 24},
        "type": 108,
    },
    "record_type": {
        "attrs_addr": 2654,
        "nid": 2654,
        "refs_flds": {"field_decl": 2575},
        "refs_name": {"identifier_node": 1759, "type_decl": 498},
        "refs_size": {"integer_cst": 2575},
        "refs_unql": {"record_type": 676},
        "type": 2654,
    },
    "reference_type": {
        "attrs_addr": 12,
        "nid": 12,
        "refs_refd": {"pointer_type": 12},
        "refs_size": {"integer_cst": 12},
        "type": 12,
    },
    "result_decl": {
        "attrs_addr": 494,
        "attrs_note": 494,
        "nid": 494,
        "refs_scpe": {"function_decl": 494},
        "refs_size": {"integer_cst": 494},
        "refs_type": {"integer_type": 400, "pointer_type": 83, "real_type": 11},
        "type": 494,
    },
    "return_expr": {
        "attrs_addr": 648,
        "nid": 648,
        "refs_expr": {"modify_expr": 616},
        "refs_type": {"void_type": 648},
        "type": 648,
    },
    "rshift_expr": {
        "attrs_addr": 54,
        "nid": 54,
        "refs_OP0": {"mult_expr": 20, "parm_decl": 33, "var_decl": 1},
        "refs_OP1": {"integer_cst": 54},
        "refs_type": {"integer_type": 54},
        "type": 54,
    },
    "save_expr": {
        "attrs_addr": 1,
        "nid": 1,
        "refs_OP0": {"truth_andif_expr": 1},
        "refs_type": {"integer_type": 1},
        "type": 1,
    },
    "statement_list": {
        "attrs_addr": 1176,
        "nid": 1176,
        "refs_E": {
            "bind_expr": 63,
            "call_expr": 223,
            "case_label_expr": 154,
            "compound_expr": 14,
            "cond_expr": 1358,
            "convert_expr": 347,
            "decl_expr": 968,
            "goto_expr": 562,
            "label_expr": 617,
            "modify_expr": 1572,
            "postdecrement_expr": 2,
            "postincrement_expr": 111,
            "predict_expr": 135,
            "preincrement_expr": 33,
            "return_expr": 177,
            "switch_expr": 14,
        },
        "type": 1176,
    },
    "string_cst": {
        "attrs_string": 1062,
        "nid": 1062,
        "refs_type": {"array_type": 1062},
        "type": 1062,
    },
    "switch_expr": {
        "attrs_addr": 14,
        "nid": 14,
        "refs_body": {"statement_list": 14},
        "refs_cond": {"component_ref": 5, "nop_expr": 3, "parm_decl": 1, "var_decl": 5},
        "refs_type": {"integer_type": 14},
        "type": 14,
    },
    "target_expr": {
        "attrs_addr": 138,
        "nid": 138,
        "refs_decl": {"var_decl": 138},
        "refs_init": {"bind_expr": 138},
        "refs_type": {"integer_type": 138},
        "type": 138,
    },
    "translation_unit_decl": {"attrs_addr": 12, "nid": 12, "type": 12},
    "tree_list": {
        "attrs_addr": 32640,
        "nid": 32640,
        "refs_chan": {"tree_list": 31716},
        "refs_purp": {"identifier_node": 6358},
        "refs_valu": {
            "boolean_type": 60,
            "complex_type": 144,
            "enumeral_type": 99,
            "integer_cst": 6300,
            "integer_type": 9682,
            "pointer_bounds_type": 36,
            "pointer_type": 13803,
            "real_type": 1062,
            "record_type": 55,
            "reference_type": 36,
            "union_type": 33,
            "vector_type": 1260,
            "void_type": 12,
        },
        "type": 32640,
    },
    "trunc_div_expr": {
        "attrs_addr": 44,
        "nid": 44,
        "refs_OP0": {"nop_expr": 33, "plus_expr": 11},
        "refs_OP1": {"integer_cst": 44},
        "refs_type": {"integer_type": 44},
        "type": 44,
    },
    "trunc_mod_expr": {
        "attrs_addr": 2,
        "nid": 2,
        "refs_OP0": {"mult_expr": 1, "parm_decl": 1},
        "refs_OP1": {"integer_cst": 2},
        "refs_type": {"integer_type": 2},
        "type": 2,
    },
    "truth_and_expr": {
        "attrs_addr": 198,
        "nid": 198,
        "refs_type": {"integer_type": 198},
        "type": 198,
    },
    "truth_andif_expr": {
        "attrs_addr": 231,
        "nid": 231,
        "refs_OP0": {
            "eq_expr": 37,
            "ge_expr": 8,
            "gt_expr": 2,
            "le_expr": 2,
            "lt_expr": 6,
            "ne_expr": 138,
            "truth_andif_expr": 38,
        },
        "refs_OP1": {
            "eq_expr": 76,
            "ge_expr": 3,
            "gt_expr": 1,
            "le_expr": 2,
            "lt_expr": 14,
            "ne_expr": 131,
            "truth_and_expr": 1,
            "truth_or_expr": 1,
            "truth_orif_expr": 2,
        },
        "refs_type": {"integer_type": 231},
        "type": 231,
    },
    "truth_or_expr": {
        "attrs_addr": 13,
        "nid": 13,
        "refs_type": {"integer_type": 13},
        "type": 13,
    },
    "truth_orif_expr": {
        "attrs_addr": 387,
        "nid": 387,
        "refs_OP0": {
            "eq_expr": 120,
            "ge_expr": 1,
            "gt_expr": 11,
            "le_expr": 2,
            "lt_expr": 1,
            "ne_expr": 20,
            "truth_andif_expr": 2,
            "truth_or_expr": 1,
            "truth_orif_expr": 229,
        },
        "refs_OP1": {
            "eq_expr": 260,
            "ge_expr": 2,
            "gt_expr": 11,
            "le_expr": 1,
            "ne_expr": 105,
            "truth_and_expr": 3,
            "truth_andif_expr": 4,
            "truth_or_expr": 1,
        },
        "refs_type": {"integer_type": 387},
        "type": 387,
    },
    "type_decl": {
        "attrs_addr": 6251,
        "attrs_note": 24,
        "nid": 6251,
        "refs_chain": {
            "const_decl": 451,
            "function_decl": 51,
            "type_decl": 5704,
            "var_decl": 16,
        },
        "refs_name": {"identifier_node": 3417},
        "refs_scpe": {"function_decl": 1, "translation_unit_decl": 5722},
        "refs_type": {
            "array_type": 90,
            "boolean_type": 12,
            "complex_type": 60,
            "enumeral_type": 484,
            "function_type": 44,
            "integer_type": 2410,
            "pointer_type": 227,
            "real_type": 96,
            "record_type": 2387,
            "union_type": 418,
            "void_type": 23,
        },
        "type": 6251,
    },
    "union_type": {
        "attrs_addr": 430,
        "nid": 430,
        "refs_flds": {"field_decl": 430},
        "refs_name": {"identifier_node": 55, "type_decl": 121},
        "refs_size": {"integer_cst": 430},
        "refs_unql": {"union_type": 133},
        "type": 430,
    },
    "var_decl": {
        "attrs_addr": 3110,
        "attrs_note": 138,
        "nid": 3110,
        "refs_chain": {"function_decl": 159, "type_decl": 12, "var_decl": 2477},
        "refs_init": {
            "constructor": 5,
            "indirect_ref": 33,
            "integer_cst": 245,
            "lshift_expr": 33,
            "minus_expr": 61,
            "nop_expr": 69,
            "trunc_div_expr": 33,
            "var_decl": 22,
        },
        "refs_name": {"identifier_node": 2972},
        "refs_scpe": {"function_decl": 968, "translation_unit_decl": 2004},
        "refs_size": {"integer_cst": 3036},
        "refs_type": {
            "array_type": 103,
            "integer_type": 1999,
            "pointer_type": 894,
            "record_type": 114,
        },
        "type": 3110,
    },
    "vector_type": {
        "attrs_addr": 144,
        "nid": 144,
        "refs_size": {"integer_cst": 144},
        "refs_unql": {"vector_type": 12},
        "type": 144,
    },
    "void_type": {
        "attrs_addr": 59,
        "nid": 59,
        "refs_name": {"type_decl": 59},
        "refs_unql": {"void_type": 47},
        "type": 59,
    },
}


def report():
    type2 = {}
    for t in list(d.keys()):
        # print t
        dl = t.split("_")
        t2 = dl[-1]
        # print t,t2
        if t2 in type2:
            dv = d[t]
            dv2 = type2[t2]
            for f in dv:
                # print (f)

                if f in dv2:
                    if f.startswith("refs"):
                        for t3 in dv[f]:
                            v3 = dv[f][t3]
                            dl2 = t3.split("_")
                            t4 = dl2[-1]
                            if t4 in dv2[f]:
                                dv2[f][t4] = dv2[f][t4] + v3
                            else:
                                dv2[f][t4] = v3

                    else:
                        # print (f)
                        dv2[f] = dv2[f] + dv[f]
                else:
                    if f.startswith("refs"):
                        dv2[f] = {}
                        for t3 in dv[f]:
                            v3 = dv[f][t3]
                            dl2 = t3.split("_")
                            t4 = dl2[-1]
                            # print t4
                            if t4 in dv2[f]:
                                dv2[f][t4] = dv2[f][t4] + v3
                            else:
                                dv2[f][t4] = v3

                    else:
                        # print(f)
                        # pprint.pprint(dv[f])
                        # pprint.pprint(dv2[f])
                        dv2[f] = dv[f]
                    # =dv[f]
        else:
            type2[t2] = {}
            dv = d[t]
            dv2 = type2[t2]
            for f in dv:
                if f.startswith("refs"):
                    dv2[f] = {}
                    for t3 in dv[f]:
                        v3 = dv[f][t3]
                        dl2 = t3.split("_")
                        t4 = dl2[-1]
                        # print t4
                        if t4 in dv2[f]:
                            dv2[f][t4] = dv2[f][t4] + v3
                        else:
                            dv2[f][t4] = v3

                else:
                    # print(f)
                    # pprint.pprint(dv[f])
                    # pprint.pprint(dv2[f])
                    dv2[f] = dv[f]

    pprint.pprint(type2)


mysizes = {
    "addr": 12,
    "nid": 5,
    "note": 4,
    "string": 228,
    "type": 21,
    "type_name": 3,
    "type_size": 35,
}


def report2():
    type2 = {}
    for t in list(d.keys()):
        t2 = "all"
        dv = d[t]
        if t2 in type2:
            dv2 = type2[t2]
            for f in dv:
                if f.startswith("refs"):
                    dv2[f] = "ref"
                else:
                    dv2[f] = "scalar"
        else:
            type2[t2] = {}
            dv2 = type2[t2]
            for f in dv:
                if f.startswith("refs"):
                    dv2[f] = "ref"
                else:
                    dv2[f] = "ref"

    # pprint.pprint(type2)
    print("from django.db import models")
    print("class Node(models.Model):")
    print("source_file= models.ForeignKey(SourceFile)")
    print("nid= models.IntegerField()")
    print("class Meta:\n    unique_together = (('source_file', 'node_id'),)")

    for f in type2:
        for f2 in type2[f]:
            v = type2[f][f2]
            s = 5
            if f2.startswith("attrs_"):
                f1 = f2.replace("attrs_", "")
                s = mysizes[f1]
                print("    %s = models.CharField(max_length=%d)" % (f2, s))
            else:
                print("    %s = models.IntegerField()" % (f2))


report2()
