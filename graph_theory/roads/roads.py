import sys
from collections import deque 
import decimal
from matplotlib.mlab import dist
import math
from functools import total_ordering
# import tarjan
sys.stdin = open("/home/maksim/dev_projects/hackerrank/graph_theory/roads/input/input13.txt", "r")

class Tarjan(object):
    
    def __init__(self,pairs,num_vertices,edges_ls):
        self.pairs = pairs
        self.num_vertices = num_vertices
        self.edges_ls = edges_ls
        self.lcas = None
        self.edges = None
        
        self.lcas = [[None for i in range(self.num_vertices+1)] for j in range(self.num_vertices+1)]
        self.edges = [[None for i in range(self.num_vertices+1)] for j in range(self.num_vertices+1)]
        for u,v in self.edges_ls:
            self.edges[u][v]  = 1
    
        self.sets = {}
        self. done = set()
        
    def lca(self,u):
    #     print(u)
        
        self.sets[u] = {'elems':set([u]), 'ancestor':u} #make set
        self.sets[u]['ancestor'] = u #find-set.ancestor
        for v,w in enumerate(self.edges[u][1:],start=1):
            if w != None:
                self.lca(v)
                self.sets[u]['elems'].update(self.sets[v]['elems']) #union
                for y in self.sets[u]['elems']:
                    self.sets[y] = self.sets[u] # union
                self.sets[u]['ancestor'] = u # #find-set.ancestor
        self. done.add(u)
        if u in self.pairs:
            for v in self.pairs[u]:
                if v in self.done:
                    self.lcas[u][v] = self.sets[v]['ancestor'] 
    
    

# print('\n'.join(map(str,edges)))





@total_ordering
class End(object):
    def __lt__(self,other):
        return 0

END = End()
# @total_ordering
# class End(object):
#     'Sentinel object that always compares greater than any other object'
#     def __lt__(self, other):
#         return 0
    

def bfs(u):
    que = deque([u])
    ds = [END for _ in range(n+1)]
    ds[u] = 0
    prnts = {}
    visited = set()
    while que:
        u = que.popleft()
        if u not in visited:
            visited.add(u)
            for v,w in enumerate(mst_edges[u][1:],start=1):
                if w != END:
                    if ds[v] > ds[u]+w:
                        ds[v] = ds[u]+w
                        prnts[v] = u
                        que.append(v)
#         print(ds)
            
    return prnts,ds
                
    

n,m = list(map(int,input().strip().split()))
edges = [[END if i !=j else 0 for i in range(n+1)]  for j in range(m+1)]
weight_dict = {}
for _ in range(m):
    u,v,r = list(map(int,input().strip().split()))
    edges[u][v] = edges[v][u] = min(2**r,edges[u][v],edges[v][u])
    weight_dict[edges[u][v]] = (u,v)

sorted_edges = sorted(weight_dict.keys())
disjoint_sets = {u:set([u]) for u in range(1,n+1)}
mst = []
for w in sorted_edges:
    u,v = weight_dict[w]
    if disjoint_sets[u] != disjoint_sets[v]:
        disjoint_sets[u].update(disjoint_sets[v])
        disjoint_sets[v] = disjoint_sets[u]
        mst.append((u,v))
        if len(disjoint_sets[u]) == n:
            break
# print(mst)            

# print("mst done")
mst_edges = [[END if i !=j else 0 for i in range(n+1)]  for j in range(m+1)]
for u,v in mst:
    r = edges[u][v]
    mst_edges[u][v] = mst_edges[v][u] = int(min(r,mst_edges[u][v],mst_edges[v][u]))

prnts,ds = bfs(1)
# # print(prnts)
# tarjan.num_vertices = n
# tarjan.edges_ls =
# # print(tarjan.edges_ls)
# tarjan.pairs = 
# for key,value in tarjan.pairs.items():
#     print(key,value)

tarjan = Tarjan({k:list(i for j in (range(1,k),range(k+1,n+1)) for i in j) for k in range(1,n+1)}, n, [(prnts[i],i) for i in range(2,n+1)])
tarjan.lca(1)
                            
# print('\n'.join(map(str,tarjan.lcas)))
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if tarjan.lcas[i][j] == None:
            tarjan.lcas[i][j] = tarjan.lcas[j][i]
        elif tarjan.lcas[j][i] == None:
            tarjan.lcas[j][i] = tarjan.lcas[i][j]

# print('\n'.join(map(str,tarjan.lcas)))

summ = 0

for i in range(1,n+1):
    for j in range(i+1,n+1):
        summ += ds[i] + ds[j] - 2*ds[tarjan.lcas[i][j]]
        
print(bin(summ)[2:])        




