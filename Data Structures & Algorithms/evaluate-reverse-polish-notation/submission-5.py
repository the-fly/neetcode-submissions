class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            if(token in "+-*/"):
                right = numStack.pop()
                left = numStack.pop()
                if token == "+":
                    left = left + right
                if token == "-":
                    left = left - right
                if token == "*":
                    left = left * right
                if token == "/":
                    left = int(left/right)
                numStack.append(left)
            else:
                numStack.append(int(token))

        return numStack.pop()
                
        