class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_counter = defaultdict(int)
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_counter[val] += 1
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] > val: 
            self.min_stack.append(val)   
        
    def pop(self) -> None:
        rem_val = self.stack.pop()


        if rem_val == self.min_stack[-1]:
            if self.min_counter[rem_val] == 1:
                self.min_stack.pop()
                del self.min_counter[rem_val]
            else:
                self.min_counter[rem_val] -= 1    
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()