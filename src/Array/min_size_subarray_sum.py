"""
LEETCODE -> https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
"""

def min_size_subarray_sum(arr, target):
    """
    :param arr: a list of integers representing the input array
    :param target: an integer representing the target sum
    :return: minimum length of a subarray in arr whose sum is greater than or equal to target

    This method takes an array of integers, arr, and a target sum, target, as input. It returns the minimum length of a subarray in arr whose sum is greater than or equal to target.

    Example usage:
    ---------------
    arr = [2, 3, 1, 2, 4, 3]
    target = 7
    min_size_subarray_sum(arr, target)  # Returns 2

    Explanation:
    ---------------
    In the given example, the subarray [4, 3] has a sum of 7 which is equal to the target. The length of this subarray is 2, which is the minimum possible length for a subarray with a sum of 7.
    """
    if not arr or not target: return 0
    count, i, j, n, res = 0, 0, 0, len(arr), float('inf')
    while j < n:
        if count < target:
            count += arr[j]
        j += 1
        while i <= j and count >= target:
            res = min(res, j - i)
            count -= arr[i]
            i += 1
    print(res if res < float('inf') else 0)


if __name__ == '__main__':
    min_size_subarray_sum([1, 1, 1, 1, 1, 1, 1, 1], 11)
    min_size_subarray_sum([1, 4, 4], 4)
    min_size_subarray_sum([2, 3, 1, 2, 4, 3], 7)
    min_size_subarray_sum([12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12], 213)
