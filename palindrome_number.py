class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        l_indx = 0
        r_indx = len(x)-1
        while l_indx <= len(x)-1 and r_indx >= 0:
            print(x[r_indx])
            if x[l_indx] != x[r_indx]:
                return False
            l_indx +=1
            r_indx -=1
            
        return True

        #s =str(x)
        #if s == s[::-1]:
        #    return True
        #else:
        #    return False

d= Solution()
print(d.isPalindrome(-121))
