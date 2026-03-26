# https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        seen = set()
        current = head.next
        prev = head
        seen.add(prev.data)
        while current!=None:
            if current.data not in seen:
                seen.add(current.data)
                current = current.next
                prev = prev.next
            else:
                if current.next!=None:
                    current.data = current.next.data
                    current.next = current.next.next
                else:
                    prev.next = None
                    current = current.next
        return head