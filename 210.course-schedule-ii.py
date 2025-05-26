#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            # 如果先修課還沒出現,給這個先修課一個空的list,用來存後面的後修課
            # If the prerequisite courses have not appeared, give the prerequisite course an empty list, used to store subsequent courses
            # if prereq not in graph:
            #     graph[prereq] = []
            # 將後修課加入先修課的list中
            # Add subsequent courses to the list of prerequisite courses
            graph[prereq].append(course)
        
        # 0 = 未訪問, 1 = 訪問中, 2 = 已完成
        # 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses
        # 用來存儲結果
        # Used to store the result
        result = []

        def dfs(course):
            # 先檢查是不是已經處理完成
            # First check if it has been processed
            # 如果該節點已經訪問過,又訪問到一次,表示有環,所以會循環到,沒辦法完成課程,將檢查有沒有環的變數改成False
            # If the node has been visited, visit it again, it means there is a cycle, so it will loop, can't finish the course, change the check variable to False
            if visit[course] == 1:
                return False
            # 已經訪問完成,直接返回
            # If the node has been visited, directly return
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
            result.append(course)
            return True

        # 遍歷所有課程
        # Traverse all courses
        for course in range(numCourses):
            if visit[course] ==0:
                if not dfs(course):
                    return []  # 有環 → 無法修完所有課
        
        # 反轉結果：從後修課排序成先修順序
        # Reverse the result: sort from subsequent courses to prerequisite order
        return result[::-1]
        

# @lc code=end

