class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking
        # keep a variable exists that starts as false and will be turned true if the word is found
        # search through grid for the starting letter
        # for every starting letter, check each following letter in the word with its left, right, top, bottom indexes
        # to see if that letter exists. if it doesn't exist, stop. if it does exist, continue to next letter
        # keep track of all indexes already searched in a seen set using tuples

        # NOTE: time complexity: O(n * m * dfs) = O(n * m * 4^n) where the second n is the length of the word
        # this is because you traverse the entire grid and for each start letter, could go 4 directions
        # n times where n is the length of the word

        exists = False

        def dfs(i, m, n, seen):
            if i >= len(word):
                nonlocal exists
                # this is needed to make changes to variable outside of current nested function
                exists = True
                return
            if not n == 0:
                # left
                if board[m][n - 1] == word[i]:
                    if (m, n - 1) not in seen:
                        seen.add((m, n - 1))
                        dfs(i + 1, m, n - 1, seen)
                        seen.remove((m, n - 1))
                        # this is so that we can use the same seen set for other recursive functions afterwards
                        # NOTE: CAN'T USE .POP() SINCE IT REMOVES A RANDOM ITEM FROM SET (pop could be used for lists though)
            if not n >= len(board[m]) - 1:
                # right
                if board[m][n + 1] == word[i]:
                    if (m, n + 1) not in seen:
                        seen.add((m, n + 1))
                        dfs(i + 1, m, n + 1, seen)
                        seen.remove((m, n + 1))
            if not m == 0:
                # up
                if board[m - 1][n] == word[i]:
                    if (m - 1, n) not in seen:
                        seen.add((m - 1, n))
                        dfs(i + 1, m - 1, n, seen)
                        seen.remove((m - 1, n))
            if not m >= len(board) - 1:
                # down
                if board[m + 1][n] == word[i]:
                    if (m + 1, n) not in seen:
                        seen.add((m + 1, n))
                        dfs(i + 1, m + 1, n, seen)
                        seen.remove((m + 1, n))

        first = word[0]

        for m, row in enumerate(board):
            for n, column in enumerate(row):
                if column == first:
                    # whenever the starting point is found, recursively search for word
                    seen = set()
                    seen.add((m, n))
                    dfs(1, m, n, seen)
                    seen.remove((m, n))
                    # HAVE TO INCLUDE STARTING POINT IN SEEN SET

        return exists

# neetcode solution:
# without reversing the word if frequency of first letter is more than last letter, time limit will be exceeded
# my solution is faster if you don't do the reversing part!


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        # this is confusing, don't worry about it too much
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # O(n * m * 4^n)
