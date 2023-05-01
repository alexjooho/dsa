class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # simple backtracking recursive problem
        # for each call, call the recursive function with the addition of each of the possible letters
        # for the number at the index
        # remember to pop after the recursive call
        # keep a hashmap of all the numbers 2-9 and their respective letters

        # since I usually don't use this method of adding to the cur array without doing
        # append and pop, I tried doing cur + [x] for this problem

        # time complexity: O(n * 4^n)
            # for each number, there are up to 4 different possible letters
            # and for each time we add to the current string, it can take up to O(n)

        # EDGE CASE: digits is an empty string
        if not digits:
            return []

        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # NOTE: digits is a string, so all the keys in letters has to be a string number
        res = []

        def dfs(i, cur):
            if i >= len(digits):
                res.append(cur)
                return

            for letter in letters[digits[i]]:
                dfs(i + 1, cur + letter)

        dfs(0, '')
        return res
    
# neetcode solution:
# same as mine

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res