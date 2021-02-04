"""A vaccination calculator."""

__author__ = "730316437"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
Pop: int = int(input("Population: "))
Doses_admin: int = int(input("Doses administered: "))
Doses_day: int = int(input("Doses per day: "))
Target: float = int(input("Target percent vaccinated: ")) / 100

already: int = int(round(Doses_admin/2))
total: int = int(round(Target * Pop))
still_need: int = int(total - already)
ppl_doses_day: int = int(round(Doses_day/2))
days_needed: int = int(round(still_need / ppl_doses_day))

today: datetime = datetime.today()
how_many: timedelta = timedelta(days_needed)
date: datetime = today + how_many

print("We will reach " + str(int(Target * 100)) + "% vaccination in " + str(days_needed) + " days, which falls on " + date.strftime("%B %d, %Y"))





