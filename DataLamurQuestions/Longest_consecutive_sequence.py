def longest_consecutive(nums):
    if not nums:
        return 0

    s = sorted(nums)
    longest = []
    curr = [s[0]]

    for i in range(1, len(s)):
        # skip duplicates
        if s[i] == s[i-1]:
            continue

        # consecutive
        if s[i] == s[i-1] + 1:
            curr.append(s[i])
        else:
            # sequence broke → update longest
            if len(curr) > len(longest):
                longest = curr
            curr = [s[i]]  # reset with a list, NOT an int!

    # final update
    if len(curr) > len(longest):
        longest = curr

    return len(longest)
