class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
                
        i = 0
        inserted = False
        
        while i < len(intervals):

            #doesn't interact with newInterval and doesn't overlap
            if intervals[i][1] < newInterval[0]:
                i += 1

            #insertion with no overlap
            elif intervals[i][0] > newInterval[1]: 
                intervals.insert(i, newInterval)
                return intervals
            #insertion but overlap
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                intervals.pop(i)

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                intervals.insert(i, newInterval)
                inserted = True
                break
        
        if not inserted:
            intervals.append(newInterval)

        return intervals