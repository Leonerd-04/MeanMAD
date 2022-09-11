# Tool for finding the mean and mean absolute deviation of a data set


# This function assumes the list has been sorted
def quartiles(nums: list[float]) -> tuple[float, float, float]:
    if len(nums) % 2 == 1:
        median = nums[(len(nums) - 1) // 2]
        half, second_half = (len(nums) - 1) // 2, (len(nums) + 1) // 2
    else:
        median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        half = second_half = len(nums) // 2

    if len(nums) % 4 > 1:
        q1 = nums[(half - 1) // 2]
        q3 = nums[second_half + (half - 1) // 2]
    else:
        q1 = (nums[half // 2 - 1] + nums[half // 2]) / 2
        q3 = (nums[second_half + half // 2 - 1] + nums[second_half + half // 2]) / 2

    return q1, median, q3


def outliers(nums: list[float], quartiles: tuple[float, float, float]) -> list[float]:
    outliers = []

    iqr = quartiles[2] - quartiles[0]
    boundary = quartiles[0] - 1.5 * iqr, quartiles[2] + 1.5 * iqr

    for n in nums:
        if n <= boundary[0] or n >= boundary[1]:
            outliers.append(n)

    return outliers


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
        nums.sort()
        q1, median, q3 = quartiles(nums)

        print(f"\nResults: {nums}")
        print(f"Quartiles: {q1:.3f}, {median:.2f}, {q3:.2f}")
        print(f"1.5 * IQR Boundaries: {q1 - 1.5 * (q3 - q1):.2f}, {q3 + 1.5 * (q3 - q1):.2f}")
        print(f"IQR Outliers: {outliers(nums, (q1, median, q3))}")

        m = mean(nums)
        mad = mean_absolute_deviation(nums, m)
        print(f"Mean and MAD of results are: {m:.4f} +/- {mad:.6f}")

        raw = input("\nEnter a list of numbers: ")


if __name__ == "__main__":
    main()