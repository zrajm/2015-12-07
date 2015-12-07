
import os, pytest
from core.conform import run_dvstory

source_file = 'example2.mp4'
dest_file   = '/tmp/file.mp4'

@pytest.fixture(scope='module')
def done_dvstory(request):

    def delete_file():
        os.remove(dest_file)

    request.addfinalizer(delete_file)

    return run_dvstory(source_file, dest_file)

################################################################################

def test_source_file_exist(done_dvstory):
    assert os.path.isfile(source_file)

def test_dest_file_exist(done_dvstory):
    assert os.path.isfile(dest_file)
