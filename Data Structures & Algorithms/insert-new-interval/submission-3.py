class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        full = intervals + [newInterval]
        res = sorted(full)
        print(res)

        i = 1
        while i < len(res):
            if res[i][0] <= res[i-1][1]:
                res[i-1][1] = max(res[i][1], res[i-1][1])
                print(res)
                res.pop(i)
                print(res, i, "i drop")
            else:
                i +=1
        return res