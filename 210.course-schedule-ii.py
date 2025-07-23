#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # # 1. Kahn's Algorithm / BFS
        # # Build adjacency list and in-degree array.
        # adj_list = [[] for _ in range(numCourses)]
        # in_degree = [0] * numCourses

        # for course, prereq in prerequisites:
        #     adj_list[prereq].append(course)
        #     in_degree[course] +=1
        
        # # Initialize the queue with course that have no prerequisties.
        # queue = deque([ i for i in range(numCourses) if in_degree[i] == 0])

        # # This list will store the topological sort order.
        # topological_order = []

        # # Process the queue.
        # while queue:

        #     # Take a course that has all its prerequisites met.
        #     course = queue.popleft()
        #     # Add it to our result list
        #     topological_order.append(course)

        #     # For each course that depends on the one just taken.
        #     for next_course in adj_list[course]:
        #         in_degree[next_course] -=1
        #         # If all prerequisites for this course are now met, add it to the queue.
        #         if in_degree[next_course] == 0:
        #             queue.append(next_course)
        # # If we could take all courses, the order is valid.
        # if len(topological_order) == numCourses:
        #     return topological_order
        # else:
        #     return []

        # 2. DFS
        # Build adjacency list
        adj_list = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        # visited states: 0 = unvisited, 1 = visiting (in current DFS path), 2= visited
        visited = [0] * numCourses
        # This list will store the topological sort. We build it backwards.
        topological_order = []

        def has_cycle(course):
            # Mark the current node as visiting
            visited[course] = 1

            for neighbor in adj_list[course]:
                if visited[neighbor] ==1:
                    return True
                if visited[neighbor] == 0:
                    if has_cycle(neighbor):
                        return True
            # All descendants visited, mark this node as fully visited.
            visited[course] = 2
            # Add the course to the front of our order list
            topological_order.insert(0, course)
            return False
        #Check for cycles starting from each course
        for i in range(numCourses):
            if visited[i] ==0:
                if has_cycle(i):
                    return []
        
        return topological_order





            
# @lc code=end

