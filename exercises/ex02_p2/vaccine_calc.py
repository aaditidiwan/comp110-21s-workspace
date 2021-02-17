"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730316437"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days_till: int = int(days_to_target(population, doses, doses_per_day, target))
    later_date: str = str(future_date(days_till))
    pct: str = str(int(target))
    print("We will reach " + pct + "% vaccination in " + str(days_till) + " days, which falls on " + later_date)


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    already: int = int(round(doses / 2))
    decimal: float = float(target/100)
    total: int = int(round(decimal * population))
    still_need: int = int(total - already)
    ppl_per_day: int = int(round(doses_per_day / 2))
    days_needed: int = int(round(still_need / ppl_per_day))
    return(days_needed)


def future_date(days_till: int) -> str: 
    n_days: str = str(days_till)
    today: datetime = datetime.today()
    how_many_days: timedelta = timedelta(days_till)
    date: datetime = today + how_many_days
    return(date.strftime("%B %d, %Y"))

if __name__ == "__main__":
    main()
