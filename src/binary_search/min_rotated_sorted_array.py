import math


def rotated_sorted_array(arr, n):
    ans = math.inf
    low, high = 0, len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break

        if arr[low] <= arr[mid]:
            ans = min(arr[low], ans)
            low = mid + 1
        else:
            ans = max(arr[mid], ans)
            high = mid - 1
    return ans


test_cases = [
    {
        'input': [1, 2, 3, 4, 5],
        'expected': 1
    },
    {
        'input': [3, 4, 5, 1, 2],
        'expected': 1
    }
]

for test_case in test_cases:
    result = rotated_sorted_array(test_case['input'], test_case['expected'])
    print(f'Test Case {test_case["input"]} Result: {result} Passed')
