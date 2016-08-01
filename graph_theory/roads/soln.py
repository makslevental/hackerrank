import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/graph_theory/roads/input/input00.txt", "r")
n, m = list(map(int, input().strip().split()))
e = []
for i in range(m):
    u, v, c = list(map(int, input().strip().split()))
    e.append((c, u - 1, v - 1))

parent = [i for i in range(n)]
rank = [1 for i in range(n)]


def find_set(v):
    global parent
    if parent[v] != v:
        parent[v] = find_set(parent[v])
    return parent[v]


e.sort()

g = [[] for i in range(n)]

# compute mst using kruskal
for (c, u, v) in e:
    a, b = find_set(u), find_set(v)
    if a != b:
        if rank[a] > rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            rank[a] += 1
            parent[b] = a
        g[u].append((v, c))
        g[v].append((u, c))

ans = [0] * (m * 2)

summ = 0
# count how many times each edge in the MST is used
def dfs(v, p=-1):
    global ans
    cur_size = 1
    for (to, c) in g[v]:
        if to != p:
            sz = dfs(to, v)
            # sz number of vertices on the other side of the edge
            # (n-sz) number of on this side. that means sz*(n-sz) paths 
            # use this edge
            ans[c] += sz * (n - sz)
            summ += c*sz*(n-sz)
            cur_size += sz
    return cur_size

dfs(0)
print(summ)

# surprisingly this is faster than python's bin
for i in range(len(ans) - 1):
    ans[i + 1] += ans[i] // 2
    ans[i] %= 2
    print(i,ans) 
flag = False
real_ans = []
for i in range(len(ans) - 1, -1, -1):
    if flag or ans[i] > 0:
        flag = True
        real_ans.append(ans[i])
print( "".join(map(str, real_ans)))