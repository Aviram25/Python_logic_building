class Solution(object):
    def searchInsert(self, nums, target):

        # Traverse the array index by index
        for i in range(len(nums)):

            # If the current number is greater than or equal to target
            # this is the position where target should be placed
            if nums[i] >= target:
                return i

        # If target is greater than all elements in nums,
        # it should be inserted at the end of the array
        return len(nums)
