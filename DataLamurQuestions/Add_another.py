def plus_one(digits):
    """
    Add 1 to number represented as array of digits
    
    Strategy:
    1. Start from the rightmost digit (ones place)
    2. Add 1
    3. If result is 10, set to 0 and carry 1 to next digit
    4. If no carry needed, we're done
    5. If we carry through all digits, prepend 1
    
    Time: O(n) where n = number of digits
    Space: O(1) - modify in place (or O(n) if count the output)
    """
    n = len(digits)
    
    # Traverse from right to left (least significant to most significant)
    for i in range(n - 1, -1, -1):
        # Add 1 to current digit
        digits[i] += 1
        
        # If digit becomes 10, set it to 0 and continue (carry over)
        if digits[i] == 10:
            digits[i] = 0
            # Continue loop to carry 1 to next digit
        else:
            # No carry needed, we're done!
            return digits
    
    # If we exit the loop, it means we carried through all digits
    # Example: [9,9,9] becomes [0,0,0], need to prepend 1
    return [1] + digits


# Test cases
print(plus_one([1, 2, 3]))    # [1, 2, 4]
print(plus_one([6, 9]))       # [7, 0]
print(plus_one([9, 9, 9]))    # [1, 0, 0, 0]
print(plus_one([0]))          # [1]
