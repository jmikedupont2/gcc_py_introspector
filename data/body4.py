#!/usr/bin/python
from .body3 import *

function_decl(
    link="extern",
    srcp="eval.c:216",
    body=bind_expr(
        body=statement_list(
            E0=decl_expr(ftype=void_type(algn="8", name="126")),
            E1=decl_expr(ftype=void_type(algn="8", name="126")),
            E2=modify_expr(
                OP0=var_decl(
                    algn="32",
                    srcp="eval.c:53",
                    used="1",
                    name=identifier_node(string="need_here_doc"),
                ),
                OP1=integer_cst(
                    low="0",
                    ftype=integer_type(
                        algn="32",
                        max="7",
                        min="6",
                        name="1",
                        prec="32",
                        sign="signed",
                        size="5",
                    ),
                ),
            ),
            E3=call_expr(
                fn=addr_expr(OP0=pointer_type(algn="64")),
                ftype=void_type(algn="8", name="126"),
            ),
            E4=cond_expr(
                OP0=truth_andif_expr(
                    OP0=ne_expr(
                        OP0=var_decl(
                            algn="32",
                            srcp="shell.h:94",
                            used="1",
                            name=identifier_node(string="interactive"),
                        ),
                        OP1=integer_cst(
                            low="0",
                            ftype=integer_type(
                                algn="32",
                                max="7",
                                min="6",
                                name="1",
                                prec="32",
                                sign="signed",
                                size="5",
                            ),
                        ),
                    ),
                    OP1=ne_expr(
                        OP0=nop_expr(
                            OP0=component_ref(
                                OP0=var_decl(
                                    algn="64",
                                    srcp="input.h:89",
                                    used="1",
                                    name=identifier_node(string="bash_input"),
                                ),
                                OP1=field_decl(
                                    algn="32",
                                    srcp="input.h:82",
                                    name=identifier_node(string="type"),
                                ),
                            ),
                            ftype=integer_type(
                                algn="32",
                                max="29",
                                min="28",
                                name="17",
                                prec="32",
                                sign="unsigned",
                                size="5",
                            ),
                        ),
                        OP1=integer_cst(
                            low="3",
                            ftype=integer_type(
                                algn="32",
                                max="29",
                                min="28",
                                name="17",
                                prec="32",
                                sign="unsigned",
                                size="5",
                            ),
                        ),
                    ),
                ),
                OP1=statement_list(
                    E0=modify_expr(
                        OP0=var_decl(
                            algn="64",
                            srcp="eval.c:219",
                            used="1",
                            name=identifier_node(string="command_to_execute"),
                        ),
                        OP1=call_expr(
                            E0=nop_expr(
                                OP0=addr_expr(
                                    OP0=pointer_type(algn="64"),
                                    ftype=string_cst(
                                        string="PROMPT_COMMAND",
                                        ftype=array_type(
                                            algn="8",
                                            domn="13067",
                                            elts="9",
                                            size="13066",
                                        ),
                                    ),
                                ),
                                ftype=pointer_type(algn="64", ptd="906", size="22"),
                            ),
                            fn=addr_expr(OP0=pointer_type(algn="64")),
                            ftype=pointer_type(algn="64", ptd="9", size="22"),
                        ),
                        ftype=pointer_type(algn="64", ptd="9", size="22"),
                    ),
                    E1=cond_expr(
                        OP0=ne_expr(
                            OP0=var_decl(
                                algn="64",
                                srcp="eval.c:219",
                                used="1",
                                name=identifier_node(string="command_to_execute"),
                            ),
                            OP1=integer_cst(
                                low="0",
                                ftype=pointer_type(algn="64", ptd="9", size="22"),
                            ),
                            ftype=integer_type(
                                algn="32",
                                max="7",
                                min="6",
                                name="1",
                                prec="32",
                                sign="signed",
                                size="5",
                            ),
                        ),
                        OP1=call_expr(
                            E0=var_decl(
                                algn="64",
                                srcp="eval.c:219",
                                used="1",
                                name=identifier_node(string="command_to_execute"),
                            ),
                            E1=nop_expr(
                                OP0=addr_expr(
                                    OP0=pointer_type(algn="64"),
                                    ftype=string_cst(
                                        string="PROMPT_COMMAND",
                                        ftype=array_type(
                                            algn="8",
                                            domn="13067",
                                            elts="9",
                                            size="13066",
                                        ),
                                    ),
                                ),
                                ftype=pointer_type(algn="64", ptd="9", size="22"),
                            ),
                            fn=addr_expr(
                                OP0=pointer_type(algn="64"),
                                ftype=function_decl(
                                    body="undefined",
                                    ftype="10721",
                                    link="extern",
                                    name="10720",
                                    srcp="input.h:105",
                                ),
                            ),
                            ftype=void_type(algn="8", name="126"),
                        ),
                        ftype=void_type(algn="8", name="126"),
                    ),
                    E2=cond_expr(
                        OP0=eq_expr(
                            OP0=var_decl(
                                algn="32",
                                srcp="eval.c:51",
                                used="1",
                                name=identifier_node(string="running_under_emacs"),
                            ),
                            OP1=integer_cst(
                                low="2",
                                ftype=integer_type(
                                    algn="32",
                                    max="7",
                                    min="6",
                                    name="1",
                                    prec="32",
                                    sign="signed",
                                    size="5",
                                ),
                            ),
                        ),
                        OP1=call_expr(
                            fn=addr_expr(OP0=pointer_type(algn="64")),
                            ftype=void_type(algn="8", name="126"),
                        ),
                        ftype=void_type(algn="8", name="126"),
                    ),
                ),
                ftype=void_type(algn="8", name="126"),
            ),
            E5=modify_expr(
                OP0=var_decl(
                    algn="32",
                    srcp="eval.c:54",
                    used="1",
                    name=identifier_node(string="current_command_line_count"),
                ),
                OP1=integer_cst(
                    low="0",
                    ftype=integer_type(
                        algn="32",
                        max="7",
                        min="6",
                        name="1",
                        prec="32",
                        sign="signed",
                        size="5",
                    ),
                ),
            ),
            E6=modify_expr(
                OP0=var_decl(
                    algn="32",
                    srcp="eval.c:218",
                    used="1",
                    name=identifier_node(string="r"),
                ),
                OP1=call_expr(
                    fn=addr_expr(
                        OP0=pointer_type(algn="64"),
                        ftype=function_decl(
                            body="undefined",
                            ftype="2560",
                            link="extern",
                            name="12695",
                            srcp="externs.h:104",
                        ),
                    ),
                    ftype=integer_type(
                        algn="32",
                        max="7",
                        min="6",
                        name="1",
                        prec="32",
                        sign="signed",
                        size="5",
                    ),
                ),
                ftype=integer_type(
                    algn="32",
                    max="7",
                    min="6",
                    name="1",
                    prec="32",
                    sign="signed",
                    size="5",
                ),
            ),
            E7=cond_expr(
                OP0=ne_expr(
                    OP0=var_decl(
                        algn="32",
                        srcp="eval.c:53",
                        used="1",
                        name=identifier_node(string="need_here_doc"),
                    ),
                    OP1=integer_cst(
                        low="0",
                        ftype=integer_type(
                            algn="32",
                            max="7",
                            min="6",
                            name="1",
                            prec="32",
                            sign="signed",
                            size="5",
                        ),
                    ),
                ),
                OP1=call_expr(
                    fn=addr_expr(
                        OP0=pointer_type(algn="64"),
                        ftype=function_decl(
                            body="undefined",
                            ftype="5191",
                            link="extern",
                            name="10700",
                            srcp="input.h:104",
                        ),
                    ),
                    ftype=void_type(algn="8", name="126"),
                ),
                ftype=void_type(algn="8", name="126"),
            ),
            E8=return_expr(
                expr=modify_expr(
                    OP0=result_decl(
                        algn="32", note="art:artificial", srcp="eval.c:216"
                    ),
                    OP1=var_decl(
                        algn="32",
                        srcp="eval.c:218",
                        used="1",
                        name=identifier_node(string="r"),
                    ),
                    ftype=integer_type(
                        algn="32",
                        max="7",
                        min="6",
                        name="1",
                        prec="32",
                        sign="signed",
                        size="5",
                    ),
                ),
                ftype=void_type(algn="8", name="126"),
            ),
        ),
        ftype=void_type(algn="8", name="126"),
        vars=var_decl(
            algn="32", srcp="eval.c:218", used="1", name=identifier_node(string="r")
        ),
    ),
    name=identifier_node(string="parse_command"),
)
