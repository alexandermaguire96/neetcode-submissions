class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def helper(n):
            total = 0
            while n > 0:
                remainder = n % 10
                total += (remainder ** 2)
                n //= 10

            return total
            

        while True: 
            n = helper(n)
            
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)

        

