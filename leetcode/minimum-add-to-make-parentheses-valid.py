class Solution:
    def minAddToMakeValid(self, s: str) -> int:    
        open_par, close_par = 0, 0
        for p in s:
            if p == '(':
                open_par += 1
            elif ')' and open_par:
                open_par -= 1
            else:
                close_par += 1


        return close_par + open_par        