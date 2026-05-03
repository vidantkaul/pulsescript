# This module is used for parsing complex/simple strings or lists

# Define Errors
class ParsingError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

# wcb stands for What it Can't Be
# Use this function to check if the str or list has something invalid in it
# l is the list that we're parsing
# wcb is what we're checking should NOT be in the list
# error_msg - uh I think this is self-explanitory if you code. If you don't, it's the error message you get if wcb is in l
# stop is optional, but it's the place in the list where you can stop
def parsing1 (l : list | str, wcb : list[str], error_msg : str, stop : str | None = None) -> None:
    assert isinstance(l, (list, str))
    assert isinstance(wcb, list[str])
    assert isinstance(error_msg, str)
    assert isinstance(stop, (str, None))

    for i in l:            # Make i a string so that any other type can't bypass wcb
        if not isinstance(i, str): i = str(i)
        elif stop and i == stop: break
        elif i in wcb: raise ParsingError(error_msg)
        else: continue
    return

# This is the same as parsing1 except wcb now stands for:
# What it Can Be
def parsing2 (l : list | str, wcb : list[str], error_msg : str, stop : str | None = None) -> None:
    assert isinstance(l, (list, str))
    assert isinstance(wcb, list[str])
    assert isinstance(error_msg, str)
    assert isinstance(stop, (str, None))
    
    for i in l:
        if not isinstance(i, str): i = str(i)
        elif stop and i == stop: break
        elif i not in wcb: raise ParsingError(error_msg)
        else: continue
    return
