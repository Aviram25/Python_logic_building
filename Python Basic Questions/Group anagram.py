class Solution(object):
    def groupAnagrams(self, strs):
        anagramDict = {}
        for i in strs:  #["eat","tea","tan","ate","nat","bat"]
            sortedStr = "".join(sorted(i))
            if sortedStr not in anagramDict:
                anagramDict[sortedStr] = []
            anagramDict[sortedStr].append(i)
        return list(anagramDict.values())    
