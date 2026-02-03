class Solution(object):
    def findPeakElement(self, nums):
        max_elem  = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_elem]:
                max_elem = i
        return max_elem      
