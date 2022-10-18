# Tool for finding the mean and mean absolute deviation of a data set
from typing import Callable
from stats_math import eval_mean_mad


def parse_data(split: list[str]) -> list[float]:
    data = []

    for n in split:
        try:
            data.append(float(n))
        except ValueError:
            print(f"Value \"{n}\" can't be parsed.")
    return data


def parse_command(raw: str, commands: dict[str, Callable]) -> Callable:
    command = raw.split(' ')[0]
    for key, func in commands.items():
        if raw == key:
            return func

    # Default command is to parse data
    return lambda data: data.extend(parse_data(raw.split(' ')))


def print_help(commands: dict[str, str]) -> None:
    for command, help in commands.items():
        print(f"{command} \t----\t {help}")


def main() -> None:
    nums = []

    command_help = {
        "help": "Prints this menu",
        "eval": "Evaluates the mean and MAD for the current data set",
        "clear": "Clears the data set",
        "<data>": "Adds the inputted data to the current set"
    }

    commands = {
        "eval": lambda data: eval_mean_mad(data),
        "clear": lambda data: data.clear(),
        "help": lambda data: print_help(command_help)
    }

    raw = input("Enter a command or raw data: ")

    while raw != "x":
        parse_command(raw, commands)(nums)
        raw = input("\nEnter data or a command (\"x\" to quit): ")


if __name__ == "__main__":
    main()
