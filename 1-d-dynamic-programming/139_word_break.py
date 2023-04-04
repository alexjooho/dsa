class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming recursive solution (kind of brute force)
        # for a starting and ending point of string:
            # iterate through wordDict and if a word
            # is within the string
            # recursively call the function with new start and end point
            # with the part of the string after the word was used
            # if a word is not within the start/end point of string, move
            # end point by one
        # create a seen set to cache start/end point strings
        # don't need a seen set for the words since they can be used
        # multiple times

        # time complexity: O(n^3 * w)
        # since we loop through string and every possible substring needs to check each word
        # NOTE: INSTEAD OF CHECKING EVERY SUBSTRING, WE COULD SIMPLY CHECK IF STARTING POINT
        # HAS A WORD THAT IS A PREFIX OF IT, WHICH WOULD MAKE THIS O(N^2 * W)
        # space complexity: O(n^2)
        # since every possible substring with l and r points could be in set

        seen_cache = set()

        def dfs(l, r):
            if (l, r) in seen_cache:
                return False

            if l == len(s):
                # this will happen if string finished and both l and r == len(s)
                return True

            if r == len(s):
                # since l != len(s), this means that the string simply finished
                return False

            cur = s[l: r + 1]
            seen_cache.add((l, r))
            # can't do .add(cur) since the current substring
            # could have already been seen, but it might also be in
            # a different area of the string
            # instead, we have to use a tuple with the left and right pointers
            # e.g. applepenapple

            for word in wordDict:
                # instead, could just do: if cur in wordDict and do the if dfs if its true
                if word == cur:
                    if dfs(r + 1, r + 1):
                        # if this recursive call finishes, return True
                        return True

            # if no word usages finished the recursive loop and finished
            # creating the string with words, then move right pointer to the
            # right one space

            return dfs(l, r + 1)

        return dfs(0, 0)

# recursive solution with checking prefixes instead of checking every start and end position:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        seen_cache = set()

        def dfs(start):
            if start in seen_cache:
                return False

            if start == len(s):
                # this will happen if string finished
                return True

            cur = s[start: ]
            seen_cache.add(start)

            for word in wordDict:
                if cur.startswith(word):
                    if dfs(start + len(word)):
                        return True
            return False

        return dfs(0)

# neetcode solution:
# instead of going through each possible substring and seeing if its a word,
# loop through the words and see if any of them are a prefix of the word
# therefore, time complexity becomes O(n^2 * w) instead of O(n^3 * w)
    # because we are only checking for prefixes and not going through
    # extra loops for prefix lengths that don't exist
# only need one pointer since we are checking for prefixes
# going to use bottom up dp approach
# once we reach end of string, return True
# use a cache array 1-d

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # start from end of string and keep a 1-d array
        # array has an extra index at the end because the end of the string is True
        # work backwards, and for each index, see if a word matches the starting
        # point of it, and if the ending point of adding the word's length
        # is true, then make this index true too since that means they connect
        # return dp[0] since if its true, that means it connected to end of str

        # NOTE: COULD ALSO DO THIS STARTING FROM THE BEGINNING OF THE STRING

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                    # the first part of "and" is just to make sure the word
                    # is not too big to be compared with string
                    # this prevents errors for indexes out of range
                if dp[i]:
                    break
                    # if it is true, then we can go to next (left) index
                    # since we don't need to re-confirm that this index
                    # is valid

        return dp[0]

# my solution using dp that starts from start of the string:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top-down dp solution

        dp = [False] * (len(s) + 1)
        # need an extra index to represent the end of string to check if true
        dp[0] = True

        for i, val in enumerate(dp):
            if val:
                # if current index is true, it means that there is a connection
                # to it from the start of the word
                cur = s[i: ]
                for word in wordDict:
                    if cur.startswith(word):
                        dp[i + len(word)] = True

        return dp[-1]