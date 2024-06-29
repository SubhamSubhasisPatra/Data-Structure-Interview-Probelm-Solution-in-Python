import math


def next_permute(nums):
    index = -1

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break

    if index == -1:
        return nums[::-1]

    for i in range(len(nums) - 1, index, -1):

        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    nums[index + 1:] = nums[index + 1:][::-1]
    return nums


# print(next_permute([2, 1, 5, 2, 1, 0]))


def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i - 1]: continue
        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]: j += 1
                while j < k and nums[k] == nums[k + 1]: k -= 1
    return res


# print(three_sum([-1, 0, 1, 2, -1, -4]))


def max_subarray(nums):
    max_sum = 0
    total = 0

    for i in range(len(nums)):

        total += nums[i]

        if total > max_sum:
            max_sum = total

        if total < 0:
            total = 0
    return max_sum


# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def majority_element(nums):
    ele1, ele2 = math.inf, math.inf
    c1 = c2 = 0
    for num in nums:
        if num != ele2 and c1 == 0:
            c1 = 1
            ele1 = num
        elif num != ele1 and c2 == 0:
            c2 = 1
            ele2 = num
        elif ele1 == nums:
            c1 += 1
        elif ele2 == nums:
            c2 += 1
        else:
            c1 -= 1
            c2 -= 1

    res = []
    c1 = c2 = 0
    for num in nums:
        if num == ele1: c1 += 1
        if num == ele2: c2 += 1

    mini = math.floor(len(nums) / 3) + 1

    if c1 >= mini: res.append(ele1)
    if c2 >= mini: res.append(ele2)
    return sorted(res)


# print(majority_element([3, 2, 3]))


def xor(nums, target):
    xr = 0
    res = {
        xr: 1
    }
    counter = 0
    for i in range(len(nums)):
        xr ^= nums[i]

        x = xr ^ target

        if x in res: counter += res[x]

        if xr in res:
            res[xr] += 1
        else:
            res[xr] = 1

    return counter


# print(xor([4, 2, 2, 6, 4], 6))


def max_prod_subarray(nums):
    res = nums[0]
    n = len(nums)
    prefix = suffix = 1

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]
        suffix *= nums[n - i - 1]
        res = max(res, max(prefix, suffix))

    return res


# print(max_prod_subarray([-2, 0, -1]))


def missing_repeating_numer(arr, n):
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1)) // 6
    S = 0
    S2 = 0

    for num in arr:
        S += num
        S2 += num ** 2

    val1 = S - SN
    val2 = S2 - S2N
    val2 = val2 // val1

    x = (val1 + val2) // 2
    y = x - val1
    return [x, y]


print(missing_repeating_numer([1, 3, 3], 3))
