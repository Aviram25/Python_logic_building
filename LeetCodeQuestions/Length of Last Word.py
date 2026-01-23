class Solution(object):
    def lengthOfLastWord(self, s):
        # Split the string into a list of words using whitespace
        s1 = s.split()
        
        # Get the last word from the list
        last_word = s1[-1]
        
        # Return the length of the last word
        return len(last_word)
