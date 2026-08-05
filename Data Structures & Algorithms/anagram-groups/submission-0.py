#import defaultdict, 
#which creates values for dictionary values that haven't been assigned. 
#Allowing for me to apply 0s to the letters that I don't have in my string

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #going to use a dictionary in order to be able to apply index to the strings
        #since we're using strings, and there are a set 26 numbers, it'll be easiest to use the defaultdict
        anagram_map = defaultdict(list)

        for word in strs:
            #here I'm going to define what will make up the key
            char_count = [0] * 26

            #next I'm going to redefine the values of my dictionary to match the alphabet ASCII values using ord()
            for char in word:
                char_count[ord(char) - ord('a')] += 1

            #now, add the words to my dictionary, with the values being defined as tuple(char_count)
            anagram_map[tuple(char_count)].append(word)

        #return the list of values, which have been organized by their char_count values
        return list(anagram_map.values())