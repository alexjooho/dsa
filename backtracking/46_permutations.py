class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking recursion problem
        # for every index in the array, recursively call function
        # within recursive function, iterate through indexes and recursively call function
        # after adding each index value to current array that hasn't already been added
        # to make sure we don't add duplicates, we keep a seen set
        
        # time complexity is O(n^n) since for every starting point, we need to iterate through 
        # all indexes n times until we get a full permutation

        res = []
        seen = set()
        cur = []

        def dfs():
            if len(seen) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if i not in seen:
                    # if i hasn't been added yet
                    # then add the i index's value to current array and seen set
                    # then call recursive function and then remove both
                    cur.append(nums[i])
                    seen.add(i)
                    dfs()
                    cur.pop()
                    seen.remove(i)

        dfs()
        # I originally included the below lines, but it's not needed since we can just
        # call dfs without using any variables and it will automatically do a call starting with each
        # index

        # for i in range(len(nums)):
        #     # start the recursive call with each index since each index has to be a starting point
        #     # append the value to cur and seen set before calling, and remove afterwards
        #     cur.append(nums[i])
        #     seen.add(i)
        #     dfs(i)
        #     cur.pop()
        #     seen.remove(i)

        return res
    
# leetcode random user solution:
# better than my solution because it makes it so that we don't have to iterate through
# entire array each time
# also better than neetcode's solution!
# time complexity is O(n * n!)

# unlike my solution, it has a nums variable in the recursive function that accepts an array
# for every call he makes, he removes an index from the nums array variable so that we check one
# less index each time
# he does this with nums[:i] + nums[i + 1:]
# THIS ALSO MEANS HE DOESNT NEED A SEEN SET since all numbers in nums have not been used yet

# another different thing he does (that is a stylistic thing) is that he doesn't keep an outside
# variable of cur, and instead he just does path + [nums[i]] to keep updating the path variable
# that is a function variable. This allows you not to have to do cur.pop() each time

class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# neetcode solution:
# pop off an element and find all permutations of the remaining elements
# keep doing this recursively until we get to the base case where there is only one element
# since we know with one element, there is only one permutation

# we are going bottom up, and instead of putting first element we start with at beginning, we always
# just append it to the end

# time complexity is O(n^2 * n!) since for every index, we pop (which is another n operation)
# and we have to do this n! times

# time complexity for neetcode's solution is better than mine since it doesn't make you iterate through
# entire array again like mine does

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            # pop off first value
            # we have to pop the first one since we will append it back at the end
            # and if we do a normal pop, then we will just repeat the same number
            perms = self.permute(nums)
            # get permutations of new "nums" array, which now does not include the first number

            for perm in perms:
                # for each permutation made with the remaining numbers, we append the starting number
                perm.append(n)
            res.extend(perms)
            nums.append(n)
            # after everything has been added to results, we append the number back into the array
        return res
