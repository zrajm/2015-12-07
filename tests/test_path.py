
import os, pytest
from program import conform


@pytest.fixture(scope='session')
def done_conform():
    return conform()

def test_path(done_conform):
    path = done_conform
    assert path == '/tmp/file.mxf'
    assert os.path.isfile(path)

def test_fileinfo(done_conform):
    path = done_conform
    with open(path, 'rb') as f:
        head = f.read(14)
        print head
        assert head == '\x06\x0e\x2b\x34\x02\x05\x01\x01\x0d\x01\x02\x01\x01\x02'
