'''
# Node Class
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    @classmethod
    def from_list(cls, arr):
        if not arr:
            return None
        
        head = cls(arr[0])
        current = head
        
        for data in arr[1:]:
            current.next = cls(data)
            current = current.next
        
        return head

    @classmethod
    def compare_lists(cls, head1, head2):
        curr1 = head1
        curr2 = head2

        while curr1 and curr2:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        # If both reached end → equal, otherwise unequal
        return curr1 is None and curr2 is None
    
    @classmethod
    def print_list(cls, head):
        print("[", end="")
        while(head!=None):
            if head.next!=None:
                print(head.data, end=", ")
            else:
                print(head.data)
            head = head.next
        print("]")

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head

        length = self.list_len(head)
        pivot = (length + 1) // 2 # Find the midpoint
        
        # 1. Reach the end of the first half
        prev_node = None
        pivot_head = head
        for i in range(pivot):
            prev_node = pivot_head
            pivot_head = pivot_head.next
            
        # 2. SEVER THE CONNECTION (The Fix)
        if prev_node:
            prev_node.next = None
            
        # 3. Reverse the second half
        new_pivot_head = self.reverseList(pivot_head)
        
        # 4. Weave them together
        ptr = head
        while ptr and new_pivot_head:
            main_next = ptr.next
            reverse_next = new_pivot_head.next
            
            ptr.next = new_pivot_head
            # If main_next is None, it means we reached the end of the first half
            if main_next:
                new_pivot_head.next = main_next
            
            ptr = main_next
            new_pivot_head = reverse_next
        
        return head

    def reverseList(self, pivot_head):
        prev = None
        curr = pivot_head
        
        while curr:
            nxt = curr.next  # Temporarily store the next node
            curr.next = prev # Flip the pointer to point backwards
            prev = curr      # Move 'prev' one step forward
            curr = nxt       # Move 'curr' one step forward
            
        return prev # 'prev' is the new head of the reversed list

    def list_len(self, head):
        length = 0 
        while head!=None:
            length += 1
            head = head.next
        return length
    

def main():
    list_1 = ListNode.from_list([1,2,3,4])
    sol = Solution()
    output_1 = sol.reorderList(list_1)
    ListNode.print_list(output_1)

if __name__=="__main__":
    main()