
from program import conform
import os

def test_path():
    path = conform()
    assert path == '/tmp/file.mxf'
    assert os.path.isfile(path)

def test_fileinfo():
    path = conform()
    with open(path, 'rb') as f:
        head = f.read(14)
        print head
        assert head == '\x06\x0e\x2b\x34\x02\x05\x01\x01\x0d\x01\x02\x01\x01\x02'
