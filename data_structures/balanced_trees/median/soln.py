from collections import Counter
import decimal
def remove_exponent(d):
    d = decimal.Decimal(d)
    return d.quantize(decimal.Decimal(1)) if d == d.to_integral() else d.normalize()

import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/data_structures/balanced_trees/median/input/input01.txt","r")

class MultiSet(Counter):
    def __init__(self):
        super().__init__()
        self.size = 0
        self.min = None
        self.max = None
        
    def put(self,x):
        if x in self:
            self[x] += 1
        else:
            self[x] = 1
            self.min = min(self.min,x) if self.min != None else x
            self.max = max(self.max,x) if self.max != None else x
        self.size +=1
        assert self.size == sum(self.values())
    
    def remove(self,x):
        if x not in self:
            raise KeyError
        else:
            if self[x] > 1:
                self[x] -= 1
            else:
                del self[x]
                if x == self.min:
                    self.min = min(self.keys()) if len(self.keys()) > 0 else None
                if x == self.max:
                    self.max = max(self.keys()) if len(self.keys()) > 0 else None
            self.size -=1
        assert self.size == sum(self.values())
                
class Median(object):
    def __init__(self):
        self.minn = MultiSet()
        self.maxx = MultiSet()
    
    def insert(self,x):
        if self.maxx.min != None and x >= self.maxx.min:
            self.maxx.put(x)
        else:
            self.minn.put(x)
        self.rebalance()

    def remove(self,x):
        if x in self.minn:
            self.minn.remove(x)
        elif x in self.maxx:
            self.maxx.remove(x)
        else:
            raise KeyError
        self.rebalance()
    
    def median(self):
        if self.minn.size > self.maxx.size:
            return self.minn.max
        elif self.maxx.size > self.minn.size:
            return self.maxx.min
        else:
            if (self.minn.max != None) and (self.maxx.min != None):
                return (self.minn.max + self.maxx.min)/2 
            else:
                raise KeyError
        
    def rebalance(self):
        if self.minn.size > self.maxx.size + 1:
            self.maxx.put(self.minn.max)
            self.minn.remove(self.minn.max)
        elif self.maxx.size > self.minn.size + 1:
            self.minn.put(self.maxx.min)
            self.maxx.remove(self.maxx.min)
        

n = int(input())
m = Median()
for _ in range(n):
    q,i = input().strip().split()
    if q == 'a':
        m.insert(int(i))
        print(remove_exponent(m.median()))
    else:
        try:
            m.remove(int(i))
            print(remove_exponent(m.median()))
        except KeyError: # just an artifact of the problem statement: removing nonexistent key means wrong
            print("Wrong!")
            continue
