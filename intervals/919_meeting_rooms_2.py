from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        # need to keep track of which rooms are finished being used

        # sort the list by start times
        # keep a min heap of end times to see if a room has opened up
        # go through min heap to see if current time is past an end time for a
        # room opening up

        # if there is an available room, use it.
        # otherwise we need a conference room
        # keep track of total rooms and how many available rooms there are

        # time complexity: O(n log n), space complexity: O(n)

        total_rooms = 1
        # no matter what, at least 1 room is needed to start

        available_rooms = 0
        # first room is used from the start

        intervals.sort(key = lambda x: x.start)
        # for this question we need a lambda function
        # since this question uses class objects for intervals with start/end

        import heapq
        min_end_heap = [intervals[0].end]
        # NOTE: since this question uses a class for intervals,
        # we can't just do intervals[0][1]. instead we have to do .end
        # make sure to put this after the sorting part!!!

        for interval in intervals[1:]:
            # starting from second meeting
            while min_end_heap:
                # only do this if a room is being used
                if interval.start >= min_end_heap[0]:
                    # checking if a room has opened up
                    available_rooms += 1
                    heapq.heappop(min_end_heap)
                else:
                    # if start time is not > lowest end time, can break loop
                    break

            if available_rooms > 0:
                # if a room is available
                available_rooms -= 1
            else:
                total_rooms += 1
            
            heapq.heappush(min_end_heap, interval.end)
            # no matter what, the conference will take up a room

        return total_rooms
    
# another possible way to solve this with similar method as above:
# simply keep checking the length of the min heap and updating max rooms if the length of min heap
# is greater than current max rooms (since min heap represents rooms being used)
    
# neetcode solution:
# he basically creates an array of start and end times
# when a start time is reached, increment count by 1
# when an end time is reached, decrement count by 1
# sorted by time, but if a start and end time are at the same time,
# then it decrements first! (since they are not overlapping and a room has opened up)

# keep checking if current count is > max count, and update if it is

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        
        time.sort(key=lambda x: (x[0], x[1]))
        
        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count

# neetcode youtube video solution:
# NOT AS GOOD AS ABOVE 2 SOLUTIONS!
# he creates a start array and an end array
# he keeps track of current count and max count (res)

# he uses two pointers: for start array and end array
# he basically moves the pointer that has an earlier time
# if start and end pointers are the same, want to move end pointer first since a room has opened up
# increments count +1 if start, decrements by 1 if end. keeps checking for updated max count

def minMeetingRooms(self, intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])
    
    res, count = 0, 0
    s, e = 0, 0
    
    while s < len(intervals):
        # start pointer will always reach end first
        if start[s] < end[e]:
            # if start time is before the current end pointer's end time
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
        
    return res