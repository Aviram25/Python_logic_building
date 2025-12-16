class Solution(object):
    def removeElement(self, nums, val):

        # If the array is empty, nothing to remove
        if not nums:
            return 0

        # j points to the index where the next valid element should be placed
        j = 0  

        # i scan every element in the array
        for i in range(len(nums)):

            # Keep the element only if it is NOT equal to val
            if nums[i] != val:

                # Place the valid element at index j
                nums[j] = nums[i]

                # Move j forward to the next free position
                j += 1

        # The first j elements now contain all elements != val
        # Return j (number of valid elements)
        return j
