import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/data_structures/balanced_trees/array_and_simple_queries/input/input00.txt","r")
import random
from functools import total_ordering
import decimal

seed = random.randint(0, sys.maxsize)
# seed = 6727083362374556920
myRand = random.Random(seed)
# myRand = random.Random(7582159941452003285)
# print("seed",seed)


class EmptyTreeError(Exception):
    def __init__(self):
        self.error = "Empty tree"

class Node(object): 
    _root = None
    def get_root(self):
        return self._root
    def set_root(self,val):
        self._root = val
    root = property(get_root, set_root)
    
    
    def __init__(self,val,prty,prnt=None,lchild=None,rchild=None):
        self.prnt = prnt
        self.lchild = lchild
        self.rchild = rchild
        self.val = val
        self.prty = prty
        self.size = 1
        if self.root == None:
            self.root = self
        
    def __str__(self, *args, **kwargs):
        # return str((self.val,self.prty,self.size,(self.prnt.val,self.prnt.prty) if self.prnt else None))
        return str(self.val)
    
    # size needs to be recalculated all the way up to the root on insertions and deletions
    def recalc_size(self):
        self.size = (self.lchild.size if self.lchild else 0) + (self.rchild.size if self.rchild else 0) + 1 
        
    # always need to keep track of the root because it potentially changes
    #@property 
#     def root(self):
#         p = self
#         while p.prnt != None: 
#             p = p.prnt
#         return p
    
    def ppprint(self):
        return self.pprint([],True,[])

    # basically an inorder traversal
    # really clever
    def pprint(self,pref,isTail,sb):
        if self.rchild:
            t = pref + list("│   " if isTail else "    ")
            self.rchild.pprint(t, False, sb)
        t = pref + list("└── " if isTail else "┌── ") + list(str(self))
        sb.append(t)
        if self.lchild:
            t = pref + list("    " if isTail else "│   ")
            self.lchild.pprint(t, True, sb)
        return sb


@total_ordering        
class End(object):
    def __lt__(self,other):
        return False

BOT = End()    
        
def print_tree(tree):
     print('\n'.join(map(lambda x: ''.join(x),tree.root.ppprint())))

def rotate_left(p,r):
    
    p.rchild = r.lchild
    # idiot - don't forget to reset child parent
    if p.rchild != None:
        p.rchild.prnt = p
    r.lchild = p
    # need to adjust child of parent of p
    if p.prnt:
        if p == p.prnt.lchild:
            p.prnt.lchild = r
        else:
            p.prnt.rchild = r
    
    r.prnt = p.prnt
    p.prnt = r
    p.recalc_size()
    r.recalc_size()
     
    
def rotate_right(p,q):    
    p.lchild = q.rchild
    if p.lchild != None:
        p.lchild.prnt = p
    q.rchild = p
    
    if p.prnt:
        if p.prnt.lchild and p == p.prnt.lchild:
            p.prnt.lchild = q
        else:
            p.prnt.rchild = q
    q.prnt = p.prnt
    p.prnt = q
    p.recalc_size()
    q.recalc_size()
    

def bubble_up(p):
    while p.prnt and p.prty < p.prnt.prty:
        if p == p.prnt.lchild:
            rotate_right(p.prnt,p)
        else:
            rotate_left(p.prnt,p)
    if p.prnt == None:
        p.root = p
    

def bubble_down(p):
    
    
    if p.root == p:
        if p.lchild != None and (p.rchild == None or (p.lchild.prty < p.rchild.prty)):
            rotate_right(p,p.lchild)
            p.root = p.prnt
        elif p.rchild != None and (p.lchild == None or (p.rchild.prty < p.lchild.prty)):
            rotate_left(p,p.rchild)
            p.root = p.prnt
        
        
    while (p.lchild and p.prty > p.lchild.prty) or (p.rchild and p.prty > p.rchild.prty):      
        if p.lchild != None and (p.rchild == None or (p.lchild.prty < p.rchild.prty)):
            rotate_right(p,p.lchild)
        elif p.rchild != None and (p.lchild == None or (p.rchild.prty < p.lchild.prty)):
            rotate_left(p,p.rchild)
        
        
        
        
