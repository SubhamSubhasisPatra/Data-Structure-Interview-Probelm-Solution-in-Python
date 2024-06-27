from heapq import merge


def count_inversion_brute(arr):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    counter = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                counter += 1
    return counter


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    counter = 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            counter += (mid - left + 1)
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return counter


def merge_sort(arr, low, high):
    counter = 0
    if low < high:
        m = low + (high - low) // 2
        counter += merge_sort(arr, low, m)
        counter += merge_sort(arr, m + 1, high)
        counter += merge(arr, low, m, high)
    return counter


def count_inversion(arr):
    return merge_sort(arr, 0, len(arr) - 1)


test_cases = [
    {
        'input': [5, 3, 2, 4, 1],
        'expected': 8
    },
    {
        'input': [5, 4, 3, 2, 1],
        'expected': 10
    }
]

for test_case in test_cases:
    result = count_inversion(test_case['input'])
    print(result, test_case['expected'] == result)
