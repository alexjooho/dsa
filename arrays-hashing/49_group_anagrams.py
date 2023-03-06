class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can not use hash sets because sets do not allow duplicates

        # iterate through the list and for each item, sort it and also include its original value e.g. ['tae', 'eat']
        # sort the list by the sorted strings

        # iterate through the list and group up sorted strings that are the same

        for idx, x in enumerate(strs):
            strs[idx] = [x, ''.join(sorted(x))]
            
        strs.sort(key = lambda x: x[1])

        i = 0

        while i < len(strs):
            group = [strs[i][0]]
            j = i + 1

            while j < len(strs) and strs[j][1] == strs[i][1]:
                group.append(strs[j][0])
                j += 1

            strs[i:j] = [group]
            # have to do [group] even though group is already a list because splicing in python turns the list into values
            i += 1
            # can increment i by one because all the values that were the same will be merged into one index
        return strs
    
#NOTE: my solution's time complexity is: O(m * nlogn) since it has to iterate through list and then sort every item
# technically though, my solution is same/better than neetcode's because n of log(n) will be 26 max
# my solution also has less space complexity because it is done within the list

# neetcode solution:
# time complexity: O(m*n*26) = O(m*n) where m is number of items in array and n is the average number of letters in a string
# use hashmap!
# have to do: from collections import defaultdict
# defaultdict is like a regular dictionary except it never raises a key error if that key doesn't exist
# this gets rid of edge case where you want to add to a key that doesn't exist yet

# View on Github
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

#NOTE: for each string, he created a list and added +1 to each position in list that corresponds
# to each letter. He then made this list into a tuple so that it is valid as a key in a dictionary
# and then added the string to the corresponding key