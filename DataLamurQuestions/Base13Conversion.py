def convertToBase13(num): 
    # Handle the special case where the number is 0
    if num == 0:
        return "0"
    
    # String containing all valid digits for base 13
    # 0-9 are regular digits, A=10, B=11, C=12
    base_digits13 = "0123456789ABC"
    
    # String to store the base 13 digits (initially empty)
    digit = ""
    
    # Work with the absolute value to handle negative numbers separately
    positive = abs(num)
    
    # Keep extracting digits until the number becomes 0
    while positive > 0:
        # Get the remainder when dividing by 13 (this is the current digit)
        temp = positive % 13  
        
        # Convert the remainder to its base 13 character and add to our digit string
        digit += base_digits13[temp]
        
        # Integer division by 13 to move to the next digit position
        positive = positive // 13
    
    # Reverse the digit string because we built it backwards
    # (we got the rightmost digit first, but need leftmost digit first)
    reverse_digit = digit[::-1]
    
    # If the original number was negative, add a minus sign
    if num < 0:
        return "-" + reverse_digit
    else:
        return reverse_digit
