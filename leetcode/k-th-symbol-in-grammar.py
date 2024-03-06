class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammar(n, k,l, r):
            if n == 1:
                return 0
            half = (l+r)/2
            if k <= half:
                return grammar(n-1, k, l, half)
            else:
                prev = grammar(n-1, k, half, r)
                if prev == 0:
                    return 1
                else:
                    return 0

        return grammar(n, k, 0, 2**(n-1))                         
        