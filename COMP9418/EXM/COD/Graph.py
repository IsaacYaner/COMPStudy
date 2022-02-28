# Visualise our graph
import graphviz
# Priority queue for Prim algorithm
import heapq as pq


class Graph():
    def __init__(self, adj_list=None):
        """
        Initialises a graph object
        arguments:
            `adj_list`, dictionary with nodes as keys and lists of adjacent nodes as value
        return:
            nothing
        """
        self.adj_list = dict()
        if adj_list is not None:
            self.adj_list = adj_list.copy() # dict with graph's adjacency list
        self.colour = dict()
        self.edge_weights = dict() # maps a tuple (node1, node2) to a number

    def __len__(self):
        '''
        return the number of nodes in the graph
        '''
        return len(self.adj_list.keys())

    def __iter__(self):
        '''
        Let a user iterate over the nodes of the graph, like:
        for node in graph:
            ... # do something
        '''
        return iter(self.adj_list.keys())
    
    def children(self, node):
        '''
        Return a list of children of a node
        '''
        return self.adj_list[node]

    def add_node(self, name):
        '''
        This method adds a node to the graph.
        '''
        if name not in self.adj_list:
            self.adj_list[name] = []

    def remove_node(self, name):
        '''
        This method removes a node, and any edges to or from the node
        '''
        for node in self.adj_list.keys():
            if name in self.adj_list[node]:
                self.adj_list[node].remove(name)
        del self.adj_list[name]
    
            
    def add_edge(self, node1, node2, weight=1, directed=True):
        '''
        This function adds an edge. If directed is false, it adds an edge in both directions
        '''
        # in case they don't already exist, add these nodes to the graph
        self.add_node(node1)
        self.add_node(node2)
        
        self.adj_list[node1].append(node2)
        self.edge_weights[(node1,node2)] = weight
        
        if not directed:
            self.adj_list[node2].append(node1)
            self.edge_weights[(node2,node1)] = weight
        
    def show(self, directed=True, positions=None):
        """
        Prints a graphical visualisation of the graph usign GraphViz
        arguments:
            `directed`, True if the graph is directed, False if the graph is undirected
            `pos: dictionary`, with nodes as keys and positions as values
        return:
            GraphViz object
        """
        if directed:
            dot = graphviz.Digraph(engine="neato", comment='Directed graph')
        else:
            dot = graphviz.Graph(engine="neato", comment='Undirected graph')        
        dot.attr(overlap="false", splines="true")
        for v in self.adj_list:
            if positions is not None:
                dot.node(str(v), pos=positions[v])
            else:
                dot.node(str(v))
        for v in self.adj_list:
            for w in self.adj_list[v]:
                dot.edge(str(v), str(w))

        return dot
    
    def _dfs_r(self, v): # This is the main DFS recursive function
        """
        argument 
        `v`, next vertex to be visited
        `colour`, dictionary with the colour of each node
        """
        print('Visiting: ', v)
        self.colour[v] = 'grey' # Visited vertices are coloured 'grey'
        for w in self.adj_list[v]: # Let's visit all outgoing edges from v
            if self.colour[w] == 'white': # To avoid loops, we check if the next vertex hasn't been visited yet
                self._dfs_r(w)
        self.colour[v] = 'black' # When we finish the for loop, we know we have visited all nodes from v. It is time to turn it 'black'

    def dfs(self, start): # This is an auxiliary DFS function to create and initialize the colour dictionary
        """
        argument 
        `start`, starting vertex
        """    
        self.colour = {node: 'white' for node in self.adj_list.keys()} # Create a dictionary with keys as node numbers and values equal to 'white'
        self._dfs_r(start)
        return self.colour # We can return colour dictionary. It is useful for some operations, such as detecting connected components
    
    def dfs_all(self, start):
        """
        Traverse the graph in DFS order. This function keep calling dfs_r while there are white vetices
        arguments: 
            `start`, starting vertex
        return:
            nothing, but self.colour is modified
        """    
        self.colour = {node: 'white' for node in self.adj_list.keys()} # Create a dictionary with keys as node numbers and values equal to 'white'
        for start in self.colour.keys():
            if self.colour[start] == 'white':
                self.dfs_recursive(start)        

    def _find_cycle_r(self, v):
        """
        Detect a cycle in the graph. This is the main recursive function based on DFS
        arguments:
            `v`, next vertex to be visited
        return:
            True if cycle is found. Otherwise, False
        """      
        print('Visiting: ', v)
        self.colour[v] = 'grey'
        for w in self.adj_list[v]:
            if self.colour[w] == 'white':
                if self._find_cycle_r(w):
                    return True
            else:
                if self.colour[w] == 'grey':
                    print(v, w, 'Cycle detected')
                    return True
        self.colour[v] = 'black'
        return False

    def find_cycle(self, start):
        """
        Detect a cycle in the graph. This is the entry function that calls find_cycle_r
        arguments:
            `v`, starting vertex
        return:
            True if cycle is found. Otherwise, False
        """        
        self.colour = dict([(node, 'white') for node in self.adj_list.keys()])
        for start in self.colour.keys():
            if self.colour[start] == 'white':
                if self._find_cycle_r(start):
                    return True
                else:
                    return self.find_cycle_r(start)

    def _topological_sort_r(self, v):
        """
        Create a list with a topological ordering of the graph nodes. This is the main recursive function based on DFS
        arguments:
            `v`, current vertex
        return:
            nothing, but modifies self.stack
        """
        self.colour[v] = 'grey'
        for w in self.adj_list[v]:
            if self.colour[w] == 'white':
                self._topological_sort_r(w)
        self.colour[v] = 'black'
        self.stack.append(v)

    def topological_sort(self):
        """
        Create a list with a topological ordering of the graph nodes. This is the entry function that calls topological_sort_r
        arguments:
            None
        return:
            a list with the topological order of the graph G
        """
        self.stack = []
        self.colour = {node: 'white' for node in self.adj_list.keys()}
        for start in self.adj_list.keys():
            if self.colour[start] == 'white':
                self._topological_sort_r(start)
        return self.stack[::-1]

    def transpose(self):
        """
        Transposes the graph creating a new graph
        arguments:
            None
        return:
            a graph object with the transposition of this object
        """      
        gt = dict((v, []) for v in self.adj_list)
        for v in self.adj_list:
            for w in self.adj_list[v]:
                gt[w].append(v)
        return Graph(gt)

    def prim(self, start):
        """
        argument 
        `start`, start vertex
        """      
        visited = {start}
        Q = []
        tree = Graph()
        for e in self.adj_list[start]:
            pq.heappush(Q, (self.edge_weights[(start,e)], start, e))
        while len(Q) > 0:
            weight, v, u = pq.heappop(Q)
            if u not in visited:
                visited.add(u)
                tree.add_edge(v, u, weight=weight)
                for e in self.adj_list[u]:
                    if e not in visited:
                        pq.heappush(Q, (self.edge_weights[(u,e)], u, e))        
        return tree