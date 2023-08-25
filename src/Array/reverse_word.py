def reverse_word(s):
    s = s.split(' ')
    result = ''
    for index in range(len(s) - 1, -1, -1):
        if s[index]:
            result += (s[index] + ' ')
    print(result)


if __name__ == '__main__':
    reverse_word("a good   example")
