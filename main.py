# Tool for finding the mean and mean absolute deviation of a data set
from typing import Callable
from stats_math import eval_mean_mad, parse_data


# Parses a command and returns a function to execute and the command's arguments
def parse_command(raw: str, commands: dict[str, Callable]) -> tuple[Callable, list[str]]:
    split = raw.split(' ')
    command = split[0]
    args = []

    if len(split) > 1:
        args = split[1:]

    for key, func in commands.items():
        if command == key:
            return func, args

    # Default command is to parse data
    return lambda data, args: data.extend(parse_data(raw.split(' '))), []


def print_help(commands: dict[str, str]) -> None:
    for command, help in commands.items():
        print(f"{command} \t----\t {help}")


def main() -> None:
    nums = []

    command_help = {
        "help": "Prints this menu",
        "eval": "Evaluates the mean and MAD for the current data set",
        "eval <args>": "Evaluates the mean and MAD for the data inputted",
        "clear": "Clears the data set",
        "<data>": "Adds the inputted data to the current set"
    }

    commands = {
        "eval": lambda data, args: eval_mean_mad(data, args),
        "clear": lambda data, args: data.clear(),
        "help": lambda data, args: print_help(command_help)
    }

    raw = input("Enter a command or raw data: ")

    while raw != "x":
        func, args = parse_command(raw, commands)
        func(nums, args)

        raw = input("\nEnter data or a command (\"x\" to quit): ")


if __name__ == "__main__":
    main()
