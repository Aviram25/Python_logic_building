class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindrome
        if x < 0:
            return False

        original = x
        rev = 0

        # Reverse the integer
        while x != 0:
            digit = x % 10
            x = x // 10
            rev = rev * 10 + digit

        # Compare reversed number with original
        return rev == original
