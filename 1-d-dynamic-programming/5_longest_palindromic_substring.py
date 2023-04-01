class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for every character, have a left and right pointer that start from char left and char right from it
        # if they are the same character, add to total and update result string if max increased
        # for edge case of a string with 2 same chars or if there are 2 same chars next to each other in a string,
        # check next letter to see if its the same as current one, and if it is, then you have to do a loop
        # that starts from char to left and right of the 2 chars too

        # time complexity: O(n^2) since for every char, it needs to check every other char
        # technically O(2n^2) since we do it twice if the next character is the same

        if len(s) == 1:
            return s

        largest = 0
        res = ""

        for i in range(len(s) - 1):
            # one less than end because we want to keep checking if there are two same chars next to each other
            # also if the last char was part of a palindrome, it would've already been checked

            total = 1
            l, r = i - 1, i + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    total += 2
                    l -= 1
                    r += 1
                else:
                    break
            
            if total > largest:
                largest = total
                res = s[l+1:r]

            if s[i+1] == s[i]:
                # another loop if there are 2 same chars next to each other
                total = 2
                l, r = i - 1, i + 2
                # have to do i + 2 for r because i + 1 is the same char and we don't want to re-check it
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        total += 2
                        l -= 1
                        r += 1
                    else:
                        break
                
                if total > largest:
                    largest = total
                    res = s[l+1:r]

        return res
    
# neetcode solution:
# same concept as my solution
# instead of using a total, just calculated r - l + 1
# had the left and right pointers start at same spot or on spot apart depending on if
# he was checking for odd or even length palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res