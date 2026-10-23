class MyQueue:

    def __init__(self):
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        self.left.append(x)

    def pop(self) -> int:
        if len(self.right) > 0:
            x = self.right.pop()
            return x
        else:
            while len(self.left) > 0:
                x = self.left.pop()
                self.right.append(x)
            x = self.right.pop()
            return x

    def peek(self) -> int:
        if len(self.right) > 0:
            return self.right[-1]
        else:
            return self.left[0]
        

    def empty(self) -> bool:
        return not ((len(self.left) > 0) or (len(self.right) > 0))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()