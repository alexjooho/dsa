import heapq

class KthLargest:

    # Min Heap of Size K
    # Don't ever need more than size K because you never get rid of elements
    # Don't need any numbers less than the 3 largest elements
    # pop elements from min heap until size is K

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k

        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # edge case of if the initialized list has less than K elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)