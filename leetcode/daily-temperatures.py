class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)  

        return answer            
      
       
        stack = []
        res = [0] * len(temperatures)



        """
        brute force solution 
        for i in range(len(temperature)):
            for j in range(i+1, len(temperature)):
                if temperature[j] > temperature[i]:
                    res[i] = j - i
                    break
        return res

        """
        