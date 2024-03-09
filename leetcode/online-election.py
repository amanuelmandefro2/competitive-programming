class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leading =[]
        self.times = []
        
        count = defaultdict(int)
        
        lead_point = 0
        
        for i in range(len(persons)):  
            count[persons[i]]+=1
            if count[persons[i]]>= lead_point: 
                lead_point = count[persons[i]]
                self.leading.append(persons[i])
                self.times.append(times[i])
              
    def q(self, t: int) -> int:
        
        index = bisect_right(self.times, t) -1
        return self.leading[index]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)