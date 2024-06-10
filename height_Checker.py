from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list,output = sorted(heights),0
        #print(sorted_list)
        #print(heights)
        for i in range(0, len(heights)):
            #print(heights[i])
            if heights[i] != sorted_list[i]:
                output +=1
                
        return output

d =Solution()
print(d.heightChecker([1,1,4,2,1,3]))
