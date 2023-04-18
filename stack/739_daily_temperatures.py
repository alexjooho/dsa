class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack problem
        # monotonic decreasing stack
        # keep a stack of visited values that have not had a temperature higher than it yet
        # notice how the stack will always be in descending order since if there is a higher value,
        # then the previous values would have been removed already

        # for every value, if it is greater than the last value of the stack,
        # keep popping from stack until it is empty or it is no longer greater than last value
        # update the day values in the output array for the popped values
        # after, add to the stack

        # to know which index in result to update, every value in stack should also include its index

        # brute force solution would have been to just do O(n^2) and search through whole array each time
        # this solution's time complexity is O(2n) since each value can only be checked twice
        # since we only look at top value of stack and if it's greater, then we continue
        
        # O(n) time complexity and O(n) space complexity because of stack

        res = [0] * len(temperatures)

        stack = [] # pair: (temp, index)

        for i, val in enumerate(temperatures):
            if stack: # this line is actually not necessary
                # since we added the index to each value in stack, we can know which index in result to update
                while stack and val > stack[-1][0]:
                    # if the stack still has values and current val is greater than last value in stack
                    # then pop last value and update its position in results array
                    
                    index = stack.pop()[1]
                    res[index] = i - index
            stack.append((val, i))

        return res
    
# neetcode solution:
# basically the exact same solution!

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res