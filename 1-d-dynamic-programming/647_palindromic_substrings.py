class Solution:
    def countSubstrings(self, s: str) -> int:
        # similar to longest palindromic substring
        # for each char, consider it as the middle point
        # move outwards with left and right pointers
        # also have to consider if it's an even palindrome
        # by checking if next character is the same char

        total = len(s)
        # every character is automatically a palindrome by itself

        for i in range(len(s)):
            l, r = i - 1, i + 1
            # left and right pointers for an odd length palindrome

            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            # left and right pointers for an even length palindrome

            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1

        return total

# neetcode solution:
# same concept as mine except he made a helper function
# he included the same index in his first call of countPali
# so that the individual chars are counted as a palindrome

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res