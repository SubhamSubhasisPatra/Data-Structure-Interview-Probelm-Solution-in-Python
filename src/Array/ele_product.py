def element_product_non_optimal(arr):
    result = []
    # N^2
    for index in range(len(arr)):
        new_arr = arr[:index] + arr[index + 1:]
        cur_result = 1
        for ele in new_arr:
            cur_result *= ele
        result.append(cur_result)

    return result


def element_product_with_division(arr):
    # N, with division
    total_product = 1
    result = []

    for element in arr:
        total_product *= element

    for index in range(len(arr)):
        result.append(total_product // arr[index])

    return result


def super_optimal(arr):
    # N, without division
    n = len(arr)

    # Calculate the prefix products
    result = [1] * n
    prefix_product = 1
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= arr[i]

    # Calculate the suffix products and combine with prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= arr[i]

    return result


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(element_product_non_optimal(arr))
    print(element_product_with_division(arr))
    print(super_optimal(arr))
