class MedianFinder:

    def __init__(self):
        
        self.array = []
        print(self.array, "array made")

    def addNum(self, num: int) -> None:
        
        self.array.append(num)
        print(self.array, "number added")
        self.array.sort()
        

    def findMedian(self) -> float:

        if len(self.array) % 2 == 0:
            
            median1 = self.array[(len(self.array) // 2)]
            print(median1, "even 1")
            median2 = self.array[(len(self.array) // 2) - 1] #round up, then go down 1 index
                                                             #way easier than rounding down
            print(median2, "even 2")
            median = (median1 + median2)/2
            

        else:
            median = self.array[len(self.array)//2]
            print(median, "median odd")

        return median
