import os
import glob
import pytest
import gcc.tree
import gcc.tree.reader

def get_file_list():
    files = []

    for path in ('*.tu','../test2/*.tu'):
        source = os.path.join(os.path.dirname(__file__), '*.tu')
        for fname in glob.glob(source):
            files.append(fname)

    return files

FILES = get_file_list()

print (FILES)
@pytest.mark.parametrize('filename', FILES)
def test_parse(filename):
    print ('test' + str(filename))
    gcc.tree.reader.parse(filename,False)
