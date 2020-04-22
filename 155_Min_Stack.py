class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        stack_list = [ ]
        self.stack = stack_list
        

    def push(self, x: int) -> None:
        self.stack = [x] + self.stack

    def pop(self) -> None:
        self.stack = self.stack[1:]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()