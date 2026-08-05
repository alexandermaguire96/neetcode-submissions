class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, 1
        res = 0
        tempSum = 0
        lastPeak = 0

        while r <= len(height)-1:
            print("l", l, "r", r, height[l], height[r])
            
            if height[l] == 0:
                l += 1
                r += 1

            elif height[l] > height[r]:
                tempSum += (height[l] - height[r])
                print(tempSum, "tempSum")
                r += 1

            elif height[l] <= height[r]:
                res += tempSum
                print(res, "res")
                tempSum = 0
                l = r
                lastPeak = l
                print(lastPeak)
                r += 1

        if tempSum != 0:
            print("finalcheck")
            tempSum = 0
            r = len(height)-1
            l = r  - 1
            limit = max(lastPeak, 0)

            while l >= limit:

                if height[r] > height[l]:
                    tempSum += (height[r] - height[l])
                    print(tempSum, "tempSum")
                    l -= 1

                elif height[r] <= height[l]:
                    res += tempSum
                    print(res, "res")
                    tempSum = 0
                    r = l
                    l -= 1

        return res
            