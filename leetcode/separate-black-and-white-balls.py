class Solution:
    def minimumSteps(self, s: str) -> int:
        l, r = 0, len(s) - 1
        steps = 0

        while l < r:
            if s[l] == "1":
                while r > l and s[r] == "1":
                    r -= 1
                if r == l:
                    break
                steps += (r - l)
                r -= 1
            l += 1

        return steps      
