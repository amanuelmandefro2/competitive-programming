class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def power( x, n):
            if n == 0:
                return 1    
            if n == 1:
                return x
            
            res = power(x, n//2)
            if n % 2==0:
                return res*res%mod
            else:
                return x*res*res%mod
 
        if n % 2 == 0: 
            return power(4, n//2)*power(5,n//2)%mod
        else:
            return power(4, n//2)*power(5, n//2+1)%mod
   

    
       

        