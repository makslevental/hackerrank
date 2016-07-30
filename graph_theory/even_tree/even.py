import sys
old_stdin = sys.stdin
sys.stdin = open("/home/maksim/dev_projects/hackerrank/graph_theory/even_tree/test2","r")


visited = set()
ans = 0


def dfs(u):
    global ans, visited
    visited.add(u)
    total_num_descendents = 0 # num of vertices in subtree rooted at u
    for v in adj[u]:
        if v not in visited:
            num_descendents = dfs(v)
            if num_descendents % 2 == 0:
                ans += 1 # each trip down the dfs is an edge. if the number of vertices is even then
                # clearly it's an edge that connects to a subtree with an eve number of vertices
            total_num_descendents += num_descendents
    return total_num_descendents+1 # don't forget to count the root

n,m = list(map(int,input().strip().split()))
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int,input().strip().split()))
    adj[u].append(v)
    adj[v].append(u)
    
dfs(1)    
print(ans)