# neetcode solution:
# O(n log n) time complexity instead of O(n^2) since he uses a stack and he also only iterates one time
# he basically does the same part of ordering by position and creating tuples/list of position and speed
# but instead of doing all the extra work, he simply calculates the time to the target
# and compares to the car ahead of it
# he uses a stack so that popping a fleet will not take O(n) time like in my solution
# since you only have to worry about the fleet directly ahead of you, you can simply pop if you catch up
# the length of the stack is how many fleets there will be

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack question
        # create a new array with each car's respective position and speed in an array
        # sort the new array by starting positions (in ascending order)
        # go from furthest ahead car (so in reverse order)

        # check if the car will catch up to the car ahead of it, by calculating its
        # time to the target point
        # if it reaches the target point sooner, then it will catch up and they should be merged
        # so we can pop the one ahead and just merge them

        # we use a stack where we insert each car fleet so that we don't have to pop from within the array
        # which would make this algorithm O(n^2) instead of O(n log n)

        # note that WE DO NOT HAVE TO WORRY ABOUT ANY FLEETS OTHER THAN THE ONE DIRECTLY AHEAD OF IT
        # since the car gets slowed down by the one directly ahead of it if it catches up
        # and the car ahead of it was already checked to see if it could catch up to the one ahead of it

        # time complexity: O(n log n) (the sorting makes it n log n but otherwise it would be n)        
        # space complexity: O(n)

        pair = [(p, s) for p, s in zip(position, speed)]
        # use zip to create tuples of the position and speed of each car
        pair.sort(reverse=True)
        # want to start with the car furthest ahead!

        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            # add the time it takes to reach target to the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # if there is a car ahead of it and the current car reaches target faster
                    # checking for the car ahead of it is just since the first car wouldn't have a car in front
                # simply pop the current car since they will merge into the slower car that is ahead
                stack.pop()
        return len(stack)

# my solution:
# created way more work because I kept iterating to find out each car's current position
# when I could simply find out when it reaches the target, and merge cars that way instead
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack question
        # NOTE: might be better to use a linked list since we have to pop from the middle sometimes!
        # create a new array with each car's respective position and speed in an array
        # sort the new array by starting positions (in ascending order)
        # keep iterating through new array (back to front) until all car fleets reach the finish line

        # if a car catches up to the car in front of it, pop the car in front and
        # set the two cars to the same position

        # if a car fleet is at or past the finish line, pop it and increment number of fleets

        # NOTE: edge case!! ->
        # a car could possibly catch up in an hour increment, but not actually in time before
        # the car ahead reaches the target if it reached it before an hour
        
        # time complexity: O(n^2) since for every fleet, we could possibly have to pop a fleet
        # and that would take O(n) time for a list
        
        # space complexity: O(n)

        total = 0

        fleets = [[position[i], speed[i]] for i in range(len(position))]
        # array of every car's position and speed

        fleets.sort()
        print(fleets)

        while fleets:
            # while there are still cars, keep iterating

            for i in range(len(fleets) - 1, -1, -1):
            # iterate backwards so that we can see if a car catches up to another car
                if fleets[i][0] >= target:
                    fleets.pop()
                    total += 1
                else:
                    fleets[i][0] = fleets[i][0] + fleets[i][1]
                    
                    if (i != len(fleets) - 1 and
                        fleets[i][0] >= fleets[i + 1][0]):
                        # if this isn't the first place fleet (since we can't compare to anything ahead then)
                        # and if it has caught up to fleet in front of it, then update and merge them
                        # but only if the ahead car hasn't crossed the line before it!!

                        if fleets[i + 1][0] > target:
                            # we have to calculate how long the ahead car took to reach the finish line
                            # if it reached finish line before current car, then we can't merge them
                            previous = fleets[i + 1][0] - fleets[i + 1][1]
                            time_to_finish = (target - previous) / fleets[i + 1][1]

                            cur_previous = fleets[i][0] - fleets[i][1]
                            cur_time_to_finish = (target - cur_previous) / fleets[i][1]

                            if cur_time_to_finish > time_to_finish:
                                # if the current fleet took longer to finish, then they stay as separate fleets
                                continue

                        fleets[i][0], fleets[i][1] = fleets[i + 1][0], fleets[i + 1][1]
                        fleets.pop(i + 1)
                        # make sure to pop the car in front, instead of just the last car with pop()

        return total