import math


def max_product_subarray_optimal(arr):
    if not arr:
        return 0

    prefix = suffix = 1
    result = -math.inf

    for i in range(len(arr) - 1):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= arr[i]
        suffix *= arr[len(arr) - i - 1]
        result = max(result, max(prefix, suffix))

    return result


def max_product_subarray(arr):
    if not arr:
        return 0

    max_product = float('-inf')
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            max_product = max(max_product, product)

    return max_product


test_cases = [
    {
        'input': [1, 2, 3, 4, 5],
        'output': 120
    },
    {
        'input': [-1, -2, 0, -4, -5],
        'output': 20
    },
    {
        'input': [0, 2],
        'output': 2
    }
]

for test_case in test_cases:
    # print(max_product_subarray(test_case['input']))
    print(max_product_subarray_optimal(test_case['input']))
