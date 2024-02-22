class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for p in s:
            if p == '(':
                stack.append(p)
            elif stack:
                if stack[-1] == '(':
                    stack.pop()
                    score = 1
                    if stack and stack[-1] !='(':
                        old_score = stack.pop()
                        score += old_score 
                    stack.append(score)
                else:
                    curr_score = stack.pop()
                    score = curr_score *2
                    stack.pop()
                    if stack and stack[-1] != '(':
                        score += stack.pop()
                    stack.append(score)    


        print(stack)
        return stack[0]
        