class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        def solve(input , output, res):
            
            if len(input) == 0:
                res.append(output)
                return 
            
            char = input[0]
            input = input[1:]
            
            op1 = output
            op2 = output
            
            if char.isalpha():
                op1 += char.lower()
                op2 += char.upper()
                
                solve(input, op1, res)
                solve(input, op2, res)
            else:
                output += char
                solve(input, output, res)

            return
        
        res = []
        solve(s, "", res)
        return res




