class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # greedy problem (always start with minimum value available)
        # sort the numbers
        # start iterating from beginning of list and continue until we get groupSize
        # numbers, making sure to compare to previous number to see if its consecutive
        # keep a visited set to make sure we don't re-use indexes
            # this is for if there are duplicate numbers
        # if the next consecutive number doesn't exist, return False

        seen = set()
        hand.sort()
        cur = 0

        while cur < len(hand):
            if cur in seen:
                # if we have already used this index, don't use again
                cur += 1
                continue

            index = cur + 1
            # keep track of starting index
            val = hand[cur]
            # current value

            size = 1
            while size < groupSize:
                # until we reach group size
                if index in seen:
                    # if we have already used this index, we skip it
                    index += 1
                    continue

                if index >= len(hand) or hand[index] > val + 1:
                    # if the index is past the list or if it skips the next value
                    # then return false
                    return False
                else:
                    # increase val and size by 1 if it is the consecutive number
                    # add to seen set so that it is not repeated
                    if hand[index] == val + 1:
                        val += 1
                        size += 1
                        seen.add(index)
                    # if it is the same number, then we don't do these, but we
                    # increment index either way
                index += 1

            cur += 1
            # update cur to start at next index now

        return True

# neetcode solution:

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
