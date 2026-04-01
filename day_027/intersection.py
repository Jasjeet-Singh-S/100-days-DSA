# https://www.geeksforgeeks.org/dsa/write-a-function-to-get-the-intersection-point-of-two-linked-lists/

class Solution:
    def intersectPoint(self, head1, head2):
        seen = set()
        while head1 != None:
            seen.add(head1)
            head1 = head1.next
        while head2 != None:
            if head2 in seen:
                return head2
            else:
                head2 = head2.next