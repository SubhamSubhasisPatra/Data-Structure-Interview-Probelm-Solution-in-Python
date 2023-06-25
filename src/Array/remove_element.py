def move_to_end(arr, index, ele):
    pass


def remove_element(nums, element):
    counter = 0

    for index in range(len(nums) - 1):
        cur_number = nums[index]
        if cur_number == element:
            counter += 1
            nums.pop(index)
            nums.append(cur_number)

            # move the element to the end of the arr but the condition is
            # how to also take care of the number which are not same as the given number
    print(nums, counter)


if __name__ == '__main__':
    arr = [3, 2, 2, 3]
    n = 3

    remove_element(arr, n)
