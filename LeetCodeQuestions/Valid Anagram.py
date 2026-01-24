class Solution(object):
    def isAnagram(self, s, t):
        # Compare character frequency counts of both strings
        # If both have the same characters with the same counts,
        # they are anagrams
        return Counter(s) == Counter(t)
