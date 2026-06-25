class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        def solve(open , close , output , res):

            if open == 0 and close == 0:
                res.append(output)
                return 

            if open > 0:
                
                solve(open-1 , close , output + "(", res)

            if close > open: 
                
                solve(open , close-1 , output + ")", res)

            return

        res = []
        solve(n , n , "", res)
        return res