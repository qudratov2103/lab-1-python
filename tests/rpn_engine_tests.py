import pytest
from src.rpn_engine import ReversePolishMachine

def test_basic_operations():
    calc = ReversePolishMachine()
    assert calc.calculate("3 4 +") == 7
    assert calc.calculate("10 5 -") == 5
    assert calc.calculate("3 4 *") == 12
    assert calc.calculate("10 2 /") == 5

def test_with_parentheses():
    calc = ReversePolishMachine()
    assert calc.calculate("( 3 4 + )") == 7
    assert calc.calculate("( 3 4 + ) ( 5 2 - ) *") == 21

def test_power():
    calc = ReversePolishMachine()
    assert calc.calculate("2 3 **") == 8

def test_floor_division():
    calc = ReversePolishMachine()
    assert calc.calculate("7 2 //") == 3

def test_modulo():
    calc = ReversePolishMachine()
    assert calc.calculate("7 3 %") == 1

def test_unary_operators():
    calc = ReversePolishMachine()
    assert calc.calculate("5 u+") == 5
    assert calc.calculate("5 u-") == -5
    assert calc.calculate("3 4 +") == 7   
    assert calc.calculate("3 4 -") == -1  

def test_complex_expressions():
    calc = ReversePolishMachine()
    assert calc.calculate("3 4 2 * +") == 11
    assert calc.calculate("3.5 2.5 +") == 6.0

def test_errors():
    calc = ReversePolishMachine()
    
    with pytest.raises(ValueError):
        calc.calculate("5 0 /")
    
    with pytest.raises(ValueError):
        calc.calculate("3 4 неизвестно +")
    
    with pytest.raises(ValueError):
        calc.calculate("3 +")