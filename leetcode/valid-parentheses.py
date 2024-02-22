class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_rule = {')':'(', '}':'{', ']':'['}

        for p in s:
            if p in stack_rule:
                if stack and stack[-1] == stack_rule[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return len(stack) == 0                    
        