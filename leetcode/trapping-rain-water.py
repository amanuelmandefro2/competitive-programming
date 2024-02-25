class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        max_before, traped_water = -float('inf'), 0
        for i in range(len(height)):
            while stack and height[stack[0]] < height[i]:
                min_max = min(height[stack[0]], height[i])
                height_before_max = height[stack.pop()]
                traped_water += min_max - height_before_max
            stack.append(i)
            
        print(stack)
        left_max = -float('inf') 
        while len(stack) >= 2:
            curr = height[stack.pop()]
            left_max = max(curr, left_max)
            min_max = min(left_max, height[stack[0]])
            if min_max - height[stack[-1]] > 0:
                traped_water +=  min_max - height[stack[-1]]
        return traped_water         


        