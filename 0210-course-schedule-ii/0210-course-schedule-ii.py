class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        visited = [0] * numCourses # 0: unprocessed, 1: processing, 2: processed
        courses = []

        # build adjacency list
        for prereq in prerequisites:
            a, b = prereq[0], prereq[1]
            adjList[b].append(a)
        
        # cycle detection with topological sort
        def dfs(root: int) -> bool:
            if visited[root] == 1:
                return False
            if visited[root] == 2:
                return True

            visited[root] = 1

            for neighbor in adjList[root]:
                if not dfs(neighbor):
                    return False

            visited[root] = 2
            courses.append(root)

            return True
        
        # iterate through every unprocessed course
        for course in range(numCourses):
            if visited[course] == 0 and not dfs(course):
                return []

        # dfs topological sort returns sorting in reversed order
        courses = reversed(courses)
        
        return courses

            