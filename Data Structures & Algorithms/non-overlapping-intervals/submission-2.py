class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        output = 0
        intervals.sort()
        preInterval = intervals[0]
        print(intervals)
        for i in range(1, len(intervals)):
            
            if preInterval[1] > intervals[i][0]:
                if preInterval[1] > intervals[i][1]:
                    preInterval = intervals[i]
                output += 1

            else:
                preInterval = intervals[i]
            
        return output
