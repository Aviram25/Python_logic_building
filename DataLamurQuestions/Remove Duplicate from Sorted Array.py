class Solution(object):
    def removeDuplicates(self, nums):

        # If the array is empty, there are no unique elements
        if not nums:
            return 0

        # j points to the index of the last unique element found
        j = 0

        # Start from the second element since the first is always unique
        for i in range(1, len(nums)):

            # If the current element is different from the last unique one
            if nums[j] != nums[i]:

                # Move j forward to store the next unique element
                j += 1

                # Overwrite the duplicate with the new unique value
                nums[j] = nums[i]

        # Number of unique elements is j + 1
        # Only the first j+1 elements are valid
        return j + 1
