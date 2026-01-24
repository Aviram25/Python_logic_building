class Solution(object):
    def wordPattern(self, pattern, s):
        
        # Split the input string into a list of words
        s1 = s.split()
        
        # Dictionaries for bidirectional mapping:
        # pattern character → word
        p_to_s = {}
        # word → pattern character
        s_to_p = {}

        # If pattern length and word count differ, mapping is impossible
        if len(pattern) != len(s1):
            return False
        
        # Traverse pattern and words together
        for i in range(len(pattern)):
            
            # Check consistency of pattern → word mapping
            if pattern[i] in p_to_s and p_to_s[pattern[i]] != s1[i]:
                return False
            
            # Check consistency of word → pattern mapping
            if s1[i] in s_to_p and s_to_p[s1[i]] != pattern[i]:
                return False   
            
            # Record the mapping from pattern character to word
            p_to_s[pattern[i]] = s1[i]
            
            # Record the reverse mapping from word to pattern character
            s_to_p[s1[i]] = pattern[i]  

        # If no conflicts were found, the pattern matches the string
        return True
