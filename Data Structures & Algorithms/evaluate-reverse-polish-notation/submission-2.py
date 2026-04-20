class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res =""
        stack=[]
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                a = int(a);b = int(b)
                if i == "+":
                    stack.append(a + b)
                elif i== "-":
                    stack.append(a - b)
                elif i== "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]
