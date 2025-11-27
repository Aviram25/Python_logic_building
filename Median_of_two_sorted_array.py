class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Step 1: Merge nums2 into nums1
        # extend() appends all elements of nums2 into nums1 (in-place)
        nums1.extend(nums2)

        # Step 2: Sort the merged list
        nums1.sort()

        # Total number of elements after merging
        n = len(nums1)

        # Step 3: If length is odd → median is the middle element
        if n % 2 == 1:
            return nums1[n // 2]

        # Step 4: If length is even → median is the average of the two middle elements
        else:
            mid = n // 2
            left_middle = nums1[mid - 1]
            right_middle = nums1[mid]
            return (left_middle + right_middle) / 2.0
