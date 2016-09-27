import pytest
from .highest_product import get_highest_product


@pytest.mark.parametrize("test_input,expected", [
   ([1, 7, 3, 4], 84),
   ([1, 2, 3, 4, 9], 108),
   ([1, 2, 3, 4, 9, -11, -5], 495)
])
def test_get_highest_product(test_input, expected):
    assert get_highest_product(test_input) == expected