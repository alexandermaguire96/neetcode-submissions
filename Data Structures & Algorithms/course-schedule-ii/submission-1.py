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
        


        # verify = []
        # order = []
        # loop = 0
        # while check >= 0:
            
        #     if check not in classes:
        #         order.append(check)
                
        #     elif check in classes:
        #         verify.append(check)
        #         print(verify, "verify")

        #     check -= 1
        # print(order, "order")
        # while verify:
        #     classs = verify.pop()
        #     req = classes[classs]
        #     print(classs, req, "classs, req")
            
        #     for i, num in enumerate(order):
        #         if num == classs:
        #             j = i
        #         if num == req and classs not in order:
        #             order.insert((i+1),classs)
        #             print(order)
        #         elif num == req and classs in order:
        #             fix = order.pop(order[j])
        #             order.insert((i+1), fix)

        # return order




            

