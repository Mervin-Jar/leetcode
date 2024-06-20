from collections import defaultdict
from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cache = defaultdict(int)
        pairs = 0
        print(cache)
        for num in nums:
            cache[num] += 1
            print(cache)
            if cache[num] % 2 == 0:
                pairs += 1        

        return [pairs, len(nums) - pairs * 2]

d= Solution()
print(d.numberOfPairs([1,3,2,1,3,2,2]))

'''
        for i in range(0,m-1):
            print(nums)
            print("i",i)
            if nums[i] == nums[i+1]:
                removed +=1
                print(nums[i+1],nums[i])
                nums.remove(nums[i+1])
                nums.remove(nums[i])
                m=len(nums)
                break
'''
