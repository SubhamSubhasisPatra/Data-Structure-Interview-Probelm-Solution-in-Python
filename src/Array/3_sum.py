"""
LEETCODE -> https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
"""

from itertools import combinations


def three_sum(arr):
    """
    NOT ACCEPTABLE -> Solution
    :param arr: A list of integers.
    :return: A list of tuples representing all unique combinations of three elements in `arr` that sum up to 0.

    """
    all_combinations = list(combinations(arr, 3))

    result = []
    for ele in all_combinations:
        if sum(ele) == 0:
            result.append(ele)

    print(result)


def optimal_3_sum(nums):
    nums = sorted(nums)
    res = set()

    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1

        target = 0 - nums[i]

        while l < r :
            if nums[l] + nums[r] == target:
                res.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return list(res)


if __name__ == '__main__':
    # print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(optimal_3_sum([-1, 0, 1, 2, -1, -4]))
