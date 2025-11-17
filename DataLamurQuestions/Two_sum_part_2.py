def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1   # Two-pointer setup: start + end of sorted array

    while left < right:
        s = nums[left] + nums[right]  # Current sum of the two pointers

        if s == target:
            return [left, right]      # Found the exact pair

        elif s < target:
            left += 1                 # Sum too small → move left pointer rightward

        else:
            right -= 1                # Sum too big → move right pointer leftward

    return [-1, -1]                   # No valid pair found
