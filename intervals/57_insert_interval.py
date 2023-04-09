class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate through the array

        # if end value of new interval is not < start of current interval AND
        # start value is not > end of current interval
        # then the new interval and current interval are OVERLAPPING

        # merge these two intervals and check any following intervals to see if they are merging too
        # keep merging until intervals no longer overlap

        # time complexity: O(n)

        res = []
        # we technically created a new array instead of inserting into original array like question said to

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # if end is less than the start of current interval
                # then we can just add the new interval and attach rest of list
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # if the start is greater than the end of current interval
                res.append(intervals[i])

            # the two above if and elif statements are if the new interval are NOT OVERLAPPING
            # which means we can just insert the current interval and move on

            else:
                # if the intervals are overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # don't append to list yet because later intervals could also be overlapping
                # since we updated the newInterval, it will keep checking with intervals after it
                # until they don't overlap and they can both be added

        res.append(newInterval)
        # takes care of edge case of overlapping at/until the end by just appending
        # at end of loop if first if statement is never reached
        
        return res
    
# if you want to insert into original array like question asks:
# this is the technically correct solution since it uses original array
# but it also takes up more time since we are popping from a list

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0

        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                # if end is less than the start of current interval
                # then we can just add the new interval and attach rest of list
                intervals.insert(i, newInterval)
                return intervals

            elif newInterval[0] > intervals[i][1]:
                # if the start is greater than the end of current interval
                i += 1

            else:
                # if the intervals are overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # don't append to list yet because later intervals could also be overlapping
                # since we updated the newInterval, it will keep checking with intervals after it
                # until they don't overlap and they can both be added
                intervals.pop(i)

        intervals.append(newInterval)
        return intervals