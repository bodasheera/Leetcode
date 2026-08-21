class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        curr = [0,0]


        for m in moves:

            match m:

                case 'U': curr[1] = curr[1] + 1

                case 'D': curr[1] = curr[1] - 1
                
                case 'R': curr[0] = curr[0] + 1

                case 'L': curr[0] = curr[0] - 1
                
        return curr == [0,0]