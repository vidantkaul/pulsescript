
import pytest

from src.parse import parsing1, parsing2

@pytest.mark.parametrize("L", [1, 5, 123, "hello", False, True, "happy", "hello"])
@pytest.mark.parametrize("")
def test_parse1(L):
    L
    