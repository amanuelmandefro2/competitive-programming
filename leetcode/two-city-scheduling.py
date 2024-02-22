class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        n = len(costs)/2
        min_cost = 0
        for i in range(len(costs)):
            if i < n:
                min_cost += costs[i][0]
            else:
                min_cost += costs[i][1]    


        return min_cost   
