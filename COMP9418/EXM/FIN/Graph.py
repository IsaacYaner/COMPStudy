# Visualise our graph
import graphviz
# Priority queue for Prim algorithm
import heapq as pq
import copy


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
        if name not in self.adj_list:
            self.adj_list[name] = []

    def remove_node(self, name):
        for node in self.adj_list.keys():
            if name in self.adj_list[node]:
                self.adj_list[node].remove(name)
        del self.adj_list[name]
    
    def copy(self):
        return copy.deepcopy(self)
        
    def convert_to_undirected(self):
        '''
        Assumes that the graph is directed, and creates a reversed version of every edge
        '''
        G = self.copy()
        GT = self.transpose()
        for vertex in self:
            G.adj_list[vertex] = G.adj_list[vertex] + GT.adj_list[vertex]
        return G
        
    def add_edge(self, node1, node2, weight=1, directed=True):
        # in case they don't already exist, add these nodes to the graph
        self.add_node(node1)
        self.add_node(node2)
        
        self.adj_list[node1].append(node2)
        self.edge_weights[(node1,node2)] = weight
        
        if not directed:
            self.adj_list[node2].append(node1)
            self.edge_weights[(node2,node1)] = weight
    
    def remove_outgoing_from(self, node1):
        self.adj_list[node1] = []        
           
        
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
            dot = graphviz.Graph(engine="neato", comment='Undirected graph', strict=True)        
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

    def _dfs_recursive(self, v): # This is the main DFS recursive function
        """
        argument 
        `v`, next vertex to be visited
        `colour`, dictionary with the colour of each node
        """
        self.colour[v] = 'grey' # Visited vertices are coloured 'grey'
        for w in self.adj_list[v]: # Let's visit all outgoing edges from v
            if self.colour[w] == 'white': # To avoid loops, we vist check if the next vertex hasn't been visited yet
                self._dfs_recursive(w)
        self.colour[v] = 'black' # When we finish the for loop, we know we have visited all nodes from v. It is time to turn it 'black'

    def dfs(self, start): # This is an auxiliary DFS function to create and initialize the colour dictionary
        """
        argument 
        `start`, starting vertex
        """    
        self.colour = {node: 'white' for node in self.adj_list.keys()} # Create a dictionary with keys as node numbers and values equal to 'white'
        self._dfs_recursive(start)
        return self.colour # We can return colour dictionary. It is useful for some operations, such as detecting connected components 

    def dfs_all(self):
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

    def find_cycle_r(self, v):
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
                if self.find_cycle_r(w):
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
                if self.find_cycle_r(start):
                    return True
                else:
                    return self.find_cycle_r(start)

    def topological_sort_r(self, v):
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
                self.topological_sort_r(w)
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
                self.topological_sort_r(start)
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
        # Intialise set 'visited' with vertex s
        visited = {start}
        # Initialise priority queue Q with an empty list
        Q = []
        # Initilise list tree with empty Graph object. This object will have the MST at the end of the execution
        tree = Graph()
        # Initilise the priority queue Q with outgoing edges from s
        for e in self.adj_list[start]:
            # There is a trick here. Python prioriy queues accept tuples but the first entry of the tuple must be the priority value
            pq.heappush(Q, (self.edge_weights[(start,e)], start, e))
        while len(Q) > 0:
            # Remove element from Q with the smallest weight
            weight, v, u = pq.heappop(Q)
            # If the node is already in 'visited' we cannot include it in the MST since it would create a cycle
            if u not in visited:
                # Let's grow the MST by inserting the vertex in visited
                visited.add(u)
                # Also we insert the edge in tree, use v, u, cost order
                tree.add_edge(v, u, weight=weight)
                # We iterate over all outgoing edges of u[1] (or "v" according to the algorithm)
                for e in self.adj_list[u]:
                    # We are interested in edges that connect to vertices not in 'visited' and with smaller weight than known values stored in a
                    if e not in visited:
                        # Edge e is of interest, let's store in the priority queue for future analysis
                        pq.heappush(Q, (self.edge_weights[(u,e)], u, e))        
        return tree
      
