# Tool for finding the mean and mean absolute deviation of a data set


# This function assumes the list has been sorted
def get_quartiles(nums: list[float]) -> tuple[float, float, float]:
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


def separate_outliers(nums: list[float], quartiles: tuple[float, float, float]) -> list[float]:
    outliers = []

    iqr = quartiles[2] - quartiles[0]
    boundary = quartiles[0] - 1.5 * iqr, quartiles[2] + 1.5 * iqr

    for n in list(nums):
        if n <= boundary[0] or n >= boundary[1]:
            outliers.append(n)
            nums.remove(n)

    return outliers


def get_mean(nums: list[float]) -> float:
    sum = 0

    for i in nums:
        sum += i

    return sum / len(nums)


def get_mean_absolute_deviation(nums: list[float], mean: float) -> float:
    sum = 0

    for i in nums:
        sum += abs(i - mean)

    return sum / len(nums)


def parse_data(string: str) -> list[float]:
    data = []
    number_strings = string.split(' ')

    for n in number_strings:
        try:
            data.append(float(n))
        except ValueError:
            print(f"Value \"{n}\" can't be parsed.")
    return data


def main() -> None:
    raw = input("Enter a list of numbers: ")

    while raw != "x":
        nums = parse_data(raw)
        nums.sort()
        q1, median, q3 = get_quartiles(nums)

        print(f"\nSorted Input: {nums}")
        print(f"\nQuartiles: {q1:.2f}, {median:.2f}, {q3:.2f}")
        print(f"1.5 * IQR Boundaries: {q1 - 1.5 * (q3 - q1):.2f}, {q3 + 1.5 * (q3 - q1):.2f}")
        print(f"IQR Outliers: {separate_outliers(nums, (q1, median, q3))}")

        print(f"Filtered Input: {nums}")
        m = get_mean(nums)
        mad = get_mean_absolute_deviation(nums, m)
        print(f"\nMean and MAD are: {m:.4f} +/- {mad:.6f}")

        raw = input("\nEnter data: ")


if __name__ == "__main__":
    main()
