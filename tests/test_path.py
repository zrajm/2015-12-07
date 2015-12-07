
import os, pytest, subprocess
from program import conform


@pytest.fixture(scope='session')
def done_conform(request):
    path = conform(u'/tmp/file.mp4')

    def delete_file():
        os.remove(path)

    request.addfinalizer(delete_file)

    return path


################################################################################

def test_path(done_conform):
    path = done_conform
    assert path == '/tmp/file.mp4'

def test_file_exist(done_conform):
    path = done_conform
    assert os.path.isfile(path)

def test_file_is_mp4(done_conform):
    path = done_conform
    process = subprocess.Popen(
        ['file', '--mime', path],
        stdout=subprocess.PIPE,
    )
    mime_type = process.stdout.readlines()[0]
    assert mime_type == path + ': video/mp4; charset=binary\n'


