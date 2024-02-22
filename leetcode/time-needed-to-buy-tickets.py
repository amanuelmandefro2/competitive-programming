class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = k+1
        if tickets[k] == 1:
            return time_taken

        time_taken = tickets[k]*len(tickets)
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                extra_time = tickets[k] - tickets[i]
                time_taken -= extra_time
            elif tickets[i] >= tickets[k] and i > k:
                time_taken -= 1    

        return time_taken
        