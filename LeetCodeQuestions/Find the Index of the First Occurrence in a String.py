class Solution(object):
    def strStr(self, haystack, needle):

        # find() searches for the first occurrence of 'needle'
        # inside the string 'haystack'
        #
        # If 'needle' is found:
        #   → returns the starting index of its first occurrence
        #
        # If 'needle' is NOT found:
        #   → returns -1
        return haystack.find(needle)
