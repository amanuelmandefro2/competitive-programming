class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l, r = 0, max(houses[-1], heaters[-1]) - min(heaters[0], houses[0])
        ans = float('inf')
        while l <= r:
            mid = (l+r)//2
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if heaters[j] - mid <= houses[i] <= heaters[j] + mid:
                    i += 1
                else: j += 1
            if j < len(heaters):
                ans = mid
                r = mid -1
            else: l = mid + 1

        return ans        
