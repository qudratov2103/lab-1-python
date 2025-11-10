import pytest
from src.rpn_engine import ReversePolishMachine

def test_with_parentheses():
    calc = ReversePolishMachine()
    assert calc.calculate("( 3 4 + )") == 7
    assert calc.calculate("( 3 4 + ) ( 5 2 - ) *") == 21
    assert calc.calculate("( 8 ( 3 2 + ) - ) 4 *") == 12

def test_basic_sum():
    calc = ReversePolishMachine()
    assert calc.calculate("3 4 +") == 7

def test_complex_expression():
    calc = ReversePolishMachine() 
    assert calc.calculate("3 4 2 * +") == 11

def test_division_operation():
    calc = ReversePolishMachine()
    assert calc.calculate("10 2 /") == 5

def test_power_calculation():
    calc = ReversePolishMachine()
    assert calc.calculate("2 3 **") == 8

def test_decimal_numbers():
    calc = ReversePolishMachine()
    assert calc.calculate("3.5 2.5 +") == 6.0

def test_missing_operands():
    calc = ReversePolishMachine()
    with pytest.raises(ValueError):
        calc.calculate("3 +")

def test_zero_division():
    calc = ReversePolishMachine()
    with pytest.raises(ValueError):
        calc.calculate("5 0 /")

def test_wrong_symbol():
    calc = ReversePolishMachine()
    with pytest.raises(ValueError):
        calc.calculate("3 4 неизвестно +")