class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights) ,sum(weights) 
        _min_cap = sum(weights)

        while l <= r:
            capacity = (l+r)//2
            can_ship = False
            day, curr_cap = 1, capacity
            for weight in weights:
                if curr_cap - weight < 0:
                    day += 1
                    curr_cap = capacity
                curr_cap -= weight
            
            can_ship = day <= days
            if can_ship :
                _min_cap = min(_min_cap, capacity)  
                r = capacity -1
            else:
                l = capacity + 1
               
        return _min_cap             
        