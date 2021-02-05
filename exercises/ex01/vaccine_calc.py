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
pop: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_day: int = int(input("Doses per day: "))
target: float = int(input("Target percent vaccinated: ")) / 100

already: int = int(round(doses_admin / 2))
total: int = int(round(target * pop))
still_need: int = int(total - already)
ppl_per_day: int = int(round(doses_day / 2))
days_needed: int = int(round(still_need / ppl_per_day))
pct: str = str(int(target * 100))
n_days: str = str(days_needed)

today: datetime = datetime.today()
how_many_days: timedelta = timedelta(days_needed)
date: datetime = today + how_many_days

print("We will reach " + pct + "% vaccination in " + n_days + " days, which falls on " + date.strftime("%B %d, %Y"))