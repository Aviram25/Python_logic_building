class Solution(object):
    def isSubsequence(self, s, t):
        idx = 0

        for i in t:
            if idx < len(s) and s[idx] == i :
                idx += 1
        return idx == len(s)             
