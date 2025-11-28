class Solution(object):
    def longestPalindrome(self, s):
        # If the string is empty, return empty string
        if not s:
            return ""

        n = len(s)
        longest = ""   # Stores the longest palindrome found so far

        # Outer loop picks the starting index of the substring
        for i in range(n):

            # Inner loop picks the ending index of the substring
            # Starts from i so that substring is always valid
            for j in range(i, n):

                # Extract substring from index i to j (inclusive)
                sub = s[i:j+1]

                # Check if substring is a palindrome
                # And check if it's longer than the current best palindrome
                if sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub   # Update the longest palindrome

        # Return the longest palindromic substring found
        return longest
