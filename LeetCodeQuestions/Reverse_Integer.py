class Solution(object):
    def reverse(self, x):
        INT_MIN = -2**31          # -2147483648
        INT_MAX = 2**31 - 1       # 2147483647
        
        rev = 0
        n = abs(x)

        while n != 0:
            digit = n % 10
            n //= 10

            # Check for overflow BEFORE updating rev
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return rev if x > 0 else -rev
