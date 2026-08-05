class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        full = intervals + [newInterval]
        print(full)
        res = sorted(full)

        i = 1
        while i < len(res):
            if res[i][0] <= res[i-1][1]:
                res[i-1][1] = max(res[i][1], res[i-1][1])
                res.pop(i)
            else:
                i +=1
        return res