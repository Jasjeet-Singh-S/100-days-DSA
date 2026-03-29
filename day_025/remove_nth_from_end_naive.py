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
                print(head.val, next=", ")
            else:
                print(head.val)
            head = head.next
        print("]")


class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        ptr_1 = head
        ptr_2 = head

        # calculate length
        while ptr_1!=None:
            length+=1
            ptr_1 = ptr_1.next

        # edge case: if we want to remove the head itself
        if n==length:
            return head.next
        
        # go to (length-n-1) node
        for _ in range(length-n-1):
            ptr_2 = ptr_2.next

        # delete the n the node
        ptr_2.next = ptr_2.next.next

        return head


def main():
    head_1 = ListNode.from_list([1,2,3,4,5])
    n_1 = 2
    expected_output_1 = ListNode.from_list([1,2,3,5])
    head_2 = ListNode.from_list([1])
    n_2 = 1
    expected_output_2 = ListNode.from_list([])
    head_3 = ListNode.from_list([1,2])
    n_3 = 1
    expected_output_3 = ListNode.from_list([1])

    solution = Solution()

    actual_output_1 = solution.removeNthFromEnd(head_1, n_1)
    actual_output_2 = solution.removeNthFromEnd(head_2, n_2)
    actual_output_3 = solution.removeNthFromEnd(head_3, n_3)

    if(ListNode.compare_lists(expected_output_1, actual_output_1) and
       ListNode.compare_lists(expected_output_2, actual_output_2) and
       ListNode.compare_lists(expected_output_3, actual_output_3)):
        print("pass")
    else:
        print("fail")
        ListNode.print_list(expected_output_1)
        ListNode.print_list(actual_output_1)
        ListNode.print_list(expected_output_2)
        ListNode.print_list(actual_output_2)
        ListNode.print_list(expected_output_3)
        ListNode.print_list(actual_output_3)


if __name__=="__main__":
    main()