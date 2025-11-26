class Solution(object):
    def maxSumDivThree(self, nums):
        # Step 1: Calculate the total sum of all numbers
        total = sum(nums)

        # Step 2: If total is already divisible by 3, return it immediately
        if total % 3 == 0:
            return total

        # Step 3: Create two lists to store numbers by their remainder modulo 3
        r1 = []  # Numbers where num % 3 == 1
        r2 = []  # Numbers where num % 3 == 2

        # Step 4: Populate r1 and r2 lists
        for i in nums:
            if i % 3 == 1:
                r1.append(i)
            elif i % 3 == 2:
                r2.append(i)

        # Step 5: Sort both lists to access the smallest numbers easily
        r1.sort()
        r2.sort()

        # Step 6: If total has remainder 1, fix it by removing smallest values
        if total % 3 == 1:
            remove_one = float('inf')  # Initialize to infinity in case option not available
            remove_two = float('inf')

            # Option A: Remove the smallest number with remainder 1
            if len(r1) >= 1:
                remove_one = r1[0]

            # Option B: Remove the two smallest numbers with remainder 2
            if len(r2) >= 2:
                remove_two = r2[0] + r2[1]

            # Step 7: Remove the option with minimal loss to maximize sum
            return total - min(remove_one, remove_two)

        # Step 8: If total has remainder 2, fix it similarly
        if total % 3 == 2:
            remove_one = float('inf')  # Initialize to infinity in case option not available
            remove_two = float('inf')

            # Option A: Remove the smallest number with remainder 2
            if len(r2) >= 1:
                remove_one = r2[0]

            # Option B: Remove the two smallest numbers with remainder 1
            if len(r1) >= 2:
                remove_two = r1[0] + r1[1]

            # Step 9: Remove the option with minimal loss to maximize sum
            return total - min(remove_one, remove_two)
