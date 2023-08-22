def compute_lsp(pattern, patt_len, lps):
    """
    Compute the Longest Proper Prefix which is also a Suffix (LPS) array.

    :param pattern: The pattern string.
    :param patt_len: The length of the pattern string.
    :param lps: The LPS array to be filled.
    :return: None

    This method computes the LPS array which stores the length of the longest proper prefix that is also a
    suffix for each position in the pattern string.

    The LPS array construction follows the Knuth-Morris-Pratt (KMP) algorithm. It uses two pointers, 'pointer' and 'i',
    to compare characters of the pattern string. The 'pointer' points to the previous character which has the longest
    proper prefix and is also a suffix until a given position i. Initially, pointer = 0.

    The algorithm iterates through each character in the pattern string from left to right (i.e., i = 1 to patt_len-1).
    If pattern[i] matches pattern[pointer], then the 'pointer' is incremented and lps[i] is assigned the value of
    'pointer + 1', indicating that the longest proper prefix which is also a suffix has length 'pointer + 1'.
    Then, 'i' is incremented to compare the next character.

    If pattern[i] does not match pattern[pointer], then we adjust the pointer. If pointer != 0, we set pointer to the
    value of lps[pointer - 1], which indicates the length of the longest proper prefix that is also a suffix before
    the character at position 'pointer'. We repeat this process until pointer becomes 0.

    If pointer becomes 0, that means there is no prefix which is also a suffix before the current position i.
    In this case, we assign lps[i] = 0 and increment i to compare the next character.

    This process continues until all the positions in the LPS array are filled.

    Example usage:
    pattern = "ABABACA"
    patt_len = 7
    lps = [0] * patt_len
    compute_lsp(pattern, patt_len, lps)
    print(lps)  # Output: [0, 0, 1, 2, 3, 0, 1]

    Complexity Analysis:
    The time complexity of this method is O(patt_len), where patt_len is the length of the pattern string.

    Note: This method modifies the original 'lps' array passed as an input parameter.

    """
    pointer = 0
    lps[0] = 0
    i = 1

    while i < patt_len:
        if pattern[i] == pattern[pointer]:
            pointer += 1
            lps[i] = pointer
            i += 1
        else:
            if pointer != 0:
                pointer = lps[pointer - 1]
            else:
                lps[i] = 0
                i += 1


def has_substring(pattern, text):
    """
    Check if a given pattern exists as a substring within a text.

    :param pattern: The pattern to search for.
    :param text: The text to search within.
    :return: The index of the first occurrence of the pattern in the text, or 0 if not found.

    """
    M = len(pattern)
    N = len(text)

    # create the LPS
    lps = [0] * M
    j = 0

    compute_lsp(pattern, M, lps)

    i = 0
    final_index = 0

    while (N - i) >= (M - j):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            # on Last index
            final_index = i - j
            j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return final_index


if __name__ == '__main__':
    txt = "abcdeabd"
    pat = "abd"
    print(has_substring(pat, txt))
