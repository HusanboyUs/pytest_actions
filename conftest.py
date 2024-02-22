import pytest
from main import Calculator


@pytest.fixture
def my_calculator():
    return Calculator()
