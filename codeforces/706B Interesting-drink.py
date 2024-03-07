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
    n = I()
    x = IL()
    x.sort()
    for _ in range( I()):
        m = I()
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if x[mid] <= m:
                l = mid + 1
            else: r = mid -1
           
        print(l)        





solve()    