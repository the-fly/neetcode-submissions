class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True
        for c in s:
            print(1, c)
            if c == "(" or c == '[' or c == '{':
                stack.append(c)
                print(2, stack)
            elif len(stack) == 0:
                print(3)
                return False
            elif c == ')':
                o = stack.pop()
                print(4, c, o)
                if not o == '(':
                    return False
            elif c == ']':
                o = stack.pop()
                print(5, c, o)
                if not o == '[':
                    return False
            elif c == '}':
                o = stack.pop()
                print(6, c, o)
                if not o == '{':
                    return False
        if not len(stack) == 0:
            print(7)
            return False
        return True