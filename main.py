# Tool for finding the mean and mean absolute deviation of a data set


def mean(nums: list[float]) -> float:
    sum = 0

    for i in nums:
        sum += i

    return sum / len(nums)


def mean_absolute_deviation(nums: list[float], mean: float) -> float:
    sum = 0

    for i in nums:
        sum += abs(i - mean)

    return sum / len(nums)


def parse_num(string: str) -> list[float]:
    nums = []
    number_strings = string.split(' ')

    for n in number_strings:
        try:
            nums.append(float(n))
        except ValueError:
            print(f"Value \"{n}\" can't be parsed.")
    return nums


def main() -> None:
    raw = input("Enter a list of numbers: ")

    while raw != "x":
        nums = parse_num(raw)


        print(f"\nResults: {nums}")

        m = mean(nums)
        mad = mean_absolute_deviation(nums, m)
        print(f"Mean and MAD of results are: {m:.4f} +/- {mad:.6f}")

        raw = input("\nEnter a list of numbers: ")


if __name__ == "__main__":
    main()