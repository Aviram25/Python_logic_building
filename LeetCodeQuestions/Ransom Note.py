class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        r = Counter(ransomNote)
        m = Counter(magazine)

        for i in r:
            if r[i] > m[i]:
                return False
        return True                
        
