# neetcode solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking problem using recursive DFS (decision tree)
        # MOST IMPORTANT NOTE: TO AVOID DUPLICATE COMBINATIONS, EACH NODE GOES THROUGH 2 RECURSIVE DFS
        # ONE THAT CAN ADD THE SAME VALUE AGAIN (pointer stays the same) AND ONE THAT CAN'T (pointer goes up by one)
        # this will prevent any duplicates since each dfs will go through all possibilities with that multiple of the same
        # number and the same combination can never be seen again
        # NOTE: if this was a permutation (order matters) instead of a combination, could just go down each branch normally

        # use a pointer starting from left side that tells you which numbers you can add
        # base case is an empty list that can't add any values
        # time complexity is O(2^(t/smallest candidate)) where t is the target value since we are making two decisions at every node,
        # if 1 is a candidate, then it could be a max of 2^t time complexity
        # space complexity is O(t), since max space is the value of target divided by greatest value in list
        # NOTE: this recursive function gets rid of the need for using a ton of space with multiple lists by popping values each time

        res = []

        def dfs(i, cur, total):
            # i is the pointer, cur is the current list of candidates added, and total is the sum
            if total == target:
                # base case
                res.append(cur.copy())
                # have to do cur.copy() since we are going to continue to use this variable/list when we do other combinations recursively
                # this is to save space instead of having to create a new list each time
                # if we didn't want to do this, we could simply make copies or do cur + [candidates[i]] each time we call a function to make a new copy
                return
            if i >= len(candidates) or total > target:
                return
            # need the returns to prevent the recursive function from being called again!

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # this is the first recursive dfs that can add the same candidate

            cur.pop()
            # this is to get rid of the last value before recursively calling next function
            dfs(i + 1, cur, total)
            # this is the second recursive dfs that can not add the same candidate, and must move on to the next one

        dfs(0, [], 0)

        return res
