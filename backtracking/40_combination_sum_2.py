class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking recursive problem
        # similar to combination sum 1, but you can't repeat the same number
        # there are duplicates in the candidates array, so to avoid duplicate combinations,
        # we will have 2 calls:
        # 1. add candidate and move index + 1
        # 2. don't add any more of the candidate number and move to next index that is different number
        # since the array is not sorted for us, we need to sort it beforehand

        # time complexity: O(n * 2^n) since for each candidate, can include or not include
        # and for each subset, it could be up to length n

        res = []
        candidates.sort()
        # have to sort so that we don't repeat the same number in the call where we don't add it

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(candidates):
                return

            # recursive call using this number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            
            # recursive call not adding any more of this number
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
    
# neetcode solution:
# same general concept of either adding the number or not adding it again at all
# but he wrote the code differently
# basically his solution will go through all the possible dfs starting at the index each time
# by iterating through entire remaining list
# my solution simply chooses to add current index or not add any of the same numbers
# I prefer my solution since it is easier to remember and splits up the problem nicely

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res
