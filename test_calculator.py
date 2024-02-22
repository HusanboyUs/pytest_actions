import pytest
from main import Calculator




def test_add_numbers(my_calculator: Calculator):
    num1, num2 = 3,5
    assert my_calculator.add_numbers(num1,num2) == 8


def test_minus_numbers(my_calculator: Calculator):
    assert my_calculator.minus_numbers(5,1) == 4


def test_subtract_numbers(my_calculator: Calculator):
    assert my_calculator.subtract_numbers(4,2) == 2


def test_mutliply_numbers(my_calculator: Calculator):
    assert my_calculator.multiply_numbers(4,2) == 8


@pytest.mark.parametrize("number1,number2,exptected", [
    (5,2,True),
    (10,3,True),
    (99,10,True),
    (70,45,True),
    (45,60,False)
])
def test_is_bigger(number1,number2,exptected,my_calculator: Calculator):
    assert my_calculator.is_bigger(number1,number2) == exptected


@pytest.mark.xfail(reason='It is broken')
def test_is_small(my_calculator: Calculator):
    assert my_calculator.is_small(3,6) == True


def test_number_square(my_calculator: Calculator):
   with pytest.raises(TypeError):
       assert my_calculator.number_square(4) == 16

@pytest.mark.skip
def test_number_rooot(my_calculator: Calculator):
    my_calculator.number_root(4)

