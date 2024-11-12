import pytest
from my_project.my_module import add, multiply

def test_add():
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1