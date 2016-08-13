import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/data_structures/balanced_trees/median/input/input00.txt","r")
import random
from functools import total_ordering

class EmptyTreeError(Exception):
    def __init__(self):
        self.error = "Empty tree"

class node(object):
    def __init__(self,val,prty,prnt=None,lchild=None,rchild=None):
        self.prnt = prnt
        self.lchild = lchild
        self.rchild = rchild
        self.val = val
        self.prty = prty
        self.size = 1
        
    def __str__(self, *args, **kwargs):
        return str(self.val)

@total_ordering        
class End(object):
    def __lt__(self,other):
        return False

BOT = End()    
        

def rotate_left(p,r):
    
    p.rchild = r.lchild
    r.lchild = p
    # need to adjust child of parent of p
    if p.prnt:
        if p == p.prnt.lchild:
            p.prnt.lchild = r
        else:
            p.prnt.rchild = r
    r.prnt = p.prnt
    p.prnt = r
    r.size = p.size
    p.size = (p.lchild.size if p.lchild else 0) + (p.rchild.size if p.rchild else 0) + 1 
    
def rotate_right(p,q):    
    p.lchild = q.rchild
    q.rchild = p
    if p.prnt:
        if p.prnt.lchild and p == p.prnt.lchild:
            p.prnt.lchild = q
        else:
            p.prnt.rchild = q
    q.prnt = p.prnt
    p.prnt = q
    q.size = p.size
    p.size = (p.lchild.size if p.lchild else 0) + (p.rchild.size if p.rchild else 0) + 1 

def bubble_up(p):
    while p.prnt and p.prty < p.prnt.prty:
        if p == p.prnt.lchild:
            rotate_right(p.prnt,p)
        else:
            rotate_left(p.prnt,p)

def bubble_down(p):
    while (p.lchild and p.prty > p.lchild.prty) or (p.rchild and p.prty > p.rchild.prty):      
        if p.rchild == None or (p.lchild.prty < p.rchild.prty):
            rotate_right(p,p.lchild)
        elif p.lchild == None or (p.rchild.prty < p.lchild.prty):
            rotate_left(p,rchild[p])
        
        
        
        
def insert(root,key):
    p = search(root,key)
    if key <= p.val:
        nod = node(key,random.uniform(0,1),p)    
        p.lchild = nod
    else:   
        nod = node(key,random.uniform(0,1),p)    
        p.rchild = nod
    bubble_up(nod)        
            
def search(root,key):
    p = root
    while (p.lchild and key <= p.val) or (p.rchild and key > p.val):
        if p.lchild and key <= p.val:
            p = p.lchild
        else:    
            p = p.rchild
    return p
        
def delete(p):
    p.val = BOT
    bubble_down(p)
    if p.prnt:
        if p.prnt.lchild and p == p.prnt.lchild:
            p.prnt.lchild = None
        else:
            p.prnt.rchild = None
    else:
        raise EmptyTreeError
    
    
def select(p,i):
    
    rank = (p.lchild.size if p.lchild else 0) + 1
    if i == rank:
        return p.val
    elif i < rank:
        return select(p.lchild,i)
    else:
        return select(p.rchild,i - rank)
    
def remove(root,key):
    p = search(root,key)
    delete(p)

def find_root(p):
    while p.prnt != None: # find root
        p = p.prnt
    return p
  
def find_succ(p):
    if p.rchild:
        p = p.rchild
        while p.lchild:
            p = p.lchild
        return p
    else:
        while p.prnt.prnt and p.prnt != p.prnt.prnt.lchild:
            p = p.prnt
        # if loop breaks because p.prnt is None
        if p.prnt.prnt == None:
            return None
        else:
            return p.prnt.prnt
        
n = int(input())
tree = None
size_tree = 0
for _ in range(n):
    q,i = input().strip().split()
    
    if q == 'a':
        size_tree +=1
        if tree == None:
            tree = node(int(i),random.uniform(0,1))
        else:
            insert(tree,int(i))
        if size_tree%2 == 1:
            print(select(find_root(tree),size_tree//2+1))
        else:
            
            print((select(find_root(tree),size_tree//2)+select(find_root(tree),size_tree//2+1))/2)
    else:
        if tree == None:
            print("Wrong!")
        else:
            try:
                remove(find_root(tree),int(i))
                size_tree -= 1
            except EmptyTreeError:
                tree = None
                print("Wrong!")
                continue
            if size_tree%2 == 1:
                print(select(find_root(tree),size_tree//2+1))
            else:
                print((select(find_root(tree),size_tree//2)+select(find_root(tree),size_tree//2+1))/2)
        
