class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by starting point first
        # if end point is before next interval's start, then there is no overlap
        # otherwise, iterate through list and merge intervals
        # continue from where the iteration stopped

        # if last interval is not an overlap with anything, then i will be len(intervals) - 1
        # so we add that to the result
        
        # time complexity: O(n logn) because we sorted

        res = []

        intervals.sort(key = lambda x: x[0])
        # sort by starting times

        i = 0

        while i < len(intervals) - 1:
            # use a while loop so that you can increment i by more than 1 when you do a merge of multiple intervals
            if intervals[i][1] < intervals[i + 1][0]:
                # if end point is before start of next interval
                res.append(intervals[i])
                i += 1

            else:
                end = intervals[i][1]

                j = i + 1

                while j < len(intervals) and end >= intervals[j][0]:
                    end = end = max(end, intervals[j][1])
                    # update end point if end point is bigger
                    j += 1

                res.append([intervals[i][0], end])
                i = j
        
        if i == len(intervals) - 1:
            # for if the last interval was not overlapping other intervals
            # this also takes care of edge case where there's only one interval
            res.append(intervals[-1])

        return res
    
# neetcode solution:
# cleaner solution that doesn't require multiple while loops
# he simply compares it to the previous value and merges current with previous if they overlap

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair: pair[0])
        # sort by starting points
        output = [intervals[0]]
        # put first interval into output array to avoid edge case of just 1 interval
        # and since in his solution, we are comparing to previous value

        for start, end in intervals:
            lastEnd = output[-1][1]
            # lastEnd is the end of last interval in output array

            if start <= lastEnd:
                # if overlapping, then merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
    
    # if there is only one interval, it will just merge with itself and give correct answer