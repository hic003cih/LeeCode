#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        # # 1. Kahn's Algorithm / Breath-First Search(BFS)
        # # Build adjacency list and in-degree array
        # adj_list = [[] for _ in range(numCourses)]
        # in_degree = [0] * numCourses

        # for course, prereq in prerequisites:
        #     adj_list[prereq].append(course)
        #     in_degree[course] += 1
        
        # # Initialize the queue with all courses that have no prerequisites
        # queue = deque([i for i in range(numCourses) if in_degree[i]==0])

        # courses_taken =0

        # #Process the courses
        # while queue:
        #     course = queue.popleft()
        #     courses_taken +=1

        #     #For each course that depends on the one just taken
        #     for next_course in adj_list[course]:
        #         #Decrement its in-degree
        #         in_degree[next_course] -=1
        #         # If all its prerequisites are now met, add it to the queue
        #         if in_degree[next_course] == 0:
        #             queue.append(next_course)
        # # If the number of courses taken equals the total, it's possible
        # return courses_taken == numCourses

        # 2. Depth First Search
        #Build adjacency list
        adj_list = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
        
        # visited states : 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses

        def has_cycle(course):
            # Mark the current node as visiting
            visited[course] = 1

            #Recur for all the neighbors
            for neighbor in adj_list[course]:
                # If the neighbor is being visited, we found a cycle
                if visited[neighbor] == 1:
                    return True
                # If the neighbor is unvisited, start a new DFS from it
                if visited[neighbor] == 0:
                    if has_cycle(neighbor):
                        return True
            # If we explored all paths from this node without finding a cycle.
            # mark it as fully visited.
            visited[course] = 2
            return False
        
        # Check for cycles staring from each course.
        for i in range (numCourses):
            if visited[i] == 0:
                if has_cycle(i):
                    return False
        return True



# @lc code=end

