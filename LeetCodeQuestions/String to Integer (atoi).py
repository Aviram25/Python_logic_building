class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            i += 1
        num = 0
        while i < len(s)  and '0' <= s[i] <= '9':  
            num = num * 10 + (ord(s[i]) - 48)
            i += 1
        num *= sign
        INTMIN,INTMAX = -2**31, 2**31 - 1
        return max(INTMIN,min(num,INTMAX))    
