def romanToInt(s):
    # Dictionary mapping Roman numeral characters to their integer values
    rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    ans = 0  # Initialize the result accumulator
    i = 0    # Index pointer to traverse the string
    
    while i < len(s):
        # Check if there's a next character and if it has a greater value
        # This handles subtractive cases like IV (4), IX (9), XL (40), etc.
        if i + 1 < len(s) and rom[s[i+1]] > rom[s[i]]:
            # Subtract current value (e.g., I in IV means subtract 1)
            ans -= rom[s[i]]
            i += 1
        else:
            # Normal case: add the current character's value
            # This handles standalone numerals or the second part of subtractive pairs
            ans += rom[s[i]]
            i += 1
    
    return ans
