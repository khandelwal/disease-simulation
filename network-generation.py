import networkx as nx

def generate_century_graph():
    """ Give me a random hundred node graph. """
    return nx.erdos_renyi_graph(100, 0.5)
