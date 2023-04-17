class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a hashmap of letters in s1 and their frequencies
        # create an empty defaultdict for s2
        # if a character is not in string 1, we clear dict2 and move on
        # if a character is in string 1:
            # if the character is in dict2 with too high freq, 
            # then we have to remove chars from dict until the same character is removed
            # if the character is not in set2, we can just add it

        # sliding window

        # time complexity: O(26 * n) -> O(n)
            # the 26 comes from there being 26 letters, and having to check at every window if all
            # the hashmap frequencies are the same
        # space complexity: O(n + m)

        s1_frequency = collections.defaultdict(int)
        s2_frequency = collections.defaultdict(int)

        for c in s1:
            # creating frequency counter for string 1
            s1_frequency[c] += 1

        l = 0
        # left pointer for start of permutation substring

        for r, c in enumerate(s2):
            if c in s1_frequency:
                # if character is in s1
                s2_frequency[c] += 1
                if s2_frequency == s1_frequency:
                    # if frequencies are correct, return true
                    # this is slightly inefficient since we are having to compare entire hashmaps
                    # instead, we can put this in an elif statement after the below if statement
                    # and simply check the length of the current window
                    return True

                if s2_frequency[c] > s1_frequency[c]:
                    while s2_frequency[c] > s1_frequency[c]:
                        # if there's an extra letter
                        # keep removing from start of current string window until it is removed
                        s2_frequency[s2[l]] -= 1
                        l += 1
            else:
                # if character is not in s1, left pointer will move to next position
                # and the current frequency counter for the permutation will be cleared
                l = r + 1
                s2_frequency.clear()

        return False
    
# NOTE: THIS IS THE SOLUTION FOR MORE OPTIMAL VERSION FROM LINES 32-44
# this is better than neetcode's solution

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_frequency = collections.defaultdict(int)
        s2_frequency = collections.defaultdict(int)
        
        s1_length = len(s1)

        for c in s1:
            s1_frequency[c] += 1

        l = 0

        for r, c in enumerate(s2):
            if c in s1_frequency:
                s2_frequency[c] += 1

                if s2_frequency[c] > s1_frequency[c]:
                    while s2_frequency[c] > s1_frequency[c]:
                        s2_frequency[s2[l]] -= 1
                        l += 1
                elif (r - l + 1) == s1_length:
                    return True
            else:
                l = r + 1
                s2_frequency.clear()

        return False
        
# neetcode solution:
# time complexity: O(26) + O(n) -> O(n)
# mine was O(26*n)

# he basically starts with a window length that is the same as s1
# keeps track of how many characters match, and if all 26 match, return True
# does this by creating 2 hashmaps, both with 26 letters and their frequencies
# keeps updating how many matches there are
# he actually uses an array instead of a hashmap

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26