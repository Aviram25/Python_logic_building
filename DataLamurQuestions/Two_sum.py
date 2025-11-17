def two_sum(nums: list[int], target: int) -> list[int]:
    # We do NOT need a temp list because we return as soon as we find a match

    i = 0  # i = index of the first number
    while i < len(nums):  # Loop through all elements
        j = i + 1         # j starts from the next element (can't use same element twice)

        while j < len(nums):  # Compare nums[i] with every number after it
            # Check if the pair adds up to the target
            if nums[i] + nums[j] == target:
                return [i, j]  # Return the indices immediately if match found

            j += 1  # Move to next index for j

        i += 1  # Move i to next index and repeat

    # If no valid pair found, return [-1, -1]
    return [-1, -1]
