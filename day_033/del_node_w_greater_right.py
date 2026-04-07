class Solution:
    def compute(self,head):
        ptr_1 = head
        ptr_2 = head.next
        # initialize
        if ptr_2.data>ptr_1.data:
            head = ptr_2
        while ptr_2 != None and ptr_2.next != None:
            if ptr_2.data>ptr_2.next.data:
                ptr_1.next = ptr_2.next
                ptr_2 = ptr_2.next
            else:
                ptr_1 = ptr_1.next
                ptr_2 = ptr_2.next
        return head 