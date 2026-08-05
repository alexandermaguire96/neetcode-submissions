class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create empty map to count
        count = {}
        #create an empty array about the same size as the range
        freq = [[] for i in range(len(nums) + 1)]

        #go over the nums and count, if there is no num, then put 0 for the count
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #put the counts into our array
        for n, c in count.items():
            freq[c].append(n)

        res = []
        
        #extract k most frequent elements going backwards along our array,
        #len(freq)-1 is the last number, all the way to 0, -1 at the end is going backwards

        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        