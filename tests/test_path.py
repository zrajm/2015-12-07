
import os, pytest
from program import conform


@pytest.fixture(scope='session')
def done_conform(request):
    path = conform()

    def delete_file():
        os.remove(path)

    request.addfinalizer(delete_file)

    return path


################################################################################

def test_path(done_conform):
    path = done_conform
    assert path == '/tmp/file.mxf'

def test_file_exist(done_conform):
    path = done_conform
    assert os.path.isfile(path)

def test_file_is_mxf(done_conform):
    path = done_conform
    with open(path, 'rb') as f:
        head = f.read(14)
        assert head == '\x06\x0e\x2b\x34\x02\x05\x01\x01\x0d\x01\x02\x01\x01\x02'
