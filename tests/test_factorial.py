import pytest
from mymath.factorial import factorial


def test_1():
    assert factorial(1) == 1

def test_2():
    assert factorial(2) == 2

def test_3():
    assert factorial(3) == 6

def test_5():
    assert factorial(5) == 120

def test_10():
    assert factorial(10) == 3628800
"""
def test_float():
    with pytest.raises(ValueError):
      factorial(1.50)
"""
def test_negative():
    with pytest.raises(ValueError):
      factorial(-1)
