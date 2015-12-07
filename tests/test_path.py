
from program import conform


def test_path():
    path = conform()
    assert path == '/tmp/file.mxf'
    
