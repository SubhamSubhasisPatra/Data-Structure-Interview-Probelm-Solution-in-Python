def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


test_case = [
    {
        'input': [[2, 5, 6, 0, 0, 1, 2], 2],
        'output': True
    },
    {
        'input': [[2, 5, 6, 0, 0, 1, 2], 3],
        'output': False
    }
]

for test_case in test_case:
    print(binary_search(test_case['input'][0], test_case['input'][1]))
