"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730316437"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
number: int = randint(1, 40)
if number < 10:
    print("You will have a great day.")
else:
    if number < 20:
        print("You will find what you have been looking for.")
    else:
        if number < 30:
            print("Someone special will come into your life soon.")
        else:
            if number <= 40:
                print("You will receieve many compliments today")
print("Now, go spread positive vibes!")
