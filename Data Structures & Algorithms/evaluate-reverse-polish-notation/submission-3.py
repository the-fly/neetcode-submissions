class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for i in range(0, len(tokens)):
            if(tokens[i] in "+-*/"):
                right = numStack.pop()
                left = numStack.pop()
                if tokens[i] == "+":
                    left = left + right
                if tokens[i] == "-":
                    left = left - right
                if tokens[i] == "*":
                    left = left * right
                if tokens[i] == "/":
                    left = int(left/right)
                numStack.append(left)
            else:
                numStack.append(int(tokens[i]))

        return numStack.pop()
                
        