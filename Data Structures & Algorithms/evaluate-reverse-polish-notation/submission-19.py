class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif s == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif s == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
            elif s == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            else:
                stack.append(int(s))
        return stack[-1]