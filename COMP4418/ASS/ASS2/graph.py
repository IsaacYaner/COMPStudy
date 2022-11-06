from graphviz import Digraph

dot = Digraph(edge_attr={'len':'1.5'})
# dot.graph_attr['minlen'] = 1
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.node('D', 'D')
dot.edges(['DC', 'DB', 'DA', 'CB', 'CA', 'BA'])
dot.graph_attr['layout'] = 'neato'
# dot.engine = 'neato'
print(dot.source)
dot.render(view=True)