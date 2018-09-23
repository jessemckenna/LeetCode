'''
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minIdxStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        stack = self.stack
        minIdxStack = self.minIdxStack

        stack.append(x)
        if len(minIdxStack) == 0 or x < stack[minIdxStack[len(minIdxStack) - 1]]:
            minIdxStack.append(len(stack) - 1)

    def pop(self):
        """
        :rtype: void
        """
        stack = self.stack
        minIdxStack = self.minIdxStack

        stack.pop()
        while len(minIdxStack) > 0 and minIdxStack[len(minIdxStack) - 1] >= len(stack):
            minIdxStack.pop()

    def top(self):
        """
        :rtype: int
        """
        stack = self.stack

        return stack[len(stack) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        stack = self.stack
        minIdxStack = self.minIdxStack

        return stack[minIdxStack[len(minIdxStack) - 1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()