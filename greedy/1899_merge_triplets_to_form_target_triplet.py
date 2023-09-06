class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # greedy problem
        # always start with the largest value out of the target triplet
        # find a triplet that has the largest value in the correct spot
        # then make sure that its 2 other numbers are not greater than the 
        # 2 other numbers of the target triplet in their respective spots
        # then continue to the 2nd largest, then the 3rd largest

        # start off with a current triplet with target's values
        # after doing the largest value of the target triplet, update that
        # index in current to 0 so it is not reused
        # O(3n) => O(n) time complexity
        # 3n since we have to iterate through triplets array for each largest value
        # O(3) space complexity => O(1)

        cur = target.copy()
        # make a current triplet so that we don't redo values when checking
        # for largest value

        for i in range(3):
            index = cur.index(max(cur))
            # get the index of the largest value available

            cur[index] = 0
            # update that index to 0 so it is not reused

            valid = False
            # keep a 'valid' variable to make sure that a valid triplet was found while looping

            for triplet in triplets:
                # search for a triplet that has the same value in respective index
                if triplet[index] == target[index]:
                    if (triplet[0] <= target[0]
                        and triplet[1] <= target[1]
                        and triplet[2] <= target[2]):
                        valid = True
                        continue
            if not valid:
                # if valid was not updated to True, then there was no valid triplet
                return False

        return True
    
# neetcode solution:
# different than mine because he doesn't keep looking for largest value and iterating
# instead, he only iterates once, and just makes sure that each index has been accounted for
# he does this by creating a set of valid indexes
# then he iterates through triplets and if a triplet has all values <= target, then he sees
# if any of the indexes are matching, and if so, adds that index to the set
# O(n) solution instead of O(3n)

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
