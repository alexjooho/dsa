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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        # Ways that a meeting can overlap:
        # meeting is within another meeting
        # meeting ends after another meeting starts
        # meeting starts before another meeting ends

        # only actually need to check if a meeting starts in between because the others are repetitive

        # If a meeting has a start or end time that is within another meeting's
        # start and end time, then the meetings will conflict

        # easy to do an O(n^2) time complexity with brute force iteration
        # better to do a solution with O(n logn) by sorting by start times and 
        # checking if a start time is before the previous meeting's end time

        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
            
        return True

# previous brute force solution that was O(n^2) time complexity and took too long:

# if len(intervals) <= 1:
#             return True

#         for i in range(len(intervals)):
#             for j in range (len(intervals)):
#                 if i == j:
#                     continue
#                 if intervals[i].start > intervals[j].start and intervals[i].start < intervals[j].end:
#                     return False
        
#         return True