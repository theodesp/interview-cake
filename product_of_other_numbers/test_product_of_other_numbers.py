import pytest
from .products_of_other_numbers import get_products_of_all_ints_except_at_index


@pytest.mark.parametrize("test_input,expected", [
   ([1, 7, 3, 4], [84, 12, 28, 21]),
   ([1, 2, 3, 4], [24, 12, 8, 6])
])
def test_products_of_other_numbers(test_input, expected):
    assert get_products_of_all_ints_except_at_index(test_input) == expected