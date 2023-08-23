"""
Leet code question -> https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
"""


def max_area(height):
    """
    Calculate the maximum area between two vertical lines formed by the given heights.

    :param height: A list of non-negative integers representing the heights of each vertical line.
    :return: The maximum area between two vertical lines.

    The method calculates the maximum area by iterating through each pair of vertical lines,
    calculating the area formed by the pair, and updating the maximum area if a larger area is found.
    The maximum area is then printed.
    """
    max_area_val = 0

    for index in range(len(height)):
        for next_index in range(index + 1, len(height)):
            area = (min(height[index], height[next_index]) * (next_index - index))
            if area > max_area_val:
                max_area_val = area

    print(max_area_val)


def optimal_max_area(height):
    """
    :param height: a list of integers representing the height of each bar in a container
    :return: the maximum area of water that can be contained by the given container

    The function 'optimal_max_area' takes a list of integers 'height' as input, where each element in the list represents the height of a bar in a container. It calculates and returns the maximum area of water that can be contained by the container.

    The function utilizes the Two Pointers approach to find the optimal solution. It starts with two pointers 'left' and 'right', initialized to the first and last indices of the 'height' list respectively.

    Then, it iteratively compares the heights of the bars pointed by 'left' and 'right'. If the height of the bar pointed by 'right' is greater than the height of the bar pointed by 'left', it calculates the area by multiplying the height of the bar pointed by 'left' with the difference between the indices of 'right' and 'left', and increments 'left' by 1. Otherwise, it calculates the area using the height of the bar pointed by 'right' and decrements 'right' by 1. The calculated area is then compared with the maximum area 'MAX' obtained so far, and the maximum value is stored in 'MAX'.

    The process continues until 'left' becomes greater than or equal to 'right'. Once the loop terminates, the function prints the maximum area 'MAX' as the result.

    Example usage:
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        optimal_max_area(height)

        Output:
        49
    """
    left, right = 0, len(height) - 1
    MAX = 0
    while left < right:
        if height[right] > height[left]:
            area = height[left] * (right - left)
            left += 1
        else:
            area = height[right] * (right - left)
            right -= 1
        MAX = max(MAX, area)
    print(MAX)


if __name__ == '__main__':
    max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    optimal_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    max_area([1, 1])
