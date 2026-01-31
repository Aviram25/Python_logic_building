class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        count = 1
        max_streak = 1
        nums.sort()  #[1,2,3,4,100,200]
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]-1:
                count+=1
            elif nums[i] == nums[i-1]:
                continue        
            else:
                max_streak = max(max_streak,count)
                count = 1
        return max(max_streak,count)    
