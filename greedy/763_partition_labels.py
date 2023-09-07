class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # greedy problem
        # make an array to keep number values of string lengths
        # for any given letter, we need to know what its last position is
        # since we need to make sure it is not included in any other partition
        # create a dictionary and iterate through string to get the last position of each letter
        # iterate through string again and keep track of starting point and keep track of the last
        # position of all visited letters in the current partition
        # keep updating last position if a new letter is found with a greater last position
        # if last position is reached, add the length to the length array

        last_position = {}
        lengths = []

        for index, c in enumerate(s):
            # keep updating positions of each letter
            last_position[c] = index

        start = 0
        end = last_position[s[0]]
        # create a start and end variable, which is initially the start and end of the first letter

        for index, c in enumerate(s):
            if index == end:
                # if we reach the last position, add the length to the lengths array
                # and update the starting and end points
                lengths.append(end - start + 1)
                if index + 1 < len(s):
                    # have to make sure that we have not already reached the end of the string
                    # or else it would throw an error
                    start = index + 1
                    end = last_position[s[start]]

            else:
                # update ending if last position of visiting letter is greater
                if last_position[c] > end:
                    end = last_position[c]

        return lengths
    
# neetcode solution:
# same concept as my solution of figuring out each letter's last position
# he uses current length instead of a starting point like I do, and he keeps incrementing it
# this prevents the problem of having to check that we are not already at the last index
# he also uses goal = max(goal, count[c]) which is technically less code than my solution of
# just checking if the last position is greater

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = {}
        res = []
        i, length = 0, len(S)
        for j in range(length):
            c = S[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = S[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res
