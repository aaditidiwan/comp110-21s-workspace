"""Tar Heels exercise redux as a structured program."""

__author__ = "730316437"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))

def tar_heels(n: int) -> str:
    """Returns a UNC related string"""
    if n % 2 == 0 and n % 7 == 0:
        return "TAR HEELS"
    else:
        if n % 2 == 0:
            return "TAR"
        else:
            if n % 7 == 0:
                return "HEELS"
            else:
                return "CAROLINA"    


if __name__ == "__main__":
    main()
