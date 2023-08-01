def jump(nums) -> int:
    """
    :param nums: List of integers representing the maximum number of steps that can be jumped from each position in the input array
    :return: Total number of jumps needed to reach to the last position in the input array

    """
    total_jumps, cur_end, cur_farthest = 0, 0, 0

    for i in range(len(nums) - 1):
        cur_farthest = max(cur_farthest, nums[i] + i)
        if i == cur_end:
            total_jumps += 1
            cur_end = cur_farthest
    return total_jumps


if __name__ == '__main__':
    nums = [2, 3, 0, 0, 4]
    print(jump(nums))
