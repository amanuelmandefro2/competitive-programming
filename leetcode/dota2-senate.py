class Solution:
    def predictPartyVictory(self, senate: str) -> str: 
        queue_r, queue_d = deque(), deque()
        n = len(senate)
        
        for i in range(len(senate)):
            if senate[i] == 'D':
                queue_d.append(i)
            else:
                queue_r.append(i)
        while queue_r and queue_d:
            left_d = queue_d.popleft()
            left_r = queue_r.popleft()
            if left_d < left_r:
                queue_d.append(n + left_d)
            else:
                queue_r.append(n + left_r)
                      

        return 'Dire' if len(queue_r) == 0 else "Radiant"
        