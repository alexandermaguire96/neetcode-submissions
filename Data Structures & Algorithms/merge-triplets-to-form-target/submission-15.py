class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        triplets_c = [x for x in triplets]

        for triplet in triplets:
            # print(triplet)
#             print(triplets_c)
            
            for i in range(0,3):
                # print(i)
                if triplet[i] > target[i]:
                    # print(triplet[i], target[i], triplet, "bye")
                    if triplet not in triplets_c:
                        break
                    triplets_c.remove(triplet)
                
        # print(triplets_c, "cleaned")
        while len(triplets_c) > 1:
            # print(triplets_c, "premerge")
            merge = triplets_c.pop()
            for i in range(0,3):
                triplets_c[0][i] = max(triplets_c[0][i], merge[i]) 
            # print(triplets_c, "postmerge")
        if triplets_c:
            
            if triplets_c[0] != target:
                return False
            else:return True
        else: return False

        return True