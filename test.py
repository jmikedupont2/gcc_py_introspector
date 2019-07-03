#!/usr/bin/python3
# PYTHONPATH=~/experiments/gcc_py_introspector/ python3
# import memory_profiler
# tests/identifier.tu
import sys

import gcc.tree.attributes
import gcc.tree.nodes
import gcc.tree.reader

gcc.tree.reader.main()
gcc.tree.attributes.report()
gcc.tree.nodes.report()
