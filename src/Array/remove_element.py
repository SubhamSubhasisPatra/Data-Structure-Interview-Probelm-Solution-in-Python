
def remove_element(nums, element):
    c = 0
    for i in range(nums):
        if i != element:
            nums[c] = i  
            c += 1 
            
    print(nums, counter)


if __name__ == '__main__':
    arr = [3, 2, 2, 3]
    n = 3

    remove_element(arr, n)
