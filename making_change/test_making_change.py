import pytest
from .making_change import get_change_count, get_change_count_dynamic, get_change_count_dynamic_space


@pytest.mark.parametrize("test_input,expected", [
     ([4, []], 0),
     ([-1, [1,2,3]], 0),
     ([4, [1]], 1),
     ([4, [3]], 0),
     ([4, [1, 2, 3]], 4),
     ([5, [1, 2]], 3)
])
def test_get_change_denominations(test_input, expected):
    assert get_change_count(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize("test_input,expected", [
     ([4, []], 0),
     ([-1, [1,2,3]], 0),
     ([4, [1]], 1),
     ([4, [3]], 0),
     ([4, [1, 2, 3]], 4),
     ([5, [1, 2]], 3)
])
def test_get_change_denominations(test_input, expected):
    assert get_change_count_dynamic(test_input[0], test_input[1]) == expected

@pytest.mark.parametrize("test_input,expected", [
     ([4, []], 0),
     ([-1, [1,2,3]], 0),
     ([4, [1]], 1),
     ([4, [3]], 0),
     ([4, [1, 2, 3]], 4),
     ([5, [1, 2]], 3)
])
def test_get_change_denominations(test_input, expected):
    assert get_change_count_dynamic_space(test_input[0], test_input[1]) == expected