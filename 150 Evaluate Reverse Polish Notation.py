'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = ['+', '-', '*', '/']
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                while len(stack)<2:
                    return None
                if i=='+':
                    stack[-2] = stack[-2]+stack[-1]
                    stack.pop()
                elif i=='-':
                    stack[-2] = stack[-2]-stack[-1]
                    stack.pop()
                elif i=='*':
                    stack[-2] = stack[-2]*stack[-1]
                    stack.pop()
                elif i=='/':
                    stack[-2] = int(float(stack[-2])/stack[-1])
                    stack.pop()
        return int(stack.pop())