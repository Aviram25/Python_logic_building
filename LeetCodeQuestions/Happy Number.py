class Solution(object):
    def isHappy(self, n):
        if n < 0:
            return False

        seen = set()

        while n != 1:
            if n in seen:       # track the full number n
                return False
            seen.add(n)

            # calculate next sum-of-squares
            temp_sum = 0
            while n > 0:
                temp = n % 10
                temp_sum += temp ** 2
                n = n // 10

            n = temp_sum

        return True
