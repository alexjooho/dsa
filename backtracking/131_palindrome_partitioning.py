class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # brute force recursive backtracking problem
        # for each call, we will need the left pointer, current index, and current array of substrings
        # for each recursive call, make up to 4 types of calls:
        # 1. skip current letter and move to next index for next call
        # 2. add current letter to array by itself (only possible if left pointer is at current index)
        # 3. use left and right pointers from current - 1 and current + 1 and keep going until it reaches
            # the left pointer. if it fails before it reaches left pointer, don't make any call at all
            # only do this if current index is > left pointer
        # 4. check if previous letter is same as current, and use the two combined as the base of palindrome
            # and keep going until left pointer
            # only do this if current index is > left pointer
            # this is very similar to call 3

        # make sure to update left pointer each call if a substring was added to array
        # NOTE: be very careful about l, left, and right pointers for typos
        # NOTE: make sure to use an else statement for if l != idx
        
        # time complexity: O(n * 2^n) since for every index we either include it on its own or don't
        # and it takes O(n) to check if it's a palindrome

        res = []

        def backtrack(l, idx, cur):
            if idx >= len(s):
                if l >= len(s):
                    # if both the current index and left pointer are past the array
                    # append the substring array to result array
                    # if left is not past array, that means we couldn't find valid palindrome so return nothing
                    res.append(cur.copy())
                return

            backtrack(l, idx + 1, cur)
            # recursive call 1

            if l == idx:
                # if left pointer is at current index, then we can make call 2
                cur.append(s[l])
                backtrack(l + 1, idx + 1, cur)
                cur.pop()

            else:
                # if left pointer is before current index, then we can make call 3 and 4 possibly
                # need to include this ELSE part or else we would create duplicates because of the line
                # if left == l - 1, since that will always end up true if they started at same spot
                # and left was index - 1

                left, right = idx - 1, idx + 1
                while left >= l and right <= len(s) - 1:
                    # while left hasn't reached the left pointer yet and right hasn't passed the array
                    # keep going until palindrome is invalid
                    # if left is at l - 1 by the end of this loop, that means we have successfully found
                    # a palindrome that continues in our array
                    # otherwise, we don't make another recursive call

                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        break

                if left == l - 1:
                    # recursive call 3
                    # if left == l - 1, that means we can append the palindrome that we created
                    # and now both the left and current index pointers will be at r
                    cur.append(s[l:right])
                    # append s[l:right] since l is the starting index of palindrome and right is the index after
                    # the end of the palindrome, and it won't get included in the slice
                    backtrack(right, right, cur)
                    cur.pop()

                if s[idx - 1] == s[idx]:
                    # recursive call 4

                    left, right = idx - 2, idx + 1
                    while left >= l and right <= len(s) - 1:
                        if s[left] == s[right]:
                            left -= 1
                            right += 1
                        else:
                            break

                    if left == l - 1:
                        cur.append(s[l:right])
                        backtrack(right, right, cur)
                        cur.pop()

        backtrack(0, 0, [])
        return res
    
# neetcode solution:
# basically instead of having to go back and check if a left pointer is not at current index,
# he just keeps track of the current index, and iterates through entire remaining array (including current)
# to check if each left and right pointer creates a palindrome, and adds it to current array if it does
# this will always include itself, and it will also create another recursive decision tree for
# every other possible palindrome starting from the current index

# he uses a helper palindrome function to check if each possible string is a palindrome
# NOTE: BIGGEST DIFFERENCE FROM MY SOLUTION AND HIS IS THAT HE DOESN'T MOVE OUTWARDS FROM EACH LETTER
# AS IF IT WAS THE CENTER, AND INSTEAD SIMPLY MOVES RIGHT POINTER AND EXTENDS THE STRING AND CHECKS
# EACH TIME IF IT IS A PALINDROME

# a lot of palindrome questions will be better done by moving outwards from center, but in this case
# it causes you to enter many more recursive functions that may never be valid anyways

# time complexity: O(n * 2^n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    
# leetcode user's solution
# same as neetcode's but with using different style of coding for using current array

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        lst = []
        def palindrome(a):
            return a == a[::-1]
        def dfs(i,curr):
            if i == len(s):
                lst.append(curr)
                return 
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if palindrome(sol):
                    dfs(j+1, curr + [sol] )
            return 
        dfs(0,[])
        return lst