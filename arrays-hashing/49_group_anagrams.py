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
            print(strs)
        return strs
    
#NOTE: this solution doesn't work because time complexity is too slow!
# O(m * nlogn) since it has to iterate through list and then sort every item

neetcode solution:
