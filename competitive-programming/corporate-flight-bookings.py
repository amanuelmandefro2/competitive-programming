class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*n
        for l, r, seats in bookings:
            arr[l-1] += seats
            if r < n:
                arr[r] -= seats
        
        curr_sum = 0
        for i in range(n):
            curr_sum += arr[i]
            arr[i] = curr_sum
        return arr          