class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            if(token in "+-*/"):
                right = numStack.pop()
                left = numStack.pop()
                if token == "+":
                    numStack.append(left + right)
                if token == "-":
                    numStack.append(left - right)
                if token == "*":
                    numStack.append(left * right)
                if token == "/":
                    numStack.append(int(left/right))
            else:
                numStack.append(int(token))

        return numStack.pop()
                
        