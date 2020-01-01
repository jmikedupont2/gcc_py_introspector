gcc_py_introspector
===================

a new stab at .tu parsing in my new favorite language, python


usage
=====

    g++ --verbose -O0 -fdump-tree-all  test.c

convert the tu to python:

    python3.7  -m  gcc.tree.gcc-tu-reader  file.tu  > file.json

now you can split up the output:

    jq -s "{nodes :.}" test_graph.json  > test_graph_jq.json
    
    splitter.py test_graph_jq.json


