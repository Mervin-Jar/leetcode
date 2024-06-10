class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #string = s       
        for ele in range(0,len(s)):
            print(s)
            s = s[1:len(s)] + s[0]
            if s == goal:
                return True
        return False


d=Solution()
d.rotateString('abcde','cdeab')
