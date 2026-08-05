class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary_str = format(n, '032b') 

        binary_str_reversed = binary_str[::-1]
        
        
        return int(binary_str_reversed,2)

