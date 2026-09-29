# https://www.geeksforgeeks.org/problems/set-bits0143/1

# class Solution:
#     def setBits(self, n):
#         return bin(n).count('1')
# this is a working solution, O(1) time and space, but idk if this will be allowed in interview

# https://youtu.be/e0sVe4-JJJI?si=NmNT7rtOPmEeiKE8 watch this to understand
class Solution:
    def setBits(self, n):
        count = 0
        while(n):
            n = n & n-1
            count += 1
        return count