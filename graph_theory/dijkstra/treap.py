from functools import total_ordering
import random

def treapnode(key,priority,prnt,lchild,rchild):
    return {'key':key,'priority':priority,'prnt':prnt,'lchild':lchild,'rchild':rchild}
    
# greater than any priority (never lt)
@total_ordering
class End(object):
    def __lt__(self,other):
        return 0

def rotateleft(root,rchild):
    
    root['rchild'] = rchild['lchild']
    rchild['lchild'] = root
    
    #fix parent relationships
    if root == root['prnt']['lchild']:
        root['prnt']['lchild'] = rchild
    else:
        root['prnt']['rchild'] = rchild
        
    rchild['prnt'] = root['prnt']
    root['prnt'] = rchild
    root['rchild']['prnt'] = root
      
def rotateright(root,lchild):
    root['lchild'] = lchild['rchild']
    lchild['rchild'] = root
    
    if root == root['prnt']['lchild']:
        root['prnt']['lchild'] = lchild
    else:
        root['prnt']['rchild'] = lchild
        
    lchild['prnt'] = root['prnt']
    root['lchild']['prnt'] = root
    root['prnt'] = lchild    
    
def bubble_down(node):
    while node['lchild'] or node['rchild']:
        if node['lchild'] and node['rchild'] and node['rchild']['priority'] < node['lchild']['priority']:
            if node['rchild']['priority'] < node['priority']:
                rotateleft(node, node['rchild'])
        if node['lchild'] and node['lchild']['priority'] < node['priority']:
            rotateright(node,node['lchild'])
        else:
            break
        
def bubble_up(node):
    while node['prnt']:
        if node['priority'] < node['prnt']['priority']:
            if node == node['prnt']['rchild']:
                rotateleft(node['prnt'], node)
            else:
                rotateright(node['prnt'],node)
        else:
            break

def insert(root,key):
    # invariant: root != None
    while root['rchild'] or root['lchild']:
        if root['key'] <= key and root['rchild']:
            root = root['rchild']
        elif root['key'] > key and root['lchild']:
            root = root['lchild']
        else:
            break
            
    newnode = treapnode(key, random.uniform(0,1), None, None,None)
    if root['key'] <= key:
        root['rchild'] = newnode
    else:
        root['lchild'] = newnode
        
    return newnode

def delete(node):
    def reassignprnt(nodeschild):
        if node == node['prnt']['lchild']:
            node['prnt']['lchild'] = nodeschild
        else:
            node['prnt']['rchild'] = nodeschild

    if node['lchild'] or node['rchild']:
        if not node['lchild']:
            reassignprnt(node['rchild'])
        elif not node['rchild']:
            reassignprnt(node['lchild'])
        else:
            node['value'] = End()
            bubble_down(node)
    else:
        reassignprnt(None)
    
    
    

    