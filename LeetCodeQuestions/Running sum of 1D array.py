class Solution(object):
    def runningSum(self, nums):  #[1,2,3,4]
        l1 = []
        count = 0
        for i in nums:
            count+=i
            l1.append(count)
        return l1     
