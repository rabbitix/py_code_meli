from py_code_meli import __version__
from py_code_meli import is_valid
def test_version():
    assert __version__ == '0.1.0'



def test_true_code_meli():
    """in this test, the code "0095017240" considered a true codemeli.

    this code meli generatged with http://mellicode.azmads.com/Home/Index?id=0
    """
    code = "0095017240" #
    assert is_valid(code)
    
def test_false_code_meli():
    code = "0095017245" #0->5
    assert not is_valid(code)

    
def test_len():
    code = "009501724" #len is 9

    assert not is_valid(code)