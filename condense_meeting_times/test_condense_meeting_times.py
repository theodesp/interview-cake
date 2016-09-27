import pytest
from .condense_meeting_times import condense_meeting_times


@pytest.mark.parametrize("test_input,expected", [
   ([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], [(0, 1), (3, 8), (9, 12)]),
   ([(6,8), (1,9), (2,4), (4,7)], [(1,9)])
])
def test_condense_meeting_times(test_input, expected):
    assert condense_meeting_times(test_input) == expected