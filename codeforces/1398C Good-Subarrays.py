from collections import Counter, defaultdict
import sys

def S(): return sys.stdin.readline().strip()
def I():return(int(S()))
def IL():return(list(map(int,S().split())))
def SL():return(list(S()))
def SIL():return list(map(int, SL()))
def IV():return(map(int,S().split()))
def M(n):return [IL() for _ in range(n)]
def SM(n):return [SIL() for _ in range(n)]

def solve():
    for _ in range(I()):
        n = I()
        a = SIL()
        prefix = defaultdict(int)
        prefix[0] = 1
        res, curr_sum = 0, 0

        for i in range(n):
            curr_sum += a[i]
            prefix[curr_sum - i - 1] += 1
            res += prefix[curr_sum - i - 1] - 1

        print(res)    

solve()    