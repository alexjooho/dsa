class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep stack of values
        # whenever an operator is reached, apply it to the 2 last values of the stack
        # and push the new value into the stack

        # time complexity and space complexity: O(n)
        # NOTE: The trick is to know that every operator is done on the previous 2 values
        # if there are more operators, those have to be done first

        values = []

        for token in tokens:
            if token == '+':
                val_2 = values.pop()
                val_1 = values.pop()

                new_val = val_1 + val_2
                values.append(new_val)

            elif token == '-':
                val_2 = values.pop()
                val_1 = values.pop()

                new_val = val_1 - val_2
                values.append(new_val)

            elif token == '*':
                val_2 = values.pop()
                val_1 = values.pop()

                new_val = val_1 * val_2
                values.append(new_val)

            elif token == '/':
                val_2 = values.pop()
                val_1 = values.pop()

                new_val = int(val_1 / val_2)
                # NOTE: have to do int of this value instead of using // since // rounds down
                # instead of towards 0
                values.append(new_val)
            
            else:
                values.append(int(token))
                # make sure to do int instead of float since test outputs expect int

        return values[0]
        # there is always a valid solution, so the only value left in the values stack will be the answer
    
# neetcode solution:
# same exact solution, just some cleaner code

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]