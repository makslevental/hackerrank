import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/graph_theory/clique/test1","r")

import math
t = int(input().strip())

turin = lambda n,r: int((1/2)*(n**2 - (n%r)*math.ceil(n/r)**2 - (r-(n%r))*math.floor(n/r)**2   ))


for _ in range(t):
    n,m = list(map(int,input().strip().split()))
    bottom = 1
    top = guess = n
    f = turin(n,guess) 
    while f != m:
        if f > m:
            top = guess
        else:
            bottom = guess
        if guess == math.ceil((top+bottom)/2):
            break
        else:
            guess = math.ceil((top+bottom)/2)
            f = turin(n,guess) 
#             print(guess)
    print(guess)    

