class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## better solution than the one below because it simplifies it and can be done with a fibonacci-esque approach
        # keep track of previous 2 steps
        # determine which total will result in the lower number
        # keep updating the 2 steps
        # O(n) time complexity and O(1) space complexity

        n1, n2 = cost[0], cost[1]
        # steps 1 and 2 so far
        # note that we are using the costs pre-emptively so that we don't have to keep extra
        # memory to know which index we are on

        for i in range(2, len(cost)):
            # start from index 2 (3rd step) since we already did first 2 steps

            temp = n2
            # need to keep track of what n2 was since that will become our new n1
            n2 = min(n1, n2) + cost[i]
            # need to add cost[i] to it since we are pre-emptively adding costs
            n1 = temp
            # n1 is now updated to the previous n2

        return min(n1, n2)
        # can just return the minimum of these two values since both have pre-emptively
        # added costs to it. so either one can reach the end of staircase


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recursive DP problem (top down)
        # for each stair, recursively call function
        # if there is already a cost associated with that stair and it is lower,
        # skip it

        # need to keep track of what the total was when it first reached that step
        # since when we memoize the total costs and find something that is cheaper to reach
        # that step, we can just subtract the difference in total cost
        
        from collections import defaultdict

        costs = [[0, 0] for i in cost]
        costs.append(float('inf'))
        # first index is for cost to reach the end, second index is for cost to reach index
        # appended last index is for the final result

        def dfs(cur, i):
            if i >= len(cost):
                # if we have reached the top, update final result if necessary and return
                costs[-1] = min(costs[-1], cur)
                return costs[-1]

            if costs[i][0] != 0:
                # if this step has already been done, don't repeat it
                # instead update it if necessary
                if cur < costs[i][1]:
                    # if the cost to reach this step is < than previous memoized, then we can update it
                    new_total = costs[i][0] - (costs[i][1] - cur)
                    
                    costs[i] = [new_total, cur]
                    # if the cost to reach this step is greater than previously memoized
                    # then there's no point in redoing the process
                return costs[i][0]

            new_cost = cur + cost[i]

            total = min(dfs(new_cost, i + 1), dfs(new_cost, i + 2))
            costs[i] = [total, cur]
            return total

        return min(dfs(0, 0), dfs(0, 1))
        # need min between these two since you can either start on index 0 or 1
        
# neetcode solution
# DP using tabulation and going backwards since we can build up from the end

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
