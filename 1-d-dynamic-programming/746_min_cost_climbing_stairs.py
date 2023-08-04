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
        
    