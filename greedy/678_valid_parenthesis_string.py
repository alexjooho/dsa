class Solution:
    def checkValidString(self, s: str) -> bool:
        # most obvious approach would be to do dp solution with 2-D array which is O(n^2)
        # straight recursive solution would be O(3^n), but memoization would be O(n^2)
        # BEST SOLUTION IMO IS THE LAST ONE (THE STACK SOLUTION)

        # greedy approach is less intuitive but much better (O(n) instead of O(n^2))
        # keep track of left open parentheses. if it ever becomes negative, then it is not valid
            # if it ends without being 0, then it is not valid

        # greedy solution requires keeping track of leftMin and leftMax
        # we do this so we can see the min and max left parentheses as we go through the string and for
        # every "*", we do both options
        # we need the max left so that if it ever becomes -1, we know that we have an invalid solution

        # if we end up with a min left that is 0, then we have a valid solution
        # NOTE: WE ONLY NEED TO KEEP TRACK OF LEFT PARENTHESES

        min_left, max_left = 0, 0

        for c in s:
            if c == '(':
                min_left += 1
                max_left += 1

            elif c == ')':
                min_left -= 1
                max_left -= 1

            else:
                # if we get a '*' then we have to do both options
                min_left -= 1
                # technically we shouldn't do this if min_left is already at 0, but it won't matter in the end
                # since we reset min_left to 0 if it is negative anyways
                max_left += 1

            if max_left < 0:
                return False
            if min_left < 0:
                # if min_left is ever negative and max_left is still >= 0, then we reset min_left to 0
                # required because -> s = ( * ) (
                min_left = 0

        return min_left == 0
    
# neetcode DP solution O(n^2):
# this solution is O(n^2) since for each n, you have to do another 3n if it is a '*'
# O(3n^2) simplifies to O(n^2)

# Dynamic Programming: O(n^2)
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s), 0): True}  # key=(i, leftCount) -> isValid

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]

            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = (
                    dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left)
                )
            return dp[(i, left)]

        return dfs(0, 0)
    
# leetcode user stack solution O(n):
# basically keep a stack of left parentheses and a stack of *'s
# if a ')' is seen, then pop from '(' stack if possible
    # if not possible, pop a *. if neither is possible, return false
# if a '(' is seen, add its index to stack
# if a * is seen, add its index to stack

# after iterating, we make sure we can get rid of all left parentheses by popping from both left
# stack and the star stack, and making sure each pop has the index of * being > than left index
# since we are making the * a right parenthesis.
# NOTE: THIS IS WHY WE ADD THE INDEX OF THE PARENTHESES TO THE STACK!

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # store the indices of '('
        stk = []
        
        # store the indices of '*'
        star = []
        
        
        for idx, char in enumerate(s):
            
            if char == '(':
                stk.append( idx )
                
            elif char == ')':
                
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False
            
            else:
                star.append( idx )
        
        
        # cancel ( and * with valid positions, i.e., '(' must be on the left hand side of '*'
        while stk and star:
            if stk[-1] > star[-1]:
                return False
        
            stk.pop()
            star.pop()
        
        
        # Accept when stack is empty, which means all braces are paired
        # Reject, otherwise.
        return len(stk) == 0