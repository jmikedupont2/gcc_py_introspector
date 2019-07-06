gcc_py_introspector
===================

a new stab at .tu parsing in my new favorite language, python


usage
=====

    g++ --verbose -O0 -fdump-tree-all  test.c

convert the tu to python:

    gcc/tree/reader.py  file.tu > test_graph.json

now you can split up the output:

    jq -s "{nodes :.}" test_graph.json  > test_graph_jq.json
    
    splitter.py test_graph_jq.json


