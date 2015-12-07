
import pytest
from core.conform import read_edl_template

@pytest.fixture(scope='session')
def edl_template(request):
    xml = read_edl_template()
    return xml

def test_edl_xmlishness(edl_template):
    xml = edl_template
    assert xml[:5] == '<?xml'

def test_source_placeholder(edl_template):
    xml = edl_template
    assert '{{source_file}}' in xml

def test_dest_placeholder(edl_template):
    xml = edl_template
    assert '{{dest_file}}' in xml
