class Solution:
    def minimumSteps(self, s: str) -> int:
        left, right = 0, len(s) - 1
        steps = 0

        while left < right:
            if s[left] == "1":
                while left < right and s[right] == '1':
                    right -= 1
                steps += right - left
                right -= 1

            left += 1

        return steps    