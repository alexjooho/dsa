class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort problem (I use dfs but you can also use BFS)
        # find indegrees (number of prereqs) for each course
        # have a dictionary with key of course that is a prereq and value of courses its a prereq for
        # (this is kind of opposite logic for dictionary as what you'd do in dfs)
        # start with courses that have no prereqs
        # pop a course that has no prereq and add it to list order
        # check which courses have that course as a pre req and get rid of it (decrement by 1)
        # add any courses that now have 0 other prereqs

        # return list if length of list is same as numCourses
        
        # time complexity: O(E + V), space complexity: O(3V) => O(V)

        indegrees = [0] * numCourses

        prereq_for = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            prereq_for[p].append(c)
            indegrees[c] += 1
        
        res = []

        no_in_stack = []

        for idx, val in enumerate(indegrees):
            if val == 0:
                no_in_stack.append(idx)

        while no_in_stack:
            cur = no_in_stack.pop()
            res.append(cur)

            for course in prereq_for[cur]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    # have to do == 0 instead of <= 0 in case it goes negative
                    no_in_stack.append(course)
            
        return res if len(res) == numCourses else []
    
# neetcode recursive dfs solution:
# O(E + V) time complexity

# a course has 3 possible states:
# visited -> course has been added to output
# visiting -> course not added to output yet, but added to cycle
# unvisited -> course not added to output or cycle

# have a visit set for nodes that have been fully visited and added to output
# have a cycle set that is for nodes that are currently being checked, to make sure there are no cycles
# for a node, add it to the cycle and then recursively check all its prereqs
# if all its prereqs return True (all the prereqs have confirmed all their prereqs), then 
# remove the node from the cycle, add the node to visited, and add it to the output array and return True
# do this for every node

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output