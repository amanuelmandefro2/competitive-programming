class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)

        l, r = 0, 0
        max_count = 0

        while r < len(fruits):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

            current_max = r - l + 1
            max_count = max(max_count, current_max)

            r += 1

        return max_count