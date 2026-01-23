class Solution(object):
    def longestCommonPrefix(self, strs):
        # Edge case: empty list
        if not strs:
            return ""
        
        # Sort the list
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        
        i = 0
        # Compare characters of first and last
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        # Return common prefix
        return first[:i]
