"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730316437"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Should return a fortune based on random number chosen"""
    x: int = int(randint(1, 40))
    if x < 10:
        return "You will have a great day."
    else:
        if x < 20:
            return "You will find what you have been looking for."
        else:
            if x < 30:
                return "Someone special will come into your life soon."
            else:
                return "You will receieve many compliments today"


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
