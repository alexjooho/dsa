class MinStack:
    # difficult part is the getMin in O(1) time
    # to solve this, we have to create another "min stack"
    # this keeps track of the minimum value at any given node/index
    # so that if a value is popped that was the minimum, the next last value in the minstack
    # will hold the new min value

    # NOTE: instructions say that pop, top, and getMin will only be called on non-empty stacks
    # so we don't have to worry about those edge cases

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.minStack[-1] if self.minStack else val, val)
        # if the minstack is empty, then we just get the min between val and val
        self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        # have to pop from the minstack as well
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # this is not meant to actually pop the minimum value
        # just wants to look at it
        return self.minStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.