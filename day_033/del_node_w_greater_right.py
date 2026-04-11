# https://www.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
# this solution only removes adjacent node less than next node
# class Solution:
#     def compute(self,head):
#         ptr_1 = head
#         ptr_2 = head.next
#         # initialize
#         if ptr_2.data>ptr_1.data:
#             head = ptr_2
#         while ptr_2 != None and ptr_2.next != None:
#             if ptr_2.data<ptr_2.next.data:
#                 ptr_1.next = ptr_2.next
#                 ptr_2 = ptr_2.next
#             else:
#                 ptr_1 = ptr_1.next
#                 ptr_2 = ptr_2.next
#         return head 


# this solution keeps the wrong half of the decreasing linked list 
# class Solution:
#     def compute(self, head):
#         ptr_1 = head
        
#         while ptr_1 != None:
#             ptr_prev = ptr_1
#             ptr_2 = ptr_prev.next
#             while ptr_2 != None:
#                 if ptr_2.data>ptr_1.data:
#                     ptr_prev.next = ptr_2.next
#                     ptr_2 = ptr_2.next
#                 else:
#                     ptr_2 = ptr_2.next
#                     ptr_prev = ptr_prev.next
#             ptr_1 = ptr_1.next
#         return head

class Solution:
    def compute(self, head):
        reversed_LL_head = self.reverseList(head)
        ptr = reversed_LL_head
        greatest = ptr.data
        while ptr.next != None:
            if ptr.next.data>=greatest:
                ptr = ptr.next
                greatest = ptr.data
            else:
                ptr.next = ptr.next.next
        return self.reverseList(reversed_LL_head)

    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # Temporarily store the next node
            curr.next = prev # Flip the pointer to point backwards
            prev = curr      # Move 'prev' one step forward
            curr = nxt       # Move 'curr' one step forward
            
        return prev # 'prev' is the new head of the reversed list