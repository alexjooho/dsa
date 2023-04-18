class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # brute force backtracking method:
        # keep a results array that we add every possible combination of parentheses to

        # keep track of how many left parts and right parts we have available
        # start with nothing, and then recursively call a function with the addition of
        # 2 choices: "(", ")"
        # originally I put "()" as a choice as well, but it's redundant
        # make a recursive call with all possible choices
        # only insert ")" if there are more starting points used than end points
        # only insert "(" if there are starting points left
        
        # keep doing this until all of the beginning and end parentheses are used and add
        # to the results array

        # keep track of seen recursive calls so they are not repeated
        # NOTE: this is actually not needed since there won't be repeats since they take different paths

        res = []
        seen = set()

        def dfs(cur, start, end):
            # cur is the current string
            # start is the number of starting parentheses left
            # end is the number of ending parentheses left

            if cur in seen:
                return

            seen.add(cur)
            # have to put this before the next part where we add to results
            # so that same result isn't added multiple times

            if start == 0 and end == 0:
                res.append(cur)
                return

            if start != 0:
                # THIS IS THE PART I WAS STUCK ON
                # NEED TO REMEMBER THAT YOU CAN ONLY ADD A STARTING PARENTHESIS
                # IF NOT ALL OF THEM ARE ALREADY USED
                # I DIDN'T ADD THIS LINE BEFORE AND IT LED TO AN ENDLESS RECURSIVE STACK!!!

                dfs(cur + '(', start - 1, end)

            if start < end:
                # only insert an end part if there are more starting points used so far
                dfs(cur + ')', start, end - 1)

        dfs('', n, n)

        return res
    
    
# neetcode solution:
# similar solution but uses an array instead of a string for the current value
# only add an open parenthesis if open < n
# only add a closing parenthesis if closed < open
# valid if open == closed == n

# NOTE: we don't need a seen hashset since there are only 2 options
# so each recursive call thereafter will never equal the same one as a previous call!!!

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                # have to pop after every call since we are using a singular stack for recursive function calls
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
