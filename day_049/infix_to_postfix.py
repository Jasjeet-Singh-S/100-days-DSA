# https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
class Solution:
    def precidence(self, op):
        if op=="^":
            return 3
        elif op=="/" or op=="*":
            return 2
        else:  # op=="+" or op=="-":
            return 1
    
    def IsRightAssociative(self, op):
        return op=="^"

    def infixtoPostfix(self, string):
        stack = []
        result = []

        for char in string:
            # if it is operand, then add to result
            if char not in "+-*/^()":
                result.append(char)
            
            # if "(", push to stack
            elif char=="(":
                stack.append(char)
            
            # if ")", pop stack and append to result until "(" is found
            elif char==")":
                TopOfStack = stack.pop()
                while TopOfStack!="(":
                    result.append(TopOfStack)
                    TopOfStack = stack.pop()
            
            # if operator
            else:
                while stack and stack[-1] != '(' and self.precidence(stack[-1])>=self.precidence(char) and not self.IsRightAssociative(char):  # the last associativity condition is pretty cool, check description.md to see why
                    result.append(stack.pop())
                stack.append(char)
        
        # pop the remaining operators
        while stack:
            result.append(stack.pop())

        return "".join(result)


if __name__=="__main__":
    sol = Solution()
    input = "a*(b+c)/d"
    expected_output = "abc+*d/"
    actual_output = sol.infixtoPostfix(input)
    if expected_output==actual_output:
        print("pass")
    else:
        print("fail")
        print(expected_output)
        print(actual_output)