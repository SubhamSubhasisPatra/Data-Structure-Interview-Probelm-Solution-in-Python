"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

from math import floor, inf


def majority_element_II(nums: list) -> list:
    """
     keep a hashmap and counter
         What ever arr len u pick u will have at most 2 element in the list
         len(nums) 8 , floor(8/3) = 2 , at least the numer count should be 3 , 3 + 3 + 3 = 9 , but array len is 8
         So at most we will have 2 element
     find the floor value
     loop over each element and store hash map
     return the values which have more counter than the floor value
    """

    result_map = {}
    floor_val = floor(len(nums) / 3)
    res = []

    for num in nums:
        if num in result_map:
            result_map[num] += 1
        else:
            result_map[num] = 1

        if result_map[num] > floor_val: res.append(num)
        if len(res) == 2: break

    return res


def optimized_majority_element_II(nums: list) -> list:
    element1, element2 = inf, inf
    counter1, counter2 = 0, 0

    for i in range(len(nums)):

        if counter1 == 0 and nums[i] != element2:
            counter1 = 1
            element1 = nums[i]

        elif counter2 == 0 and nums[i] != element1:
            counter2 = 1
            element2 = nums[i]

        elif element1 == nums[i]:
            counter1 += 1
        elif element2 == nums[i]:
            counter2 += 1
        else:
            counter1 -= 1
            counter2 -= 1

    res = []
    counter1, counter2 = 0, 0
    for num in nums:
        if element2 == num: counter2 += 1
        if element1 == num: counter1 += 1

    mini = floor(len(nums) / 3) + 1
    if counter1 >= mini: res.append(element1)
    if counter2 >= mini: res.append(element2)
    return sorted(res)


# Add some test cases
test_cases = [
    {
        'input': [3, 2, 3],
        'output': [3]
    },
    {
        'input': [1],
        'output': [1]
    },
    {
        'input': [1, 2],
        'output': [1, 2]
    }
]

for test_case in test_cases:
    # response = majority_element_II(test_case['input'])
    response = optimized_majority_element_II(test_case['input'])
    print(response == test_case['output'], response)
