import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/dynamic_programming/max_sub_array/data/input00.txt","r")
t = int(input().strip())
for _ in range(t):
    n = input().strip()
    arr = list(map(int,input().strip().split()))
    maxx = 0
    maxx_here = 0
    disc = 0
    for a in arr:
        maxx_here = max(maxx_here+a,0)
        maxx = max(maxx,maxx_here)
        if a > 0:
            disc += a
    nmaxx = max(arr)                
    print(nmaxx if nmaxx <= 0 else maxx, nmaxx if nmaxx <= 0 else disc)   