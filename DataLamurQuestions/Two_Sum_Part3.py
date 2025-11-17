def max_sum_less_than_k(nums, k):
    nums.sort()                         # Sort so two-pointer strategy works
    left, right = 0, len(nums) - 1
    best = -1                           # Track the best valid sum < k

    while left < right:
        s = nums[left] + nums[right]    # Current pair sum

        if s < k:
            best = max(best, s)         # Valid sum → update best if larger
            left += 1                   # Move left to try a bigger sum
        else:
            right -= 1                  # Sum too large → decrease by moving right inwards

    return best                         # -1 if no valid sum was found
