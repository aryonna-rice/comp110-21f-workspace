"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Will return a fortune."""
    chance: int = randint(1, 100)
    if chance < 25: 
        return("Someone special will come into your life soon.")
    elif chance < 50:
        return("Something BIG is about to happen in your life!")
    elif chance < 75:
        return("Your hard work is about to pay off.")
    else: 
        return("Cheer up... good things come to those who wait.")
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 


if __name__ == "__main__":
    main()