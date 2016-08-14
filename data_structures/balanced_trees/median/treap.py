import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/data_structures/balanced_trees/median/input/input08.txt","r")
import random
from functools import total_ordering
import decimal

seed = random.randint(0, sys.maxsize)
#seed = 5627733067069922840
myRand = random.Random(seed)
# myRand = random.Random(7582159941452003285)
print("seed",seed)

def remove_exponent(d):
    d = decimal.Decimal(d)
    return d.quantize(decimal.Decimal(1)) if d == d.to_integral() else d.normalize()

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
        return str((self.val,self.prty,self.size,(self.prnt.val,self.prnt.prty) if self.prnt else None))
    
    def recalc_size(self):
        self.size = (self.lchild.size if self.lchild else 0) + (self.rchild.size if self.rchild else 0) + 1 
        
    def find_root(self):
        p = self
        while p.prnt != None: # find root
            p = p.prnt
        return p
    
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

        # print(pref + (r"└── " if isTail else r"├── ") + str(self.val))
        # ls = list(iter(self))
        # for i in range(0,len(ls)-1):
        #     ls[i].pprint(pref + (r"    " if isTail else r"│   "), False)
        # if len(ls) > 0:
        #     ls[-1].pprint(pref + (r"    " if isTail else r"│   "), True)

@total_ordering        
class End(object):
    def __lt__(self,other):
        return False

BOT = End()    
        

def rotate_left(p,r):
    
    p.rchild = r.lchild
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

def bubble_down(p):
    while (p.lchild and p.prty > p.lchild.prty) or (p.rchild and p.prty > p.rchild.prty):      
        if p.lchild != None and (p.rchild == None or (p.lchild.prty < p.rchild.prty)):
            rotate_right(p,p.lchild)
        elif p.rchild != None and (p.lchild == None or (p.rchild.prty < p.lchild.prty)):
            rotate_left(p,p.rchild)
        
        
        
        
def insert(root,key):

    p = root
    while (p.lchild and key <= p.val) or (p.rchild and key > p.val):
        if p.lchild and key <= p.val:
            p = p.lchild
        else:    
            p = p.rchild
            
    if key <= p.val:
        nod = node(key,myRand.uniform(0,1),p)    
        p.lchild = nod
    else:   
        nod = node(key,myRand.uniform(0,1),p)    
        p.rchild = nod
    
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
        return p.val
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
#     print(q,i)
    if q == 'a':
        size_tree +=1
        if tree == None:
            tree = node(int(i),myRand.uniform(0,1))
        else:
            insert(tree.find_root(),int(i))
#         print('\n',  '\n'.join(map(lambda x: ''.join(x),tree.find_root().ppprint())),'\n')
        if size_tree%2 == 1:
            print(remove_exponent(select(tree.find_root(),size_tree//2+1)))
        else:
            print(remove_exponent((select(tree.find_root(),size_tree//2)+select(tree.find_root(),size_tree//2+1))/2))
        tree = tree.find_root()
    else:
        if tree == None:
            print("Wrong!")
        else:
            try:
                remove(tree.find_root(),int(i))
            except EmptyTreeError:
                tree = None
                size_tree = 0
                print("Wrong!")
                continue
            except KeyError:
                print("Wrong!")
                continue
#             print('\n',  '\n'.join(map(lambda x: ''.join(x),tree.find_root().ppprint())),'\n')
            if size_tree%2 == 1:
                print(remove_exponent(select(tree.find_root(),size_tree//2+1)))
            else:
                print(remove_exponent((select(tree.find_root(),size_tree//2)+select(tree.find_root(),size_tree//2+1))/2))
            tree = tree.find_root()
    

# tree = node(1,myRand.uniform(0,1))
# insert(tree.find_root(), 2)
# insert(tree.find_root(), -1)
# insert(tree.find_root(), -3)
# insert(tree.find_root(), 5)
# print(  '\n'.join(map(lambda x: ''.join(x),tree.ppprint())))