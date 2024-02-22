class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, path_lst = ['/'], path.split('/') 
      
        for curr_p in path_lst:
            if curr_p == '..':  
                if len(stack) >= 2:
                    stack.pop()
                else:
                    continue    
            elif curr_p == ".":
                continue
            elif curr_p :
                stack.append(curr_p)       
       
        path = '/'.join(stack)
        return path if len(path) == 1 else path[1:]
            
       
        