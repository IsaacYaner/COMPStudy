from graphviz import Digraph

dot = Digraph(edge_attr={'len':'1'})
# dot.graph_attr['minlen'] = 1
# dot.node('A', 'A')
# dot.node('B', 'B')
dot.node('C', 'C')
# dot.node('D', 'D')
# dot.node('E', 'E')
# dot.node('1', '1')
# dot.node('2', '2')
dot.node('3', '3')
# dot.node('4', '4')
# dot.node('5', '5')
# dot.edges(['2B', 'B2', '1E', 'E5', '5D', 'D4', '4A', 'A1', 'C3', '3A'])
# dot.edges(['C3', '3B', '2B', 'B2'])
dot.edges(['C3', '3C'])
dot.graph_attr['layout'] = 'neato'
# dot.engine = 'neato'
print(dot.source)
dot.render(view=True)