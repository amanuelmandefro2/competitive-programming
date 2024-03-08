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
    n=I()
    x= IL()
    v=IL()
    x_v = [[x[i],v[i]] for i in range(n)]
    x_v.sort()

    def helper(mid): 
        limit = x_v[0][0]+mid*x_v[0][1]
        for i in range(n):
            if limit >= x_v[i][0]:
                limit =min(limit , x_v[i][0]+x_v[i][1]*mid)
            else:
                if x_v[i][0] - x_v[i][1]*mid >limit:
                    return False
        return True

    l,r=0, max(x) - min(x)
    ans = 0
    while l + 0.000001 < r:
        mid=(r+l)/2
        if helper(mid):
            r=mid 
            ans=mid
        else:
            l=mid 
    print(ans)
solve()    


