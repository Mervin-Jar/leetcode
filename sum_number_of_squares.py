from math import *
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(isqrt(c)+1):
            j = c-i*i
            #print(j)
            if sqrt(j) %1 ==0:
                return True
        return False
d= Solution()
print(d.judgeSquareSum(5))
print(d.judgeSquareSum(3))
