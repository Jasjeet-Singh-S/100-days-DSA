# https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

class Solution:
    def removeLoop(self, head):
        seen = set()
        curr = head
        prev = None
        
        while curr is not None:
            if curr in seen:
                prev.next = None
                return True
            
            seen.add(curr)
            prev = curr 
            curr = curr.next
            
        return False