# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        n = len(lists)
        
        dummy = ListNode()
        current = dummy

        while any(lists):
            smallest = None
            smallest_index = -1

            for i in range(n):
                if lists[i] is not None:

                    if smallest is not None or lists[i].val < smallest.val:
                        smallest = lists[i]
                        smallest_index = i

            current.next = smallest
            current = current.next

            lists[smallest_index] = lists[smallest_index].next

        return dummy.next