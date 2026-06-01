class MinStack:

    values = []

    def __init__(self):
        self.values = []
        

    def push(self, val: int) -> None:
        self.values.append(val)
        

    def pop(self) -> None:
        self.values.pop()
        

    def top(self) -> int:
        return self.values[-1]

        

    def getMin(self) -> int:
        if len(self.values) == 0:
            return None
        minimum = self.values[0]

        for value in self.values:
            minimum = min(value, minimum)
        return minimum

        
