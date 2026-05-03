# This file is used to store variables and functions
# TODO:
#   Make this file store variables and functions

# Import modules
from parse import parsing1, parsing2
from string import punctuation, whitespace, digits
from atoms import *

# Had to remove ',' from punctuation otherwise Bind(x, 3) would give an error
punctuation.replace(",", "")

# Define Errors
class NameError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

# Store all variables with name : value
Variables = {}

def store_variable(argument : String) -> None:
    # Make sure argument is a Stringing that starts with 'Bind(' and ends with either ')' or whitespace
    if not isinstance(argument, String): raise SyntaxError(f"Variable {argument} is not a String")
    if not argument.startswith("Bind("): raise SyntaxError(f"Variable {argument} doesn't start with 'Bind('")
    if not argument.endswith(")") and not argument[-1].isspace(): raise SyntaxError(f"Variable {argument} doesn't end properly")

    # Check if there's anything invalid in the name of the variable
    if argument[5] in digits: raise NameError(f"Variable {argument}'s name is invalid")
    parsing1(argument[5:], Memory(punctuation, whitespace), f"Variable {argument}'s name is invalid", ',')
    name = argument[5:argument.find(",")]
    parsing2(argument[argument.find(','):], )
    
