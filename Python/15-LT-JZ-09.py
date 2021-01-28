class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack2) == 0:
            if len(self.stack1) != 0:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            else:
                return -1
        return self.stack2.pop()