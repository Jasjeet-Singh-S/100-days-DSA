# https://leetcode.com/problems/climbing-stairs/
# explanation here https://youtu.be/Y0lT9Fck7qI?si=S4d6ubVoIV8g5-z3 basically we need to solve the fibonacci problem 

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp 

        return one