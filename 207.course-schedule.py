#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 建立一個 graph,用來儲存圖的結構
        # Create a graph, used to store the structure of the graph
        graph = {}
        for course, prereq in prerequisites:
            # 如果先修課還沒出現,給這個先修課一個空的list,用來存後面的後修課
            # If the prerequisite courses have not appeared, give the prerequisite course an empty list, used to store subsequent courses
            if prereq not in graph:
                graph[prereq] = []
            # 將後修課加入先修課的list中
            # Add subsequent courses to the list of prerequisite courses
            graph[prereq].append(course)
        # 0 = 未訪問, 1 = 訪問中, 2 = 已完成
        # 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses

        def dfs(course):
            # 先檢查是不是已經處理完成
            # First check if it has been processed
            # 如果該節點已經訪問過,又訪問到一次,表示有環,所以會循環到,沒辦法完成課程,直接返回False
            # If the node has been visited, visit it again, it means there is a cycle, so it will loop, can't finish the course ,directly return False
            if visit[course] == 1:
                return False
            # 已經訪問完成, 表示沒有環, 可以完成課程,直接返回True
            # If the node has been visited, it means there is no cycle, can finish the course, directly return True
            if visit[course] == 2:
                return True
            
            # 沒有訪問過,則開始執行訪問過程
            # If it has not been visited, start the visit process
            # 剛執行訪問中,改成1
            # Just execute the visiting, change it to 1
            visit[course] = 1

            # 如果該節點有後修課,則遍歷後修課
            # If the node has subsequent courses, traverse subsequent courses
            if course in graph:
                for neighbor in graph[course]:
                    # 遞歸訪問後修課,如果有環,則返回False
                    # Recursively visit subsequent courses, if there is a cycle, return False
                    if not dfs(neighbor):
                        return False
                
            # 遞歸訪問完成,改成2
            # Recursive visit completed, change it to 2
            visit[course] = 2
            return True
        
        # 初執行遞歸訪問
        # Initialize recursive visit
        for i in range(numCourses):
            # 如果收到false,表示有環,則返回False
            # If false is received, there is a cycle, return False
            if not dfs(i):
                return False
            
        return True

        


        
# @lc code=end

