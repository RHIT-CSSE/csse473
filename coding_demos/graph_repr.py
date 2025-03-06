import networkx as nx
"""
Graph representations: 
Adjacency matrix vs. adjacency list. 

Demonstration using the NetworkX library. 

Author: Ian Ludden
Date: 2025-03-06
Course: CSSE/MA 473
"""

if __name__ == '__main__':
    DIRECTED = True

    # Create example directed graph
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    positions = {
        'a': (0, 1),
        'b': (1, 1),
        'c': (2, 1),
        'd': (0, 0),
        'e': (1, 0),
        'f': (2, 0),  
        'g': (3, 0.5)
    }
    edges = [('a', 'b'), ('a', 'd'), ('a', 'e'), 
             ('b', 'c'), 
             ('c', 'b'), 
             ('d', 'e'), 
             ('e', 'b'), ('e', 'd'), 
             ('f', 'c'), ('f', 'e'), ('f', 'g')]
    
    # Create NetworkX graph object
    G = nx.Graph()
    if DIRECTED:
        G = nx.DiGraph()
    
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Set node positions for visualization
    nx.set_node_attributes(G, positions, 'pos')

    # Draw graph
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 4))
    nx.draw(G, pos=positions, with_labels=True, node_size=500, node_color='lightblue')
    plt.show()

    # Print adjacency matrix
    print('Adjacency matrix:')
    A = nx.adjacency_matrix(G).todense()
    print(A)
    print('Symmetric? ', "Yes" if (A == A.T).all() else "No")
    print()

    # Print adjacency lists
    print('Adjacency lists:')
    for node in G.nodes:
        print(f'{node}: {list(G.neighbors(node))}')
