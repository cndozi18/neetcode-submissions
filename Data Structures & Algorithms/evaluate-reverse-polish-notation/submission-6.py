from collections import deque 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])
        stack = deque()
        for token in tokens:
            if token in ops:
                arg_2 = stack.popleft()
                arg_1 = stack.popleft()
                res = 0
                match(token):
                    case '+':
                        res = arg_1 + arg_2
                    case '-':
                        res = arg_1 - arg_2
                    case '*':
                        res = arg_1 * arg_2
                    case '/':
                        res = int(float(arg_1) / arg_2)
                stack.appendleft(res)
            else:
                stack.appendleft(int(token))
        return stack[0]

