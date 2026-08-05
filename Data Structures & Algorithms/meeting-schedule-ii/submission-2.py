"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        sTime = [i.start for i in intervals]
        eTime = [i.end for i in intervals]
        
        # print(sTime)
        # print(eTime)
        
        sortedStart = sorted(sTime)
        sortedEnd = sorted(eTime)

        # print(sortedStart)
        # print(sortedEnd)
        
        maxCount = 0
        count = 0
        s = 0
        e = 0

        while s < len(sortedStart):

            if sortedStart[s] < sortedEnd[e]:

                s += 1
                count += 1
                

            else:

                e += 1
                count -= 1
                
            maxCount = max(count, maxCount)        

        return maxCount

