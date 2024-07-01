def search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:

        mid = (low + (high - low) // 2)

        if arr[mid] == target:
            return True

        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False


if __name__ == '__main__':
    print(search([1, 2, 3, 4, 5, 6, 7, 8, 9], 90))
