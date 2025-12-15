# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        # Dummy node acts as a fixed starting point for the merged list

        curr = dummy
        # Pointer used to build the merged list step by step

        # Continue merging while both lists still have nodes
        while l1 and l2:
            # Compare current node values of both lists
            if l1.val < l2.val:
                curr.next = l1
                # Attach the smaller node to the merged list
                l1 = l1.next
                # Move forward in list l1
            else:
                curr.next = l2
                # Attach the smaller node to the merged list
                l2 = l2.next
                # Move forward in list l2

            curr = curr.next
            # Advance the merged list pointer

        # At this point, one list is exhausted
        # Attach the remaining nodes from the non-empty list
        curr.next = l1 if l1 else l2

        # Return the merged list (skipping the dummy node)
        return dummy.next
