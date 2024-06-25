def subarray_given_xor_brute_force(a, b):
    """
    Time Complexity: O(N^3)
    Space Complexity: O(1)
    a: an array of integers
    b: int
    return: int
    """

    # two sum subarray with XOR
    count = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            xor = 0
            for index in range(i, j + 1):
                xor ^= a[index]
            if xor == b:
                count += 1

    return count


def subarray_given_xor_better2(a, b):
    count = 0
    for i in range(len(a)):
        xor = 0
        for j in range(i, len(a)):
            xor ^= a[j]
            if xor == b:
                count += 1
    return count


def subarray_given_xor_optimal(arr, k):
    xr = 0
    count = 0
    res = {
        xr: 1
    }

    for i in range(len(arr)):
        xr ^= arr[i]

        x = xr ^ k
        if x in res:
            count += res[x]

        if xr in res:
            res[xr] += 1
        else:
            res[xr] = 1

    return count


test_cases = [{
    "input": [[4, 2, 2, 6, 4], 6],
    "output": 4
}]
for test_case in test_cases:
    # print("Worst Solution", subarray_given_xor_brute_force(test_case["input"][0], test_case["input"][1]))
    # print("Better Solution", subarray_given_xor_better2(test_case["input"][0], test_case["input"][1]))
    print("Most Optimal Solution", subarray_given_xor_optimal(test_case["input"][0], test_case["input"][1]))
