from collections import Counter


def majorityElement(nums: list[int]) -> int:
    majorCount = len(nums) / 2
    count = Counter(nums)

    # Returns the element in count if its occurrence is more than majorCount
    return next((k for k, v in count.items() if v > majorCount), None)
