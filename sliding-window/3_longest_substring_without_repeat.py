class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # create a dictionary to make sure there are no repeated characters (this will take up O(n) memory)
            # dictionary will have key of character and value of index
        # iterate through list and check if current length is max length
        # every time there is a repeated character, move the left pointer to repeated character's original index + 1
            # that key's value in the dictionary will be the current index
        # edge case: empty string

        # NOTE: when seeing a duplicate, can ignore it if its previous index is before l (since that's not in our current substring)

        if len(s) == 0:
            return 0

        max_length = 1
        # have to do max_length = 1 instead of 0 since edge case "bbb" would be 0 if 0 was used
        seen = {s[0]: 0}
        # need to use dictionary and keep track of index to update left pointer
        l = 0

        for r in range(1, len(s)):

            if s[r] in seen:
                if seen[s[r]] < l:
                    # we don't care about having a duplicate if its before the left pointer of current substring
                    # so we just update the index of that character
                    seen[s[r]] = r
                    max_length = max(max_length, (r - l + 1))
                else:
                    l = seen[s[r]] + 1
                    seen[s[r]] = r
            else:
                seen[s[r]] = r
                max_length = max(max_length, (r - l + 1))

        return max_length
    
# Neetcode solution using a set:
# same concept, but instead of using a dictionary to know the exact index to change pointer to,
# he keeps removing items from the set until the duplicate is removed, and keeps adding 1 to l
# to adjust the pointer to the right spot
# this is probably less efficient but it gets rid of the issue of having random keys in dictionary
# that aren't relevant to current substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res