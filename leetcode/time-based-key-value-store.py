class TimeMap:

    def __init__(self):
        self.timestamp_store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        time = self.timestamp_store[key]
        l, r = 0, len(time) - 1
        ans = ''
        while l <= r:
            mid = (l+r)//2
            if time[mid][1] <= timestamp:
                ans = time[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)