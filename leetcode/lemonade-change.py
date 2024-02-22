class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        _5, _10 = 0, 0
       
        for bill in bills:
            if bill == 5:
                _5 += 1

            elif bill == 10:
                _10 += 1
                _5 -= 1
            elif bill == 20:
                if _10 > 0:
                    _10 -= 1
                    _5 -= 1
                else:
                    _5 -= 3    
            if _5 < 0:
                return False        

        return True                  