class Solution():
    def appendcharacter(self, s: str, t: str) -> int:
        s_indx, t_indx =0,0
        s_ln, t_ln = len(s), len(t)

        while s_indx < s_ln and t_indx < t_ln:
            if s[s_indx] ==  t[t_indx]:
                t_indx += 1
            s_indx += 1
        return len(t[t_indx:])

d= Solution()
print(d.appendcharacter('coaching','coding'))
print(d.appendcharacter('a','bcdef'))
print(d.appendcharacter('a','azt'))