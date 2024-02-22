class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans, n = 0, len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                if len(stack) >= 2:  
                    j = stack.pop()
                    ans += arr[j] * (i - j) * (j - stack[-1]) 
                else:
                    j = stack.pop()
                    ans += arr[j] * (i-j)*(j+1) 
            stack.append(i)

        for i in range(len(stack)):
            if i > 0:
                ans += (stack[i] - stack[i - 1]) * (n - stack[i]) * arr[stack[i]]
            else:
                ans += (stack[i] + 1) * (n - stack[i]) * arr[stack[i]] # Modification: Correcting the calculation for single element in stack
        
        return ans % (10**9 + 7)
