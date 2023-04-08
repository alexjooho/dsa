class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dynamic programming with longest common subsequence type
        # create a 2-d array
            # extra row and extra column, so that we have a starting point of 0
        # since letters can be skipped (subsequence), have to keep track of
        # current longest length at each index
        # we have to check every letter with every letter of both words
        # as we traverse the 2-d array, if the letters are the same, add
        # + 1 to the cell to the top and left of it (diagonally top-left)
        # since this represents the longest length at the point of 1 letter
        # behind for both words (so that there's no repeats)

        # if the letters are not the same:
        # the cell will be the max of the cell above it and the cell to the left of it
        # since this is the longest current length before this cell

        # time complexity: O(n1 * n2), space complexity: O(n1 * n2)

        len_1, len_2 = len(text1), len(text2)

        dp = [[0] * (len_2 + 1) for i in range(len_1 + 1)]
        # creating 2-d array with all 0's
        # text1 will represent rows (left side of 2-d array)
        # text2 will represent columns (top side of 2-d array)

        for i in range(1, len_1 + 1):
            # rows
            for j in range(1, len_2 + 1):
                # columns
                if text1[i - 1] == text2[j - 1]:
                    # have to do - 1 since we are starting from 1
                    # if they are equal, add 1 to longest streak of diagonal top-left cell
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    # if the letters are not the same, get max of top and left cell
                
        return dp[-1][-1]
        # last cell will always have the longest subsequence length
        
# neetcode solution:
# same concept but he did it starting from the end instead of the beginning
# more "bottom-up-like" solution than mine, because mine is starting from beginning like
# a top-down solution

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
    
# recursive solution:
# if char are equal, find lcs of remaining string of both words. otherwise, find the max of the 
# recursive lcs of first string and remaining string of second string starting from next letter
# AND vice versa for other string.
# cache results so they are not repeated
# when reaching the beginning of 2-d cache, return 0

# A Top-Down DP implementation of LCS problem
 
# Returns length of LCS for X[0..m-1], Y[0..n-1]
def lcs(X, Y, m, n, dp):
 
    if (m == 0 or n == 0):
        return 0
 
    if (dp[m][n] != -1):
        return dp[m][n]
 
    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m][n]
 
    dp[m][n] = max(lcs(X, Y, m, n - 1, dp),lcs(X, Y, m - 1, n, dp))
    return dp[m][n]
 
# Driver code
 
X = "AGGTAB"
Y = "GXTXAYB"

m = len(X)
n = len(Y)
dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]
 
print(f"Length of LCS is {lcs(X, Y, m, n, dp)}")