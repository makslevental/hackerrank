import sys
old_stdin = sys.stdin
sys.stdin = open("/home/maksim/dev_projects/hackerrank/graph_theory/floyd_warshall/test","r")

n,m = list(map(int,input().strip().split()))
edges = [[float("inf") if i !=j else 0 for i in range(n+1)] for j in range(m+1)]
for _ in range(m):
    u,v,r = list(map(int,input().strip().split()))
    edges[u][v] = r
    
for k in range(1,n+1):
    for i in range(1,n+1):
        if edges[i][k] == float("inf"): continue
        for j in range(1,n+1):
            if edges[k][j] == float("inf"): continue
            edges[i][j] = min(edges[i][k]+edges[k][j],edges[i][j])
        
q = int(input().strip())
for _ in range(q):
    x,y = list(map(int,input().strip().split()))
    print(edges[x][y] if edges[x][y] != float("inf") else -1)