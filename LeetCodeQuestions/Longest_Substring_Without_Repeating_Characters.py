class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # Stores the longest substring found so far
        longest = ''

        # Temporary sliding window substring (keeps current valid substring without duplicates)
        temp = ''

        # Loop through each character in the string
        for ch in s:

            # If the character is NOT inside the current substring,
            # simply extend the substring by adding it
            if ch not in temp:
                temp += ch

            else:
                # If we see a duplicate character:
                # Find the index of the duplicate character inside "temp"
                idx = temp.index(ch)

                # Remove everything up to (and including) that duplicate
                # and then add the current character back
                # This effectively "slides the window"
                temp = temp[idx + 1:] + ch

            # Update the longest substring if the current temp is longer
            if len(temp) > len(longest):
                longest = temp

        # Return the length of the longest substring found
        return len(longest)
