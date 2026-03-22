class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        # Check if the current node exists at all
        while current is not None:
            next_node = current.next  # Save the rest of the list
            current.next = prev       # Reverse the pointer
            
            # Move the markers forward
            prev = current
            current = next_node
            
        # Once current is None, prev is the new head
        return prev

# had to take help from gpt unfortunately, i kept fumbling pointers