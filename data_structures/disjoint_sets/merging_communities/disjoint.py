import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/disjoint_sets/merging_communities/input/input01.txt", "r")

n, m = map(int, input().strip().split())

roots = [i for i in range(n + 1)]
sizes = [1 for i in range(n + 1)]

def find_set(i):
    global roots
    if i != roots[i]:
        roots[i] = find_set(roots[i])
    return roots[i]

def merge(i, j):
    global roots, sizes
    a, b = find_set(i), find_set(j)
    if a != b:
        if sizes[a] > sizes[b]:
            roots[b] = a
            sizes[a] += sizes[b]
            sizes[b] = None
        elif sizes[b] > sizes[a]:
            roots[a] = b
            sizes[b] += sizes[a]
            sizes[a] = None
        else:
            roots[a] = b
            sizes[b] += sizes[a]
            sizes[a] = None
            
for _ in range(m):
    arr = input().strip().split()
    if arr[0] == 'Q':
        print(sizes[find_set(int(arr[1]))])
    else:
        i, j = map(int, arr[1:])
        merge(i, j)
