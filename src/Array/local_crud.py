import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            index, last = self.pos[val], self.nums[-1]
            self.nums[index], self.pos[last] = last, index
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]

