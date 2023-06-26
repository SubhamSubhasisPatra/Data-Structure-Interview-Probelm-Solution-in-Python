"""

eg arr [3,2,3], n = 3 

if n/2 = 1.5 , if any number has a count more than that , that is the major element 

"""


def majorityElement( nums: List[int]) -> int:
    majorCount = len(nums) / 2 
    count = {}
    
    for i in nums:
        if i in count:
            count[i] += 1 
        else:
            count[i] = 1 
        # find the major Count 
        if count[i] >= majorCount:
            return i 
