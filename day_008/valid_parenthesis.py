class Solution:
    opening_parenthesis = ["(", "{", "["]
    closing_parenthesis = [")", "}", "]"]

    def isValid(self, s: str) -> bool:
        stack = Stack()
        for parenthesis in s:
            if parenthesis in self.opening_parenthesis:
                stack.push(parenthesis)
            if parenthesis in self.closing_parenthesis:
                if stack.is_empty():
                    return False
                if stack.top()==self.opening_parenthesis[self.closing_parenthesis.index(parenthesis)]:
                    stack.pop()
                else:
                    return False
        if stack.is_empty():
            return True
        else:
            return False

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items)==0
    
def main():
    s_1 = "()"
    expected_output_1 = True
    s_2 = "()[]{}"
    expected_output_2 = True
    s_3 = "(]"
    expected_output_3 = False
    s_4 = "([])"
    expected_output_4 = True
    s_5 = "([)]"
    expected_output_5 = False

    solution = Solution()

    actual_output_1 = solution.isValid(s_1)
    actual_output_2 = solution.isValid(s_2)
    actual_output_3 = solution.isValid(s_3)
    actual_output_4 = solution.isValid(s_4)
    actual_output_5 = solution.isValid(s_5)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2 and actual_output_3==expected_output_3
       and actual_output_4==expected_output_4 and actual_output_5==expected_output_5):
        print("pass")
    else:
        print("fail")
        print(actual_output_1, actual_output_2, actual_output_3, actual_output_4, actual_output_5)

if __name__=="__main__":
    main()