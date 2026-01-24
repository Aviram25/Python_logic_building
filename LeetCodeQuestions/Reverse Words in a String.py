class Solution(object):
    def reverseWords(self, s):
        
        # Split the string on any whitespace and rejoin with single spaces
        # This removes leading, trailing, and extra spaces
        s2 = " ".join(s.split())
        
        # Split the cleaned string into a list of words
        rev = s2.split()
        
        # Initialize an empty string to build the result
        empty = ""
        
        # Iterate over the words in reverse order with index
        for idx, i in enumerate(rev[::-1]):
            # Append the current word
            empty += i
            
            # Add a space after the word unless it's the last one
            if idx != len(rev) - 1:
                empty += " "
        
        # Return the reversed words as a single string
        return empty


# --------------------------------------------Alternate Version without using loops----------------------------------------------------------

class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        return " ".join(words[::-1])

