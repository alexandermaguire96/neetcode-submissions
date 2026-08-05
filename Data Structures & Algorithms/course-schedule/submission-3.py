class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        reqMap = defaultdict(list)

        for req in prerequisites:
            reqMap[req[1]].append(req[0])

        visited = set()

        def dfs(course, path):
            if course in path:
                return True
            if course in visited:
                return False
            

            for nextCourse in reqMap[course]:
                visiting = dfs(nextCourse, path + [course])
                if visiting:
                    return True
            
            visited.add(course)
            return False
            
        for course in range(numCourses):
            if course not in visited:
                if dfs(course, []):
                    return False

        return True
