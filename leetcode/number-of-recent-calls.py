class RecentCounter:

    def __init__(self):
        self.request = deque()
        self.size = 0
        

    def ping(self, t: int) -> int:
        self.request.append(t)
        self.size += 1
        time = t - 3000
        while self.request[0] < time:
            self.request.popleft()
            self.size -= 1
        return self.size    
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)