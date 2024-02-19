class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = curr_penalty = customers.count('Y')
        ans = 0

        for j in range(len(customers)):
            curr_penalty += 1 if customers[j] == 'N' else -1
            
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                ans = j + 1

        return ans