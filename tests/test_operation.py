from src.math_operation import add, substract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_substract():
    assert substract(5, 3) == 2
    assert substract(0, 0) == 0
