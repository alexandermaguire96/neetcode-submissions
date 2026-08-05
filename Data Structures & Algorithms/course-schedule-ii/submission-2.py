class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        check = numCourses - 1
        classes = defaultdict(list)
        for prereq in prerequisites:
            classes[prereq[0]].append(prereq[1])

        visited, visiting = set(), set()
        order = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return  True
            
            visiting.add(course)
            for prereq in classes[course]:
                if dfs(prereq) == False:
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return order

