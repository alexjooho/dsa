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

        # time complexity: O(n)

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
                    # if frequencies are correct
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