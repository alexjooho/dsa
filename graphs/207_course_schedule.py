# my solution after looking at neetcode's logic:
# faster time complexity because it doesn't do a dfs again, but takes up more space because it uses an extra set
# O(n + p) time complexity but O(p + 2n) space complexity
# can just get rid of confirmed set and just do dfs on each course instead if you want to save space
# NOTE: NEETCODE'S SOLUTION HAS A REALLY COOL TRICK TO THIS. INSTEAD OF USING A CONFIRMED SET
# HE SIMPLY SETS THE PREREQS OF THAT COURSE TO AN EMPTY LIST SO THAT IT NEVER HAS TO CHECK IT AGAIN!

# this question is not about doing dfs to find the total length, since parts can be unconnected
# instead, you should be trying to confirm that each course is valid

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs adjacency list
        # run dfs for every course from 0 to n-1  (need to do it for every course in case the graph is not fully connected!)
        # keep track of which courses were visited, since if they were visited then the current course can not be taken
        # create a hashmap of prereq courses
        # O(n + p) time complexity where n is the number of courses and p is the number of prerequisites (len(prerequisites))
        # edge case: course with no prereq and the course is not a prereq to anything
        
        # trick: for every course, make sure that it is possible to take it by recursively dfs checking
        # if all of the prereqs for that course can also be taken

        prereq = {}

        for c, p in prerequisites:
            if c in prereq:
                prereq[c].append(p)
            else:
                prereq[c] = [p]

        confirmed = set()
        # this is so that we don't redo a dfs of a course if it was already confirmed in another dfs to be valid

        def dfs(course, visited):
            if course in visited:
                return False
            if course in confirmed:
                return True
            elif course not in prereq:
                confirmed.add(course)
                return True

            visited.add(course)
            for pre in prereq[course]:
                if not dfs(pre, visited):
                    return False
            visited.remove(course)
            # need to remove this so that it doesn't keep it for future loops

            confirmed.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False

        return True
    
# neetcode solution:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

# my old solution (doesn't work):
# doesn't work because if a course has 2 prereqs that are also after the course of a previous course
# then it will stop the dfs because it doesn't know that it could take the other prereq beforehand as well
# e.g. 4 -> (1 & 2) -> 3   it will go to 3 from 1 side and 3 from 2 side, but dfs will not know it could
# have done both before getting to 3!

# problem with my idea/method was that I was trying to find a path that connects to have a length
# of the number of courses. THIS WILL NOT WORK because not all courses are connected!
# this might work for adjaceny matrixes but not for adjacency lists

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph recursive dfs problem
        # can a course have multiple prerequisites?
        
        # courses can be disconnected and not need a prereq and not be a prereq for another class
        # if that's the case, that course can always be taken

        # create a hash map of keys with courses and values of prerequisite
        # create another hash map with keys of course and value of an array of which classes it is a prerequisite for

        # for each course that has no prerequisite and is a prerequisite to a course, increment and recursively call the course that
        # the current course is required for (don't need to dfs each course since we know that a course with no prerequisite is start)
        # if that course has a prereq that has not been seen, that means its impossible to take that course, so return value
        # if the course is a prereq for multiple courses, sum the result of the dfs of all the courses
        # if there is no course that requires the current course as a prerequisite, return total

        # NOTE: all prerequisite pairs are unique

        required_for = {}
        courses_required = {}

        start = 0

        def dfs(course, seen, total):
            for c in courses_required.get(course, []):
                # .get [] is in case this course has no prereqs
                if c not in seen:
                    return
            
            total += 1
            if total >= numCourses:
                return True

            seen.add(course)
            for c in required_for.get(course, []):
                if dfs(c, seen, total):
                    return True
            
            seen.remove(course)

        for c, pre in prerequisites:
            # use .setdefault to initiate a list if it isn't present already
            courses_required.setdefault(c, [])
            courses_required[c].append(pre)

            required_for.setdefault(pre, [])
            required_for[pre].append(c)
        
        for i in range(numCourses):
            if i not in required_for and i not in courses_required:
                # this is for edge case if a course is not connected to anything
                start += 1
        
        for i in range(numCourses):
            if i not in courses_required:
                if dfs(i, set(), start):
                    return True
        
        return False