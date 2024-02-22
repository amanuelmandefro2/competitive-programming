class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palid_count = Counter(palindrome)
        palindrome_lst = list(palindrome)
        if len(palindrome) == 1:
            return ''
        for i in range(len(palindrome)): 
            if palindrome_lst[i] != 'a':
                if len(palid_count) == 2 and palid_count[palindrome[i]] == 1:
                    continue
                palindrome_lst[i] = 'a'
                break
            elif i == len(palindrome) -1 and  palindrome_lst[i] == 'a':
                 palindrome_lst[i] = 'b'  

        return ''.join(palindrome_lst)
          
        
        