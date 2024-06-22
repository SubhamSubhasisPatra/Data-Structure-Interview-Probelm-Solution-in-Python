"""
LEETCODE -> https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
"""

from itertools import combinations


def three_sum(arr):
    """
    NOT ACCEPTABLE -> Solution
    :param arr: A list of integers.
    :return: A list of tuples representing all unique combinations of three elements in `arr` that sum up to 0.

    """
    all_combinations = list(combinations(arr, 3))

    result = []
    for ele in all_combinations:
        if sum(ele) == 0:
            result.append(ele)

    print(result)





def three_sum_optimal(nums):
    
    # APPROCH - 1
    
    # loop thorught arr i , arr i + 1 arr i + 2 
    # Sum all 3 element , 
    # Create a hash to avoid duplicate 
    # Store to result arr 
    
    # APPROCH 2 
    
    # Lopp arr i and arr i + 1 
    # keep the inbetwen element of arr i and i + 1 in hash set 
    # target = - ( sum arr i + arr i + 1 )
    # Create a hash to avoid duplicate 
    # Store to result arr 
    
    # APPROCH 3 
    # Use Two pointer and one basic Start point 
    # Sort the array 
    # keep one point at the begniing 
    # keep one at the i + 1
    # keep one at the end of the array 
    # Sum i + ( i + 1 AKA j) + (LastIndex AKS K) **not equer **= target 
    # Move j to the next j += 1
    # Decremnet k = k - 1 
    # When it match to target 
    # Sum i + ( i + 1 AKA j) + (LastIndex AKS K) = target 
    # j += 1 , k -= 1 
    # Store to restult arr[i] , arr[j] , arr[k]
    # Move to the next new element 
    # while j < k and num[j] == num[j - 1] : j += 1;
    # while j < k and num[k] == num[k + 1] : k -= 1;
    
    result = []
    nums.sort()
    for i in range(len(nums)):
        
        if i > 0 and nums[i] == nums[i - 1]: continue
        
        j = i+ 1 
        k = len(nums) - 1 
        
        while j < k :
            
            target = nums[i] + nums[j] + nums[k]
            
            if target < 0 : j += 1 
            elif target > 0 : k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1 
                
                while j < k and nums[j] == nums[j-1] : j += 1
                while j < k and nums[k] == nums[k + 1]: k -= 1 
    print(result)



three_sum_optimal([-1, 0, 1, 2, -1, -4]) # [[-1, 0, 1], [-1, -1, 2]]
three_sum_optimal([-1,0,1]) # [[0, 0, 0]]
three_sum_optimal([-2,0,0,2,2]) #[[-2,0,2]]...

def optimal_3_sum(nums):
    nums = sorted(nums)
    res = set()

    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1

        target = 0 - nums[i]

        while l < r :
            if nums[l] + nums[r] == target:
                res.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return list(res)


if __name__ == '__main__':
    # print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(optimal_3_sum([-1, 0, 1, 2, -1, -4]))
