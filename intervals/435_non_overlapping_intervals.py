class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals question
        # sort by starting time
        # whenever there's an overlap (start is less than end of previous interval)
        # then we get rid of the interval with a bigger end point

        # this is because the interval with a bigger end point has a higher chance of overlapping with
        # other intervals

        # greedy approach
        # keep track of end point of previous interval to keep checking if current interval overlaps
        # time complexity: O(n log n) since we have to sort

        # NOTE: same values do not count as overlapping! e.g. 1-2 and 2-3 are not overlapping

        removed = 0

        intervals.sort(key = lambda x: x[0])
        # sort by starting times
        # technically don't need the key/lambda function since it will sort by first index first
        # automatically

        end = intervals[0][1]
        # set end to first end point

        for i in range(1, len(intervals)):
            # start from second interval (or dont do a loop if only 1 interval in list)
            # NOTE: could also do -> for start, end in intervals[1:]:
            # this is slightly better code
            
            if intervals[i][0] < end:
                removed += 1
                end = min(end, intervals[i][1])
                # if we removed an interval, the new previous end will be the smaller endpoint
                # since we remove the interval with a larger endpoint
            else:
                end = intervals[i][1]
                # if they are not overlapping and we don't get rid of an interval,
                # then we simply update end to current interval's endpoint
        
        return removed