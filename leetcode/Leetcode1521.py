
class CQueue:

    def __init__(self):
        self.topStack = []
        self.bottomStack = []

    def appendTail(self, value: int) -> None:
        self.bottomStack.append(value)

    def deleteHead(self) -> int:
        if len(self.topStack) != 0:
            return self.topStack.pop()
        if len(self.bottomStack) == 0:
            return -1
        for i in range(len(self.bottomStack)):
            self.topStack.append(self.bottomStack.pop())
        return self.topStack.pop()
