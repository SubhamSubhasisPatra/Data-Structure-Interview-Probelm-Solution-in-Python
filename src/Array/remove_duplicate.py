
def remove_duplicates(arr):
    c = 0

    for i in arr:

        if c < 2 or i != arr[c - 2]:
            arr[c] = i
            c += 1
    return c


if __name__ == '__main__':
    numbers = [2, 3, 3, 3, 4, 4, 5]
    remove_duplicates(numbers)
