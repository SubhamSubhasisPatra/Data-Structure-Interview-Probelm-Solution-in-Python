"""
LEETCODE -> https://leetcode.com/problems/text-justification/
"""

import math


def add_words_per_line(words, word_index, max_width, result, row_index):
    cur_words = []
    cur_len = 0
    while word_index < len(words):
        cur_len += (len(words[word_index]) + 1)
        if cur_len <= max_width:
            cur_words.append(words[word_index])
            word_index += 1
        else:
            break

    result[row_index] = cur_words
    return word_index


def full_justify(words, max_width):
    total_rows = math.ceil(len("".join(words)) / max_width)

    result = [0] * total_rows
    word_index = 0
    for row in range(total_rows):
        word_index = add_words_per_line(words, word_index, max_width, result, row)

    print(result)


if __name__ == '__main__':
    full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    full_justify(["What","must","be","acknowledgment","shall","be"], 16)
