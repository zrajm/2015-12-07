
import pytest
from core.conform import read_edl_template, render_edl

@pytest.fixture(scope='session')
def edl_template(request):
    xml = read_edl_template()
    return xml


@pytest.fixture(scope='session')
def edl(request, edl_template):
    return render_edl(
        edl_template,
        source_file = 'example2.mp4',
        dest_file = '/tmp/file.mp4',
    )

################################################################################

def test_edl_xmlishness(edl_template):
    xml = edl_template
    assert xml[:5] == '<?xml'

def test_source_placeholder(edl_template):
    xml = edl_template
    assert '{{source_file}}' in xml

def test_dest_placeholder(edl_template):
    xml = edl_template
    assert '{{dest_file}}' in xml

def test_source_filename(edl):
    xml = edl_template
    assert '<filename>example2.mp4</filename>' in xml

def test_dest_filename(edl):
    xml = edl_template
    assert '<filename>/tmp/file.mp4</filename>' in xml
