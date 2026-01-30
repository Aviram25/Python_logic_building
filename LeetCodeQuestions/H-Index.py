class Solution(object):
    def hIndex(self, citations):
        count = 0
        citations.sort(reverse=True)  #[3,1,1]
        
        for i in range(1,(len(citations)+1)):  
            if citations[i-1] >= i:
                count += 1
        return count    
