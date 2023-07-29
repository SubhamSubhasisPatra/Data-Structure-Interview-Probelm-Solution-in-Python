def jump(nums) -> int:
    """
    :param nums: List of integers representing the maximum number of steps that can be jumped from each position in the input array
    :return: Total number of jumps needed to reach to the last position in the input array

    This method takes in an input array `nums` and calculates the minimum number of jumps needed to reach to the last position in the array. Each element in the array represents the maximum number of steps that can be jumped from that position.

    The method uses the variables `total_jumps`, `cur_end`, and `cur_farthest` to keep track of the current jump count, the end index of the current jump, and the farthest position that can be reached from the current jump, respectively.

    The method iterates over the input array from index 0 to index `len(nums) - 2` (excluding the last position). For each index `i`, it updates the `cur_farthest` by taking the maximum of the current `cur_farthest` and `nums[i] + i`. This calculates the farthest position that can be reached from the current index.

    If the current index `i` is equal to `cur_end`, it means that the current jump has reached its end. In this case, the method increments the `total_jumps` by 1 and updates the `cur_end` to `cur_farthest`. This represents starting a new jump from the farthest position reached so far.

    Finally, the method returns the `total_jumps` as the minimum number of jumps needed to reach the last position in the input array.
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
