def reverse_vowels(s):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
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


if __name__ == '__main__':
    s1 = "hello"
    print(reverse_vowels(s1))  # Output: "holle"

    s2 = "leetcode"
    print(reverse_vowels(s2))  # Output: "leotcede"
