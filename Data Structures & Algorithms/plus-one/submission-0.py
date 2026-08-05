class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        check = False

        while check is False:
            if digits[i] == 9:
                digits[i] = 0
                if i > 0:
                    i -= 1
                else:
                     digits.insert(0, 1)
                     check = True
                    
            else:
                digits[i] += 1
                check = True

        return digits