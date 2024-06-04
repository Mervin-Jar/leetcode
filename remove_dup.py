from typing import List
class Solution:
    def __init__(self):
        pass
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                print(nums[i])
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j

d= Solution()

print(d.removeDuplicates([1,1,2]))
