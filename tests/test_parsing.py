
import pytest

from src.parse import parsing1, parsing2, ParsingError

@pytest.mark.parametrize("Wcb", [list(range(11, 100))])
def test_parse1(Wcb):
    L = [5, 10, "happy", False, True, 8, "hello"]
    parsing1(L, Wcb, "UnexpectedError")
    with pytest.raises(ParsingError):
        parsing2(L, Wcb, "expected error")
