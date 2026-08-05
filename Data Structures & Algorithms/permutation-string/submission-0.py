class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
                    
        seek = [0] * 26
        for char in s1:
            seek[ord(char) - ord('a')] += 1
            print(seek,'seek')
            
        check = [0] * 26
        for char in s2[:len(s1)]:
            check[ord(char) - ord('a')] += 1
            print(check, 'check')

        if seek == check:
            return True

        for i in range(len(s1), len(s2)):
            check[ord(s2[i]) - ord('a')] += 1
            check[ord(s2[i-len(s1)]) - ord('a')] -= 1
            print(check, 'check_window')
            if seek == check:
                return True
        return False                    


