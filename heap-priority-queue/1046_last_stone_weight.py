class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a "max heap" by turning each value into a negative value
        # while the length of the heap is > 1 keep checking the two biggest stones
            # remember that the second value in heap will not necessarily be the biggest
        # and make changes based on the rules
        # revert all values in heap to positive numbers

        stones = [-weight for weight in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = heapq.nsmallest(2, stones)
            y = heaviest[0]
            x = heaviest[1]

            if x == y:
                heapq.heappop(stones)
                heapq.heappop(stones)
            elif x != y:
                heapq.heappop(stones)
                heapq.heapreplace(stones, y-x)

        stones = [-weight for weight in stones]
        
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
            
# neetcode solution (cleaner code):
# better because doesn't repeat the heapq.heapop twice like I did, and also solves
# final lines of code smoother with lines 46 and 47

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones = [-s for s in stones]
#         heapq.heapify(stones)

#         while len(stones) > 1:
#             first = heapq.heappop(stones)
#             second = heapq.heappop(stones)
#             if second > first:
#                 heapq.heappush(stones, first - second)

#         stones.append(0)
#         return abs(stones[0])