class MinStack:

    def __init__(self):
        self.stack = []
        self.n = 0
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
            self.n+=1
        else:
            self.stack.append((val,min(self.stack[-1][1],val)))
    def pop(self) -> None:
        r = self.stack.pop()
        self.n-=1
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
        
