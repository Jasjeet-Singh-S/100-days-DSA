# https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
class Solution:
    def reverseFirstK(self, q, k):
        stack = []
        if k>len(q):
            return q
        for _ in range(k):
            stack.append(q[0])
            q.popleft()
        for i in range(k):
            q.insert(i, stack.pop())
                
        return q