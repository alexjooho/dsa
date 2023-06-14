class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # have to use Bellman-Ford instead of Dijkstra's because we have to find
        # destination within K stops!

        # keep a current prices array and a temporary prices array
        # this is so that we only update values for the specific iteration
        # that we are on

        # we will have k + 1 iterations, since we can only have k stops in between
        # For each edge, check if the current price + edge will result
        # in a lower cumulative value than in the temporary array for
        # that node, and if so, update it
        # after each iteration, the temporary array becomes the current array
            # temporary array will also stay the same and be the one
            # being updated in subsequent iteration

        # O(E * K) time complexity

        prices = [float('infinity')] * n
        prices[src] = 0
        temp_prices = prices.copy()
        # creating prices array and temporary prices array

        edges = defaultdict(list)
        for f, t, p in flights:
            # for the from, to, and price values in flights
            # create an adjacency list dictionary
            edges[f].append([t, p])

        for i in range(k + 1):
            for city in range(n):
                # for each city, go through adjacency list
                # and update any lower cumulative prices
                # ignore if the current price is infinity since
                # that means we haven't reached this city previously

                curr_price = prices[city]
                if curr_price == float('infinity'):
                    continue
                for to_city, price in edges[city]:
                    if curr_price + price < temp_prices[to_city]:
                        # if cumulative price is less than temporary price of city
                        # then update in temporary array
                        temp_prices[to_city] = curr_price + price

            prices = temp_prices.copy()
            # update prices array to be a copy of temp prices since iteration is over

        return prices[dst] if prices[dst] != float('infinity') else -1

# neetcode solution:
# same solution but he doesn't make an adjacency list

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
