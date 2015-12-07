
from program import conform
import os

def test_path():
    path = conform()
    assert path == '/tmp/file.mxf'
    assert os.path.isfile(path)
