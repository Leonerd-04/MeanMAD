def parse_data(split: list[str]) -> list[float]:
    data = []

    for n in split:
        try:
            data.append(float(n))
        except ValueError:
            print(f"Value \"{n}\" can't be parsed.")
    return data


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
        if n < boundary[0] or n > boundary[1]:
            outliers.append(n)
            nums.remove(n)

    return outliers


def get_mean(nums: list[float]) -> float:
    if len(nums) == 0:
        return 0

    sum = 0

    for i in nums:
        sum += i

    return sum / len(nums)


def get_mean_absolute_deviation(nums: list[float], mean: float) -> float:
    if len(nums) == 0:
        return 0

    sum = 0

    for i in nums:
        sum += abs(i - mean)

    return sum / len(nums)


# Prints the data evaluation to the console
def eval_mean_mad(saved: list[float], inputted: list[str]) -> None:
    if len(inputted) > 0:
        data = parse_data(inputted)
    else:
        data = saved

    data.sort()
    q1, median, q3 = get_quartiles(data)

    print(f"\nSorted Input: {data}")
    print(f"\nQuartiles: {q1:.2f}, {median:.2f}, {q3:.2f}")
    print(f"1.5 * IQR Boundaries: {q1 - 1.5 * (q3 - q1):.2f}, {q3 + 1.5 * (q3 - q1):.2f}")
    print(f"IQR Outliers: {separate_outliers(data, (q1, median, q3))}")

    print(f"Filtered Input: {data}")
    m = get_mean(data)
    mad = get_mean_absolute_deviation(data, m)
    print(f"\nMean and MAD are: {m:.4f} ?? {mad:.6f}")