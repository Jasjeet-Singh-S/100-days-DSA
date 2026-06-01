import operator
class Solution:
    def evaluatePostfix(self, arr):
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
            "^": operator.pow
        }
        stack = []
        for i in range(len(arr)):
            if arr[i] not in ops:
                stack.append(arr[i])
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = ops[arr[i]](float(operand_1), float(operand_2))
                stack.append(result)
        return int(stack.pop())


if __name__=="__main__":
    arr = ["2", "3", "1", "*", "+", "9", "-"]
    sol = Solution()
    if sol.evaluatePostfix(arr)==-4:
        print("pass")
    else:
        print("fail")
        print(sol.evaluatePostfix(arr))