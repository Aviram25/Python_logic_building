def triangular_sum_v1(nums):
    """
    Recursive approach: Create new array in each iteration
    
    Base case: If array has only 1 element, return it
    Recursive case: Create new array with sums, recurse
    
    Time: O(n²) - n + (n-1) + (n-2) + ... + 1
    Space: O(n) - recursion depth + array storage
    """
    # Base case: only one element left
    if len(nums) == 1:
        return nums[0]
    
    # Create new array for next iteration
    new_nums = []
    for i in range(len(nums) - 1):
        new_nums.append((nums[i] + nums[i + 1]) % 10)
    
    # Recursively process the new array
    return triangular_sum_v1(new_nums)


# def triangular_sum_v2(nums):
#   if len(nums) == 1:
#     return nums[0]
    
#   new_nums = []
#   for i in range(len(nums)-1):
#     new_nums.append((nums[i]+ nums[i+1])%10 )
    
  # return triangular_sum_v2(new_nums)  
