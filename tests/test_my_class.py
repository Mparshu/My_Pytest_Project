import pytest
from my_project.my_class import MyClass

def test_my_class():
    obj = MyClass(42)
    assert obj.get_value() == 42