class Solution:
    def climbStairs(self, n: int) -> int:
        # to get to a step n, there are f(n-1) + f(n-2) ways of getting there
        # this is because you could either be 2 steps behind and take 2 steps, or be 1 step behind and take 1 step
        # edge case: 0 steps

        # add possible ways to the top in a list until the length of the list reaches n
        # each new step will be the value of the previous 2 steps

        # this is a O(n) time complexity because it only solves each step once up to n

        if n == 0 or n == 1:
            return 1

        if n == 2:
            return 2
        
        steps = [1, 2]

        while len(steps) < n:
            current = len(steps)

            steps.append(steps[current - 1] + steps[current - 2])

        return steps[n-1]
        
    
    # neetcode solution (this is better because it doesn't use up the O(n) memory):
    # only actually need 2 variables of memory which is O(1)
    
    class Solution:
        def climbStairs(self, n: int) -> int:
            if n <= 3:
                return n
            n1, n2 = 2, 3

            for i in range(4, n + 1):
                temp = n1 + n2
                n1 = n2
                n2 = temp
            return n2
    
    
    # basically same solution just written differently:
    
    class Solution:
        def climbStairs(self, n: int) -> int:
            n1, n2 = 1, 1
        
            for i in range(n-1):
                temp = n1 + n2
                n1 = n2
                n2 = temp
            
            return n2