import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("input, expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    (4, "4"),
])
def test_fizzbuzz(input, expected):
    assert fizzbuzz(input) == expected
