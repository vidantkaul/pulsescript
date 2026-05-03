# This module is used for parsing complex/simple string's or Memory's

# Import modules
from atoms import *

# Define Errors
class ParsingError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

# wcb stands for What it Can't Be
# Use this function to check if the String or Memory has something invalid in it
# l is the Memory that we're parsing
# wcb is what we're checking should NOT be in the Memory
# error_msg - uh I think this is self-explanitory if you code. If you don't, it's the error message you get if wcb is in l
# stop is optional, but it's the place in the Memory where you can stop
def parsing1 (l : Memory | String, wcb : Memory[String], error_msg : String, stop : String | None = None) -> None:
    if not isinstance(l, Memory) and not isinstance(l, String): raise SyntaxError
    assert isinstance(wcb, Memory)
    assert isinstance(error_msg, String)
    if stop and not isinstance(stop, String): raise SyntaxError

    for i in l:
        # Make sure i is a string
        if stop and String(i) == stop: break
        # Make sure i is a string
        elif String(i) in wcb: raise ParsingError(error_msg)
        else: continue
    return

# This is the same as parsing1 except wcb now stands for:
# What it Can Be
def parsing2 (l : Memory | String, wcb : Memory[String], error_msg : String, stop : String | None = None) -> None:
    assert isinstance(l, (Memory, String))
    assert isinstance(wcb, Memory[String])
    assert isinstance(error_msg, String)
    assert isinstance(stop, (String, None))
    
    for i in l:
        if stop and String(i) == String(stop): break
        elif String(i) not in wcb: raise ParsingError(error_msg)
        else: continue
    return
