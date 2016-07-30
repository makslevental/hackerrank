import copy
import sys
from collections import namedtuple
# from functools import total_ordering
old_stdin = sys.stdin
sys.stdin = open("/home/maksim/dev_projects/hackerrank/graph_theory/dijkstra/testcase2","r")

# @total_ordering
# class End(object):
#     'Sentinel object that always compares greater than any other object'
#     def __lt__(self, other):
#         return 0

def swap(heap,entry_finder,pos1,pos2):
    heap[pos1], heap[pos2] = heap[pos2], heap[pos1]  
    heap[pos1][2],heap[pos2][2] = pos1, pos2
    
def bubble_up(heap,entry_finder,pos):
    # the loop invariant is that pos is always a legal position
    # and can't go up further    
    while pos >= 0:
        prnt_pos = (pos - 1) >> 1
        if prnt_pos >=0 and heap[pos][0] < heap[prnt_pos][0]:
            swap(heap,entry_finder,pos,prnt_pos)
            pos = prnt_pos
        else:
            break
    
    return heap[pos]


def bubble_down(heap,entry_finder,pos):
    # the loop invariant is that pos is always a legal position
    # and can't go down further    
    while pos < len(heap):
        childpos = 2*pos + 1
        rchildpos = childpos + 1
        if rchildpos < len(heap) and heap[childpos][0] > heap[rchildpos][0]: # you need to switch with the smallest child
            childpos = rchildpos
        if childpos < len(heap) and heap[pos][0] > heap[childpos][0]:
            swap(heap,entry_finder,pos,childpos) 
            pos = childpos
        else:
            break
        
    return heap[pos]

def heappop(heap,entry_finder):
    if heap:
        minitem = copy.deepcopy(heap[0])
        heap[0] = heap[-1]
        heap[0][2] = 0
        del heap[-1]
        if (len(heap) > 0):
            bubble_down(heap,entry_finder, 0)
        return minitem
    else:
        raise IndexError

def heappush(heap, entry_finder, item):
    """Push item onto heap, maintaining the heap invariant."""
    item.append(len(heap))
    heap.append(item)
    return bubble_up(heap, entry_finder, len(heap)-1)

def add_task(heap, entry_finder, task, priority=0):
    entry_finder[task] = heappush(heap, entry_finder, [priority, task])

def change_priority_task(heap,entry_finder, task, new_priority):
    priority , task, pos = entry_finder[task]
    heap[pos][0] = new_priority
    if new_priority < priority:
        entry_finder[task] = bubble_up(heap,entry_finder, pos)
    elif new_priority > priority:
        entry_finder[task] = bubble_down(heap, entry_finder, pos)

def pop_task(heap, entry_finder):
    priority, task, _ = heappop(heap, entry_finder)
    del entry_finder[task] 
    return priority,task

def process():
    t = int(input().strip())
    
    for __ in range(t):
    
        heap = []                         # list of entries arranged in a heap
        entry_finder = {}               # mapping of tasks to entries
        n,m = list(map(int,input().split()))
        
        edges = [[ float("inf") if i != j else 0 for i in range(0,n+1)] for j in range(n+1)]
        for _ in range(m):
            u,v,r = list(map(int,input().split()))
            edges[v][u] = edges[u][v] = min(edges[u][v],r)
        s = int(input().strip())
        
        
        visited = set()
        ds = [float("inf") for __ in range(n+1)]
        ds[s] = 0
        add_task(heap,entry_finder,s, 0)
        for u in (i for j in (range(1,s),range(s+1,n+1)) for i in j):
            add_task(heap,entry_finder,u, float("inf"))
        while heap:
            d,u = pop_task(heap, entry_finder)
        
            visited.add(u)
            for v,r in enumerate(edges[u][1:],start=1):
                if v not in visited and ds[v] > d+r:
                    ds[v] = d+r
                    change_priority_task(heap, entry_finder,v, ds[v])
            
        print(' '.join(str(x) if x!=float("inf") else str(-1) for x in ds[1:s]+ds[s+1:]))
   
if __name__ == '__main__':
    process()
        