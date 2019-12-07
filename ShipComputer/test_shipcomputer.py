import pytest
from .shipcomputer import ShipComputer


def test_computer_1():
    computer = ShipComputer([1, 0, 0, 0, 99])
    assert computer.runprogram()['itr'] == [2, 0, 0, 0, 99]


def test_computer_2():
    computer = ShipComputer([2, 3, 0, 3, 99])
    assert computer.runprogram()['itr'] == [2, 3, 0, 6, 99]


def test_computer_3():
    computer = ShipComputer([2, 4, 4, 5, 99, 0])
    assert computer.runprogram()['itr'] == [2, 4, 4, 5, 99, 9801]


def test_computer_4():
    computer = ShipComputer([1, 1, 1, 4, 99, 5, 6, 0, 99])
    assert computer.runprogram()['itr'] == [30, 1, 1, 4, 2, 5, 6, 0, 99]
