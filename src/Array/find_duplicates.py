def find_duplicate(arr):
    hashMap = {}
    for i in arr:
        if i in hashMap:
            return i
        else:
            hashMap[i] = 1


def remove_duplicate(arr):
    return set(arr)

if __name__ == '__main__':
    elements = [10, 20, 3, 14, 1, 1]
    result = remove_duplicate(elements)
    print(result)