def insert(root,key):
    # insert and remove traversal are different: insert needs to 
    # keep going but remove needs to stop
    p = root
    while (p.lchild and key <= p.val) or (p.rchild and key > p.val):
        if p.lchild and key <= p.val:
            p = p.lchild
        else:    
            p = p.rchild
            
    if key <= p.val:
        nod = Node(key,myRand.uniform(0,1),p)    
        p.lchild = nod
    else:   
        nod = Node(key,myRand.uniform(0,1),p)    
        p.rchild = nod
    
    # recalculate tree decorations all the way up to the root
    p = nod
    while p != None: # find root
        p.recalc_size()
        p = p.prnt
    
    bubble_up(nod) 
    

            
def delete(p):
    p.prty = BOT
    bubble_down(p)
    if p.prnt:
        if p.prnt.lchild and p == p.prnt.lchild:
            p.prnt.lchild = None
        else:
            p.prnt.rchild = None
        
        while p != None: # find root
            p.recalc_size()
            p = p.prnt

    else:
        raise EmptyTreeError
    
    
def select(p,i):
    try:
        rank = (p.lchild.size if p.lchild else 0) + 1
    except:
        print(p,i)
    if i == rank:
        return p
    elif i < rank:
        return select(p.lchild,i)
    else:
        return select(p.rchild,i - rank)
    
def remove(root,key):
    p = root
    while (p.lchild and key < p.val) or (p.rchild and key > p.val):
        if p.lchild and key < p.val:
            p = p.lchild
        else:    
            p = p.rchild
    if p.val == key:
        delete(p)
    else:
        raise KeyError

def inorder(tree,sb):
    if tree == None:
        return
    inorder(tree.lchild, sb)
    sb.append(tree.val)
    inorder(tree.rchild, sb)

  
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
        
        
def split(tree,k):
    p = select(tree,k)
    old_min_prty = p.prty
    p.prty = -1
    bubble_up(p)
    rtree = p.rchild
    rtree.prnt = None
    ltree = p
    ltree.rchild = None
    ltree.prnt = None
    ltree.recalc_size()
    ltree.prty = old_min_prty
    bubble_down(ltree)
    return ltree,rtree

def double_split(tree,i,j):
    # middle portion will include i through j
    ltree, rtree = split(tree,j)
    ltree, mtree = split(ltree.root,i-1)
    return ltree, mtree, rtree

def merge(ltre,rtre):  
    avg_node = Node(None, BOT, None, ltre.root, rtre.root)
    ltre.prnt = avg_node
    rtre.prnt = avg_node
    
    avg_node.recalc_size()
    delete(avg_node)
    return ltre
    
n,m = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))
tree = Node((0,arr[0]),myRand.uniform(0,1))
tree.root = tree
for i,a in enumerate(arr[1:],start=1):
    insert(tree.root, (i,a))
# arr2 = arr[:]
# print(arr2)
# sb = []
# inorder(tree.root,sb)
# print(sb)
for _ in range(m):
    q,i,j = list(map(int,input().strip().split()))
#     print(q,i,j)
    if i == 1 and j == n:
        pass
    elif i > 1 and j < n:
        ltree, mtree, rtree = double_split(tree.root, i, j)
#         larr,marr,rarr = arr2[0:i-1],arr2[i-1:j],arr2[j:]
#         print_tree(ltree)
#         print_tree(mtree)
#         print_tree(rtree)
#         print(larr,marr,rarr)
        
        if q == 1: # to the front
            ltree = merge(mtree.root,ltree.root)
#             larr = marr + larr
        else: # to the back
            rtree = merge(rtree.root,mtree.root)
#             rarr = rarr + marr
        tree = merge(ltree.root,rtree.root)
#         arr2 = larr+rarr
    elif j == n:
        if q == 1: # to the front
            ltree, rtree = split(tree,i-1)
#             larr, rarr = arr2[:i-1],arr2[i-1:]
            tree = merge(rtree.root,ltree.root)
#             arr2 = rarr + larr
        else: # already in the back
            pass
    else: # i == 1
        if q == 1:
            pass # already in the front
        else: # to the back
            ltree, rtree = split(tree,j)
#             larr, rarr = arr2[:j], arr2[j:]
            tree = merge(rtree.root,ltree.root)
#             arr2 = rarr + larr
    tree = tree.root
#     print_tree(tree)
#     print(arr2)
sb = []
inorder(tree,sb)
print(abs(sb[0][1]-sb[-1][1]))
print(' '.join(map(str,[s[1] for s in sb])))

# print(' '.join(map(str,arr2)))