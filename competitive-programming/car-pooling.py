class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_point = -float('inf')

        for trip in trips:
            if max_point < trip[2]:
                max_point = trip[2]
        passangers = [0]*max_point

        for passanger, fromi, to in trips:
            passangers[fromi] += passanger
            if to < max_point:
                passangers[to] -= passanger

        curr_passangers = 0        
        for i in range(max_point):
            curr_passangers += passangers[i]
            passangers[i] = curr_passangers

        return max(passangers) <= capacity        

        