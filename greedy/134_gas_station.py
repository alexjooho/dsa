class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy problem O(n)
        # brute force would be O(n^2) since we would have to check from each starting point

        # create an array of differences between gas gained and the cost of the next station
        # first, we make sure the sum of gas is >= sum of costs
            # if not, then there is no solution. if true, then there is a solution
            # NOTE: THIS IS THE MOST IMPORTANT PART!

        # then, we do what we did for maximum sum subarray question
        # we keep adding the diferences and if the total becomes negative, we start again from 0
            # update starting point whenever the sum ends up at 0
            # once we iterate through entire list, we will have found a position that doesn't end up with a
            # negative total, and that will be our starting point
            # NOTE: we don't have to loop again since we already confirmed that sum gas >= sum cost so there is a valid start

        if sum(gas) < sum(cost):
            # if not enough gas, then there is no solution
            return -1

        difference = [gas[i] - cost[i] for i in range(len(gas))]

        res = 0
        # just set result to 0 for now and update it if we encounter a negative total
        total = 0

        for index, diff in enumerate(difference):
            # need both index and difference
            total += diff
            if total < 0:
                # if the total is now negative, then we reset total and set the next index to the starting point
                res = index + 1
                total = 0

        return res
    
# neetcode solution:
# saved memory by not making a differences array

# other neetcode solution:
# probably not worth understanding since other solution is easier!

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]

        while start >= end:
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
            if start == end:
                return start
            total += gas[end] - cost[end]
            end += 1
        return -1
