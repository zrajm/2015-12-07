
import os, pytest
from core.conform import run_dvstory

source_file = ''
dest_file   = ''

@pytest.fixture(scope='session')
def done_dvstory(request):
    return run_dvstory(source_file, dest_file)

################################################################################

def test_source_file_exist(done_dvstory):
    assert os.path.isfile(source_file)

def test_dest_file_exist(done_dvstory):
    assert os.path.isfile(dest_file)
