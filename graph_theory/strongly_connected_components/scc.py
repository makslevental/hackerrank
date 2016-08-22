# this is actually from hackerearth
import sys
from functools import reduce
sys.stdin = open("/home/maksim/dev_projects/hackerrank/graph_theory/strongly_connected_components/input/input00.txt","r")

n,m = map(int,input().strip().split())
adj_mat = [[0 for _ in range(n)] for __ in range(n)]
for _ in range(m):
    u,v = map(int,input().strip().split())
    adj_mat[u-1][v-1] = 1

# print('\n'.join(map(str,adj_mat)))
visited = set()
closed = []
for u in range(n):
    if u in visited:
        continue
    visited.add(u) # visited reflects being, or having been in the stack already
    stk = [[u,0]] # 0 indicates opened
    while stk:
        l = stk[-1]
        v,t = l
        if t == 1:
            stk.pop()
            closed.append(v)
            continue
        for w,e in enumerate(adj_mat[v]):
            if w not in visited and e != 0:
                stk.append([w,0])
                visited.add(w)
        l[1] = 1 # indicates closed
# print(closed)        
transpose_mat = list(zip(*adj_mat))
# print('\n'.join(map(str,transpose_mat)))
visited.clear()
# print(visited)
scc = []
while closed:
    u = closed.pop()
    if u in visited:
        continue
    visited.add(u)
    u_component = set()
    stk = [u]
    while stk:
        v = stk.pop()
        u_component.add(v)
        for w,e in enumerate(transpose_mat[v]):
#             print(v,w,e,visited)
            if w not in visited and e != 0:
                
                stk.append(w)
                visited.add(w)
    scc.append(u_component)
# print(scc)
print(reduce(lambda x,y: x+len(y) if len(y)%2 else x-len(y),scc,0))
