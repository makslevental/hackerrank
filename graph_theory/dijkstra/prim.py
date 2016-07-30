import copy

import sys

def swap(pos1,pos2):
    heap[pos1], heap[pos2] = heap[pos2], heap[pos1]
    heap[pos1][2], heap[pos2][2] = pos1, pos2

def bubble_up(pos):
    # loop invariant: pos is a legal position
    # and heap[pos] >= heap[prnt_pos]
    while pos >= 0:
        prnt_pos = (pos-1) >> 1
        if prnt_pos >=0 and heap[prnt_pos][0] > heap[pos][0]:
            swap(prnt_pos,pos)
            pos = prnt_pos
        else:
            break
    return heap[pos]        

def bubble_down(pos):
    while pos < len(heap):
        childpos = 2*pos + 1
        rchildpos = childpos + 1
        if rchildpos < len(heap) and heap[rchildpos][0] < heap[childpos][0]:
            childpos = rchildpos
        if childpos < len(heap) and heap[pos][0] > heap[childpos][0]:
            swap(pos,childpos)
            pos = childpos
        else:
            break
    return heap[pos]

def heap_push(item, priority):
    heap.append([priority,item,len(heap)])
    entry_finder[item] = bubble_up(len(heap)-1)
    
def heap_pop():
    if heap:
        minitem = copy.deepcopy(heap[0])
        heap[0] = heap[-1]
        heap[0][2] = 0
        del heap[-1]
        if len(heap) > 0:
            bubble_down(0)
        return minitem
    else:
        raise IndexError
    return minitem
def pop_task():
    w,u,_ = heap_pop()
    del entry_finder[u]
    return w,u
        
def change_priority(item,new_priority):
    old_priority,item,pos = entry_finder[item]
    heap[pos][0] = new_priority
    if new_priority < old_priority:
        bubble_up(pos)        
    elif new_priority > old_priority:
        bubble_down(pos)
    

    
    
n,m = list(map(int,input().strip().split()))
edges = [[float("inf") if i!=j else 0 for i in range(n+1)] for j in range(n+1)]
for _ in range(m):
    u,v,r = list(map(int,input().strip().split()))
    edges[u][v] = edges[v][u] = min(edges[u][v],r)

src = int(input().strip())
heap = []
entry_finder = {}

ws = [float("inf") for _ in range(n+1)]
ws[0] = ws[src] = 0
heap_push(src,0)
for u in (i for j in (range(1,src),range(src+1,n+1)) for i in j):
    heap_push(u,float("inf"))
    
added = set()

while heap:
    w,u = pop_task()
    added.add(u)
    for v,r in enumerate(edges[u][1:],start=1):
        if v not in added and ws[v] > r:
            ws[v] = r
            change_priority(v,r)
            
print(sum(ws))

        


    
