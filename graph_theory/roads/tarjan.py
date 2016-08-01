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
    