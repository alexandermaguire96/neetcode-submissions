class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        mergedlist = sorted(intervals)
        print(mergedlist)

        def merge(array):

            if array[0][1] >= array[1][0]:
                array[0] = [min(array[0][0], array[1][0]), max(array[0][1], array[1][1])]
                stuff = array.pop(1)
                print(stuff)
            
            elif array[0][1] < array[1][0]:
                goodstuff = (array.pop(0))
                res.append(goodstuff)

            

            print("merged merg", mergedlist)
            

        
        while len(mergedlist) > 1:
            merge(mergedlist)
            print("merge")
         
        res = res + (mergedlist)
        print("we done")

        print(res)

        return res