def missing_and_repeating(arr, n):
    res_hash = [0] * (n + 1)

    for i in range(n):
        res_hash[arr[i]] += 1

    repeating_num = -1
    missing_num = -1
    for i in range(1, n + 1):
        if res_hash[i] == 2:
            repeating_num = i
        elif res_hash[i] == 0:
            missing_num = i

        if repeating_num != -1 and missing_num != -1:
            break

    return missing_num, repeating_num


def missing_and_repeating2_math(arr, n):
    SN = (n * (n + 1)) / 2
    S2N = (n * (n + 1) * (2 * n + 1)) / 6
    S, S2 = 0, 0

    for i in range(n):
        S += arr[i]
        S2 += arr[i] * arr[i]

    val1 = S - SN
    val2 = (S2 - S2N)
    val2 = val2 / val1

    x = (val1 + val2) / 2
    y = x - val1
    return x, y


test_cases = [
    {
        'input': [[2, 2], 2],
        'expected': [1, 2]
    },
    {
        'input': [[1, 3, 3], 3],
        'expected': [2, 3]
    }
]

for test_case in test_cases:
    result = missing_and_repeating2_math(test_case['input'][0], test_case['input'][1])
    print(f"Input: {test_case['input'][0]}, Output: {result}, Expected: {test_case['expected']}")
