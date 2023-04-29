class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # very similar to combination sum question
        # recursive backtracking
        # note the constraint that all numbers of nums are unique, so we don't have to worry about duplicates
        # for each number, recursively call function adding the number and not adding the number
            # this way, we will not have any duplicate subsets
        # keep a current array so that we can add to the array, and keep a pointer for which index we are at
        # pop from current after calling function

        res = []

        def backtrack(cur, pointer):
            if pointer == len(nums):
                # if we have exhausted the list, add to the result and exit function
                res.append(cur.copy())
                # NOTE: MAKE SURE TO APPEND A COPY OF THE ARRAY SINCE THE REAL ONE WILL ALWAYS
                # END UP BEING [] AT THE END
                return
            
            # append current number to cur array and call backtrack. pop afterwards
            cur.append(nums[pointer])
            backtrack(cur, pointer + 1)
            cur.pop()

            backtrack(cur, pointer + 1)
            # call function without adding current number

        backtrack([], 0)

        return res
    
# neetcode solution:
# same as mine basically

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res