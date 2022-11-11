class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointers to start from the beginning and end to confirm each character matches
        # skip non-alphanumeric characters, and keep going until there is mismatch or the pointers reach each other
        # always make sure to convert characters into lowercase

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left = left + 1
            elif not s[right].isalnum():
                right = right - 1
            elif s[left].lower() == s[right].lower():
                left = left + 1
                right = right - 1
            else:
                return False

        return True

# neetcode solution:
# Creates its own alphnum function using ord()
# using an inner while loop instead of doing multiple if statements

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l < r:
#             while l < r and not self.alphanum(s[l]):
#                 l += 1
#             while l < r and not self.alphanum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

#     # Could write own alpha-numeric function
#     def alphanum(self, c):
#         return (
#             ord("A") <= ord(c) <= ord("Z")
#             or ord("a") <= ord(c) <= ord("z")
#             or ord("0") <= ord(c) <= ord("9")
#         )


# alternative solution would be to create a new string with non-alphanumeric characters taken out
# then compare it with its reverse to see if they are the same
# but this takes up more memory

# new_str = ""

# for c in s:
#     if c.isalnum():
#         new_str += c.lower()
#     return new_str == new_str[::-1]ß