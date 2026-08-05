class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def backtrack(count_f, count_b):
            front_para = "("
            back_para = ")"


            # Save the current subset (path)

            if len(stack) == n * 2:
                s = "".join(stack)
                res.append(s)

            if count_f < n:
                stack.append(front_para)
                backtrack(count_f + 1, count_b)
                stack.pop()
            if count_b < count_f:
                stack.append(back_para)
                backtrack(count_f, count_b + 1)
                stack.pop()
       
            
        backtrack(0, 0)

        print(res)

        return res

        
