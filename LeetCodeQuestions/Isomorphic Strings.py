class Solution(object):
    def isIsomorphic(self, s, t):
        
        # Dictionary to map characters from s → t
        s_to_t = {}
        
        # Dictionary to map characters from t → s
        t_to_s = {}
        
        # Traverse both strings character by character
        for i in range(len(s)):
            
            # If s[i] was seen before, its mapping must stay consistent
            if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
                return False
            
            # If t[i] was seen before, its reverse mapping must stay consistent
            if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
                return False  

            # Record the mapping from s to t
            s_to_t[s[i]] = t[i]
            
            # Record the mapping from t to s
            t_to_s[t[i]] = s[i] 
        
        # If no conflicts were found, the strings are isomorphic
        return True
