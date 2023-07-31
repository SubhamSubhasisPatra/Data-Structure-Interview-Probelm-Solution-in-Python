def len_of_last_word(s):
    return len(s.strip().split(' ')[-1])

def optimized_len_count(s):

    size = len(s)
    max_count  = 0
    flag = False

    for i in range(size - 1  , 0 , -1):

        if s[i] == ' ' and flag:
            break

        if s[i] != ' ':
            max_count += 1
            flag = True

    return max_count


if __name__ == '__main__':
    test_string = 'Hello World'
    print(len_of_last_word(test_string))
    print(optimized_len_count(test_string))
