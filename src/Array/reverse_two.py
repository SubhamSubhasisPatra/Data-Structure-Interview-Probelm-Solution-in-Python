vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])


def reverse_vowels(s):
    s_list = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1

        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return ''.join(s_list)


def reverse_vowel_non_optimal(s):
    v_list = []

    result = ''

    for v in s:
        if v in vowels:
            v_list.append(v)

    for ele in s:
        if ele not in vowels:
            result += ele
        else:
            result += v_list.pop()

    return result


if __name__ == '__main__':
    s1 = "hello"
    print(reverse_vowels(s1))  # Output: "holle"
    print(reverse_vowel_non_optimal(s1))  # Output: "holle"

    s2 = "leetcode"
    print(reverse_vowels(s2))  # Output: "leotcede"
    print(reverse_vowel_non_optimal(s2))  # Output: "leotcede"
