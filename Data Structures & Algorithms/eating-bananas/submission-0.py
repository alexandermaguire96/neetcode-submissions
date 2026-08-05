class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r)//2 #find midpoint between two pointers
            hours = 0

            for p in piles:
                hours += math.ceil(p / k) #find out how many hours it takes to eat the piles with the k we're at

            if hours <= h:#ate within the hour limit
                res = min(res, k) #store the k that works
                r = k - 1 #search the for a slower eating speed

            else:#didn't eat fast enough
                l = k + 1 #search for a higher eating speed

        return res


