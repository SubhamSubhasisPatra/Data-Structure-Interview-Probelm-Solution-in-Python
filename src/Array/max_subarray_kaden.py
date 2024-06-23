import math


def max_subarray_brute_force(nums):
    # Generate all possible sub array
    # Find the max sum of that

    if len(nums) == 1:
        return nums[0]

    # assign negative infinite
    max_sub = -9999999999999

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            max_sub = max(max_sub, sum(nums[i:j + 1]))

    return max_sub


def max_subarray_better(nums):
    if len(nums) == 1: return nums[0]
    max_sub = -math.inf

    # Keep the sum prior to the 2nd iteration to save repeated calculation

    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sub = max(max_sub, cur_sum)
    return max_sub


def max_subarray(nums):
    max_sub = -math.inf
    total = 0

    start, end = -1, -1  # To keep tack of all the subarray element

    for i in range(len(nums)):
        if total == 0: start = i
        total += nums[i]

        if total > max_sub:
            max_sub = total
            end = i

        if total < 0: total = 0

    print(nums[start:end + 1])
    return max_sub


# Add some test cases
test_cases = [
    {
        'input': [5, 4, -1, 7, 8],
        'expected': 23,
    },
    {
        'input': [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        'expected': 6,
    },
    {
        'input': [1],
        'expected': 1
    },
    {
        'input': [-1, -2, -3],
        'expected': 0,
    }
]

for test_case in test_cases:
    print(max_subarray(test_case['input']))
