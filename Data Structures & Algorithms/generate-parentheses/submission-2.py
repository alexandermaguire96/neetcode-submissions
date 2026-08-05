class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
    
        res = []
        
        def backtrack(string, count_f, count_b):
            front_para = "("
            back_para = ")"


            # Save the current subset (path)

            if len(string) == n * 2:
                res.append(string)
                return

            if count_f < n:
                
                backtrack(string + front_para ,count_f + 1, count_b)

            if count_b < count_f:
                
                backtrack(string + back_para ,count_f, count_b + 1)

       
            return
        backtrack("",0, 0)


        return res

        
