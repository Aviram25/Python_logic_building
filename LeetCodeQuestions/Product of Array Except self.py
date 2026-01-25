class Solution(object):
    def productExceptSelf(self, nums):
        # Length of the input array
        n = len(nums)

        # Result array initialized with 1s
        # result[i] will eventually store:
        # (product of elements to the left of i) *
        # (product of elements to the right of i)
        result = [1] * n

        # -------------------------------
        # Step 1: Prefix products
        # -------------------------------
        # 'left' keeps track of the product of all elements to the left
        left = 1
        for i in range(n):
            # Store product of elements before index i
            result[i] = left

            # Update left to include current element
            left *= nums[i]

        # -------------------------------
        # Step 2: Suffix products
        # -------------------------------
        # 'right' keeps track of the product of all elements to the right
        right = 1
        for i in range(n - 1, -1, -1):
            # Multiply existing left product with right product
            result[i] *= right

            # Update right to include current element
            right *= nums[i]

        # Final result array
        return result
