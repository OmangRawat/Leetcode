"""

---> Implement Queue using Stacks
---> Easy

"""


class MyQueue:

    def __init__(self):
        self.for_push = []
        self.for_pop = []

    def push(self, x: int) -> None:
        self.for_push.append(x)

    def pop(self):
        self.peek()
        if not len(self.for_pop):
            return "Queue Empty"
        return self.for_pop.pop()

    def peek(self):
        if not self.for_pop:
            while self.for_push:
                self.for_pop.append(self.for_push.pop())
        if not len(self.for_pop):
            return "Queue Empty"
        return self.for_pop[-1]

    def empty(self) -> bool:
        return not self.for_push and not self.for_pop


obj = MyQueue()
print(obj.empty())
print(obj.pop())
print(obj.peek())
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.peek())


"""

Approach 1:
Using 2 stack one for input and other for output

Approach 2:
Use 1 stack and a variable for tracking index. Input at last and output from first

"""
