# https://www.geeksforgeeks.org/problems/queue-reversal/1
class Solution:
    def reverseQueue(self, q):
        stack = []
        while q:
            stack.append(q[0])
            q.popleft()
        while stack:
            q.append(stack.pop())