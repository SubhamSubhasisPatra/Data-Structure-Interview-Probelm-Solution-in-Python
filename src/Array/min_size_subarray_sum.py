def min_size_subarray_sum(arr, target):
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
