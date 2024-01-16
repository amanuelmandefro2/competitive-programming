class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*len(s)
        for shift in shifts:
            if shift[2] == 0:
                prefix[shift[0]] -= 1
                if shift[1] < len(s)-1:
                    prefix[shift[1]+1] += 1
            else:
                prefix[shift[0]] += 1
                if shift[1] < len(s)-1:
                    prefix[shift[1]+1] -= 1  
        
        curr_sum = 0
        for i in range(len(prefix)):
            curr_sum += prefix[i]
            prefix[i] = curr_sum

        res = []
        for i in range(len(prefix)):
            new_ord = ord(s[i]) + prefix[i] - 97
            new_ord %= 26
            

            res.append(chr(new_ord+97))

                   
        return ''.join(res)                  
        