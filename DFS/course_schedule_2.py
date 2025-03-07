class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = { i: [] for i in range(numCourses)}
        for (course, prereq) in prerequisites:
            prereq_map[course].append(prereq)

        visited = set()
        path = set()
        res = []

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res


            