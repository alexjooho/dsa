class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O(26*n) solution:
        # sliding window
        # keep a hash map of all letters and their count
        # check if the max letter's count does not satisfy -> length - max < k
        # if it doesn't, move the left pointer and update counter hash map until its satisfied
        # keep updating length as you traverse along the list

        counter = {}
        max_length = 0
        l = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length
    
# Neetcode O(n) solution:
# this solution is better because it doesn't have to keep searching through the entire dictionary for a max
# it simply keeps the max value, and if a value that is encountered has a dictionary value
# that is greater, it will update the max
# it doesn't matter if it is overestimating it (e.g. when that character is removed in line 44) 
# since at one point, that max was true
# and the result max length can never increase again until the max is increased again

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res