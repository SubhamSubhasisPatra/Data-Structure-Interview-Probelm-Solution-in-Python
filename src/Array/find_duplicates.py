def find_duplicate(arr):
    hashMap = {}
    for i in arr:
        if i in hashMap:
            return i
        else:
            hashMap[i] = 1


if __name__ == '__main__':
    elements = [10, 20, 3, 14, 1, 1]
    result = find_duplicate(elements)
    print(result)
