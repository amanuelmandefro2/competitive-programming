class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_move = 0
        while maxDoubles and target > 1:
            if target % 2:
                target -= 1
                min_move += 1
            else:
                target //= 2
                min_move += 1
                maxDoubles -= 1
        
        return min_move + target-1            

        