import pytest
import mod1

def test_fuel_conversions():
    assert list(mod1.get_fuel(12)) == [2]
    assert list(mod1.get_fuel(14)) == [2]
    assert list(mod1.get_fuel(1969)) == [654]
    assert list(mod1.get_fuel(100756)) == [33583]

def test_fuel_conversions_recursive():
    assert list(mod1.get_fuel(12, True)) == [2]
    assert list(mod1.get_fuel(14, True)) == [2]
    assert list(mod1.get_fuel(1969, True)) == [654, 216, 70, 21, 5]
    assert list(mod1.get_fuel(100756, True)) == [33583, 11192, 3728, 1240, 411, 135, 43, 12, 2]

def test_multiple_fuel_conversion():
    assert mod1.get_fuel_list([12, 14, 1969, 100756]) == [2, 2, 654, 33583]

def test_multiple_fuel_conversion_recursive():
    assert mod1.get_fuel_list([12, 14, 1969, 100756], True) == [2, 2, 654, 216, 70, 21, 5, 33583, 11192, 3728, 1240, 411, 135, 43, 12, 2]