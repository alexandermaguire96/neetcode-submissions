from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a default dict, which organizes information in groups based on key
        res = defaultdict(list)

        for s in strs:
            #since we're only using lowercase letters, I can make an array that will mark the number of letters as the key
            count = [0] * 26

            for c in s:
                #ord of character - ord of a will give  a number 0-25 which is being used as the index in our array. 
                #Pointing us which number to raise
                count[ord(c)-ord('a')] += 1
             #use tuple of count in order for the key to be entered as the key, but will remain unchanged. Append string attached to the key. 
             #Since anagrams will have the same number of char. The keys will be the same for multple strings.
             #Strings will be grouped together by key auto... due to defaultdict. This also means, solo strings will be used as well. 
            res[tuple(count)].append(s)
        #we return our list, but only the values, because the answer we're looking for is just the strings. 
        return list(res.values())