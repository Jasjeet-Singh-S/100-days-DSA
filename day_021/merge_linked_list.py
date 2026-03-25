# https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        current=ListNode()
        if(list1!=None and list2!=None):
            if list1.val<=list2.val:
                current=list1
                list1=list1.next
            else:
                current=list2
                list2=list2.next
        elif(list1!=None):
            current=list1
            list1=list1.next
        elif(list2!=None):
            current=list2
            list2=list2.next
        else:
            return list1  # or list2
        current_ptr = current
        while(list1!=None or list2!=None):
            if(list1==None):
                current_ptr.next=list2
                current_ptr=current_ptr.next
                list2=list2.next
            elif(list2==None):
                current_ptr.next=list1
                current_ptr=current_ptr.next
                list1=list1.next
            elif(list1.val<=list2.val):
                current_ptr.next=list1
                current_ptr=current_ptr.next
                list1=list1.next
            else:  # (list2.val<list1.val)
                current_ptr.next=list2
                current_ptr=current_ptr.next
                list2=list2.next
        return current