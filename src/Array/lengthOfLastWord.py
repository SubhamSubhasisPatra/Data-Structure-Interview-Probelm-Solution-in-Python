def len_of_last_word(s):
    return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    test_string = 'Hello World'
    print(len_of_last_word(test_string))
