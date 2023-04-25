# neetcode solution:
# O(n + n * log(26)) => O(n) time complexity
# the log(26) comes from the push and pop operations for a heap, and since there can be 26 different
# lettered tasks, that is the max x that log(x) could have.

# we actually don't need to worry about the letter of the task, we just care about the count of each task
# similar concept to my idea of using a max heap based on count, but here we use both a MAX HEAP and a QUEUE
# whenever we do a task from the max heap, we decrement its count by 1, and then add it to the queue if it's not 0
# along with the time that the task is available [count, time available]
    # unlike my solution, we don't re-add the task to the heap, we simply add it to the queue
# MAKE SURE TO KEEP THE COUNTS AS NEGATIVE NUMBERS TO MAKE THE HEAP A "MAX HEAP"

# if the time is = to the available time of the first task in the queue,
# then we put that task back in the max heap (just put its count into the heap) since its available again

# keep looping until there are no tasks in both the heap and the queue and keep incrementing time by 1
# NOTE: can also skip time if there is nothing in the max heap, since that means that the earlier time we could
# do anything would be at the time of the first task in the queue

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task is 1 unit time
        count = Counter(tasks)
        # can just iterate through tasks, but could also use built-in counter from python with
        # from collections import Counter
        
        maxHeap = [-cnt for cnt in count.values()]
        # use the negative value of each count to make it a "max heap"
        heapq.heapify(maxHeap)

        time = 0
        # time starts at 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            # if maxHeap or q has tasks, that means we haven't finished all tasks yet so we keep going
            time += 1
            # increment time by 1 automatically in the beginning since no matter what, time will increase

            if not maxHeap:
                # if there is nothing in the maxHeap and we are still in this loop, then that means
                # that there must be a task in the queue and we can skip to whatever time makes the
                # first available task available
                time = q[0][1]
            else:
                # if there is a task in the max heap, then we can just pop the task with largest count
                # and do it (we can check queue for available tasks after doing this since
                # we incremented time earlier but time actually only increments after the task is done
                # which means only the tasks in the heap are available at the actual current time
                cnt = 1 + heapq.heappop(maxHeap)
                # add 1 to the count since its a negative value and that'll get it closer to 0
                if cnt:
                    # if the count isn't 0, we add it to the queue with the time that it available again
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                # if there is something in the q and the earlier available task time is == now current
                # time, then we can add that task into the heap again
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    

# unintuitive "mathematical" O(n) solution:
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## RC ##
        ## APPROACH : HASHMAP ##
        ## LOGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
        ##  Slot size = (n+1) if n= 2 => slotsize = 3 Example: {A:5, B:1} => ABxAxxAxxAxxAxx => 
        ## indices of A = 0,2 and middle there should be n elements, so slot size should be n+1
        
        ## Ex: {A:6,B:4,C:2} n = 2
        ## final o/p will be
        ## slot size / cycle size = 3
        ## Number of rows = number of A's (most freq element)
        # [
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # ]
        #
        # so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
                                     # ans   =     rows_except_last   * columns +        last_row
        
        # the "all elements with max freq" is since we need that many extra slots at the end for those tasks
            
        ## but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
        ## total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, 
        ## which is not possible. so we have to return max(ans, number of tasks)
        
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        task_count = collections.Counter(tasks)
        max_count = max(task_count.values())
        max_tasks = sum(1 for count in task_count.values() if count == max_count)
        total_slots = (max_count - 1) * (n + 1) + max_tasks
        return max(total_slots, len(tasks))

# my solution:
# O(n^2 log n) time complexity... it results in a time limit exceeded error for leetcode
# but it technically gets the correct answer every time

# the problem with my approach was that I tried to do too many things in the maxheap
# instead of utilizing another data structure (queue) to hold other information, which in this
# case are the tasks that are unavailable

# My idea of popping and pushing items back into the heap, and only using a max heap, would work
# if I didn't pop extra tasks that could not be done. In order to make this work, while there are items
# in the heap, I pop n + 1 tasks, store them, and re-add them.
    # NOTE: THIS WOULD STILL NOT BE AS OPTIMAL AS THE SOLUTION USING A QUEUE AS WELL!
# this way, whatever we pop from the heap will always be a task that we can do, and we don't even have
# to worry about the task's next available time
# we also don't need to keep track of the task's name.
# update time by either the number of tasks stored/added if the heap is now empty, or n + 1
# only add tasks back into the heap if their count is not 0 after decrementing them.
# https://www.youtube.com/watch?v=ySTQCRya6B0 uses this solution method

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a dictionary with the counts of each letter in tasks array
        # create a list with items of: [count, soonest time it can be done, task]
        # create a MAX HEAP sorted by the count of each letter
            # this is since we want to do tasks that are most common as often as possible
            # to minimize idle time
        # while the heap still has tasks, pop tasks until there is a task with a 
        # "soonest time it can be done" that is <= current time
            # keep track of the popped tasks in a list
        # if there are none, increment time by 1
        # push the tasks back into the heap, and if a task was completed, decrement its
        # count by 1 and update the soonest time it can be done again
        # don't push it back in if the count for the task is now 0

        # O(2n + (n^2 * 2log n)) time complexity since for each task, we may have to check every task
        # until we find a task that can be done/there are no tasks we can do
        # and for each task that we pop out and push back in, it is 2 log n heap time complexity

        # O(4n) => O(n) space complexity since we make a dictionary, list, heap of size n
        # and we also have a list of popped tasks that we use to re-push into the heap

        counter = defaultdict(int)

        for task in tasks:
            counter[task] += 1

        task_heap = []
        time = 0

        for count in counter:
            task_heap.append([-counter[count], 0, count])
            # we make a list of [count, soonest time, task] so that we can make a heap out of it
            # TAKE THE NEGATIVE VALUE OF COUNT TO MAKE IT A "MAX HEAP"

        import heapq
        heapq.heapify(task_heap)
        # O(n) time complexity operation for heapify

        while task_heap:
            popped_tasks = []
            cur = heapq.heappop(task_heap)

            while cur[1] > time and task_heap:
                # if the popped task is not doable yet, keep popping until the popped task is doable
                # or until there are no tasks in task_heap

                popped_tasks.append(cur)
                cur = heapq.heappop(task_heap)

            if cur[1] <= time:
                # if the current popped task is doable, then update its count and soonest time
                # push to heap if count is still > 0
                cur[0] += 1
                # since the counts are negative to make it a max heap, we actually add 1 to count
                # to get it closer to 0
                cur[1] = time + n + 1
                if cur[0] != 0:
                    heapq.heappush(task_heap, cur)

            else:
                # if the current task is not doable (which means we exhausted the heap of tasks)
                # then we simply append to popped tasks
                popped_tasks.append(cur)

            for popped in popped_tasks:
                # push all the popped tasks back into the heap
                heapq.heappush(task_heap, popped)

            time += 1
            # always increment time by 1

        return time
    
# my solution after watching neetcode video but before looking at code:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_heap = []

        from collections import Counter
        count = Counter(tasks)

        for task_count in count.values():
            task_heap.append(-task_count)

        import heapq
        heapq.heapify(task_heap)

        from collections import deque
        queue = deque()

        time = 0

        while task_heap or queue:
            if queue and queue[0][1] == time:
                task = queue.popleft()
                heapq.heappush(task_heap, task[0])
            
            if task_heap:
                cur_task = heapq.heappop(task_heap) + 1
                if cur_task != 0:
                    queue.append([cur_task, time + n + 1])

            time += 1

        return time