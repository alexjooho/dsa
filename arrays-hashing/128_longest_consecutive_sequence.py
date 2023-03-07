class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn list into a set so that you can find values at O(1)
        # iterate through list and for each time there is no num - 1 value in the set
        # you know that it is a start of a sequence
        # keep checking the values above it to see how long the sequence goes for
        # update the current longest length to that new length if it is longer
        
        # O(n) time and memory complexity

        num_set = set(nums)

        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                current = 1
                j = nums[i] + 1
                while j in num_set:
                    current += 1
                    j += 1
                longest = max(current, longest)
        
        return longest
    
# neetcode solution:

# better code since it uses n in nums and (n + length) instead of making new variables

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
# union-find solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i,j):
            pi, pj = find(i), find(j)
            if pi != pj:
                if rank[pi] >= pj:
                    parent[pj] = pi
                    rank[pi] += 1
                else:
                    parent[pi] = pj
                    rank[pj] += 1
        
        if not nums:
            return 0 # corner case
        
        # first pass is initialize parent and rank for all num in nums
        parent, rank, nums = {}, {}, set(nums)
        for num in nums: # init
            parent[num] = num
            rank[num] = 0
            
        # second pass: union nums[i] with nums[i]-1 and nums[i]+1 if ums[i]-1 and nums[i]+1 in nums
        for num in nums:
            if num-1 in nums:
                union(num-1, num)
            if num+1 in nums:
                union(num+1, num)
                    
        # second pass find numbers under the same parent
        d = collections.defaultdict(list)
        for num in nums:
            d[find(num)].append(num)
        return max([len(l) for l in d.values()])