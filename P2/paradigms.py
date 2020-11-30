# Practica 2

## Problema 2.1

### Divide and Conquer
def maxsum_subseq_dnc(lst):
    '''lst is a list of integers'''
    #TODO
    pass

### Dynamic Programming
def maxsum_subseq_dp(lst):
    '''lst is a list of integers'''
    #TODO
    pass

##Problema 2.2

class Graph:
    def __init__(self, edge_list):
        self.nverts = max(map(max, edge_list)) + 1

        self._adjacent = dict(map(lambda x: (x, set()), range(self.nverts)))
        for v_a, v_b in edge_list:
            self._adjacent[v_a].add(v_b)
            self._adjacent[v_b].add(v_a)

    def get(self, x):
        if x < self.nverts:
            return list(self._adjacent[x])
        else:
            raise AttributeError(f'Value {x} is not a vertex in this graph.')


### Greedy
def coloring_greedy(graph):
    '''graph is an instance of class Graph'''
    #TODO
    pass

### Backtrack
def coloring_backtrack(graph, n):
    '''graph is an instance of class Graph, n is the maximum number of colors to be used'''
    #TODO
    pass
