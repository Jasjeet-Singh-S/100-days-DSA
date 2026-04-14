class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr):
        if not arr:
            return None
        
        head = cls(arr[0])
        current = head
        
        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        
        return head

    @classmethod
    def compare_lists(cls, head1, head2):
        curr1 = head1
        curr2 = head2

        while curr1 and curr2:
            if curr1.val != curr2.val:
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
                print(head.val, end=", ")
            else:
                print(head.val)
            head = head.next
        print("]")


class Solution:
    def divide(self, head):
        even_head = None
        even_tail = None
        odd_head = None
        odd_tail = None

        ptr = head
        while ptr is not None:
            next_node = ptr.next
            ptr.next = None
            if ptr.val % 2 == 0:
                if even_head is None:
                    even_head = even_tail = ptr
                else:
                    even_tail.next = ptr
                    even_tail = ptr
            else:
                if odd_head is None:
                    odd_head = odd_tail = ptr
                else:
                    odd_tail.next = ptr
                    odd_tail = ptr
            ptr = next_node

        if even_head is None:
            return odd_head
        even_tail.next = odd_head
        return even_head


def main():
    head_1 = ListNode.from_list([17,15,8,9,2,4,6])
    expected_output_1 = ListNode.from_list([8,2,4,6,17,15,9])
    head_2 = ListNode.from_list([1,3,5,7])
    expected_output_2 = ListNode.from_list([1,3,5,7])

    sol = Solution()

    actual_output_1 = sol.divide(head_1)
    actual_output_2 = sol.divide(head_2)

    if(ListNode.compare_lists(expected_output_1, actual_output_1) and
       ListNode.compare_lists(expected_output_2, actual_output_2)):
        print("pass")
    else:
        print("fail")
        ListNode.print_list(actual_output_1)
        ListNode.print_list(expected_output_1)
        ListNode.print_list(actual_output_2)
        ListNode.print_list(expected_output_2)


if __name__=="__main__":
    main()