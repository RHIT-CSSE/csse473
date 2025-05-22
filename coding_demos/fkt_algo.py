# Heavily adapted from ChatGPT conversation: 
# https://chatgpt.com/share/67ae700b-5ff8-8006-b74c-241b5a61e9c8

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.linalg import lu

VISUALIZE = True  # Set to True to visualize the graph's planar embedding


def get_planar_embedding(G: nx.Graph):
    """Get a planar embedding of the graph if it is planar."""
    is_planar, embedding = nx.check_planarity(G)
    if not is_planar:
        raise ValueError("Graph is not planar.")
    return embedding, nx.planar_layout(G)


def extract_faces(G: nx.Graph, embedding: nx.PlanarEmbedding):
    """
    Returns a list of faces in a planar embedded graph.
    """
    faces = []
    visited_half_edges = set()

    for u, v in G.edges():
        if (u, v) not in visited_half_edges:
            # This "traverse_face" method is pulling a lot of weight here
            face = embedding.traverse_face(u, v, visited_half_edges)
            faces.append(face)

    return faces


def build_dual_spanning_tree(G: nx.Graph, embedding: nx.PlanarEmbedding, T1: nx.Graph):
    """
    Construct a spanning tree of the dual graph of G based on extracted faces.
    Only adds edges between faces that share an edge *not* in T1. 
    """
    faces = extract_faces(G, embedding)
    dual = nx.Graph()

    # Create a mapping from faces to nodes in the dual graph
    face_nodes = {i: tuple(face) for i, face in enumerate(faces)}
    
    # Add nodes
    for i in face_nodes:
        dual.add_node(i)

    def get_edges(face):
        """
        From face which is list of vertices, construct list of edges in both directions
        """
        f = len(face)
        edges = set()
        for k in range(f):
            # Add edges in both directions
            edges.add((face[k], face[(k + 1) % f]))
            edges.add((face[(k + 1) % f], face[k]))
        return edges

    # Connect faces that share an edge
    for i in range(len(faces)):
        edges_i = get_edges(faces[i])
        for j in range(i + 1, len(faces)):
            edges_j = get_edges(faces[j])
            common_edges = set(edges_i) & set(edges_j)
            if not common_edges: 
                continue
            for u, v in common_edges:
                # Check whether the common edge is in T1
                if not T1.has_edge(u, v) and not T1.has_edge(v, u):
                    dual.add_edge(i, j)
                    break

    return dual, face_nodes


def pfaffian_orientation(G, embedding):
    """Find a Pfaffian orientation using the dual graph method."""
    oriented_G = nx.DiGraph()
    oriented_G.add_nodes_from(G.nodes())

    # Find a spanning tree of G and orient its edges arbitrarily
    T1 = nx.minimum_spanning_tree(G)
    oriented_G.add_edges_from(T1.edges())

    # Find a spanning tree of the dual graph that "avoids" T1
    T2, face_nodes = build_dual_spanning_tree(G, embedding, T1)
    
    # Process leaves in T2 and orient edges accordingly
    while T2.nodes:
        leaf_nodes = [v for v in T2.nodes if T2.degree(v) == 1]
        if not leaf_nodes:
            break  # Stop when no more leaves

        leaf = leaf_nodes[0]
        face = face_nodes[leaf]

        # Find the unique edge in G that is not yet oriented, and count clockwise edges
        clockwise_edges = 0
        edge_to_orient = None
        for i in range(len(face)):
            u, v = face[i], face[(i + 1) % len(face)]
            if oriented_G.has_edge(u, v):
                clockwise_edges += 1
            elif not oriented_G.has_edge(u, v) and not oriented_G.has_edge(v, u):
                edge_to_orient = (u, v)
        
        # Orient the edge based on the number of clockwise edges to ensure odd total
        if clockwise_edges % 2 == 0:
            oriented_G.add_edge(*edge_to_orient)
        else:
            oriented_G.add_edge(edge_to_orient[1], edge_to_orient[0])
        
        # Remove processed leaf from T2
        T2.remove_node(leaf)

    return oriented_G


def count_perfect_matchings(G):
    """Compute the number of perfect matchings using the FKT algorithm."""
    # Step 1: Get a planar embedding
    embedding, positions = get_planar_embedding(G)
    
    if VISUALIZE:
        nx.draw(G, pos=positions, with_labels=True)
        plt.show()
    
    # Steps 2-4: Compute the Pfaffian orientation
    oriented_G = pfaffian_orientation(G, embedding)
    
    A = nx.adjacency_matrix(oriented_G).todense()
    # Make skew-symmetric
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i, j] == 1:
                A[j, i] = -1
            elif A[j, i] == 1:
                A[i, j] = -1

    if VISUALIZE:
        print("Pfaffian orientation adjacency matrix:")
        print(A)
    
    # Step 5: Compute the Pfaffian using LU decomposition
    _, _, U = lu(A)
    # Product of diagonal of U gives determinant, possibly negative
    diag_product = np.prod(np.diag(U))
    pfaff = round(np.sqrt(abs(diag_product)))

    # Step 5, alternative to LU: directly compute determinant
    # pfaff = round(np.sqrt(np.linalg.det(A)))

    return pfaff  # Pfaffian of A gives the number of perfect matchings


if __name__ == '__main__':

    sample_graphs = {
        "grid2x2": nx.grid_graph(dim=[2, 2]),
        "grid3x2": nx.grid_graph(dim=[3, 2]),
        "complete": nx.complete_graph(4),
        "cycle": nx.cycle_graph(6), 
        "star": nx.star_graph(5),
        "grid4x4": nx.grid_graph(dim=[4, 4]), 
        "barbell4x4": nx.barbell_graph(4, 4),
        "lollipop": nx.lollipop_graph(4, 6),
        # Experiment by adding other graphs here. 
        # You can search online for inspiration, e.g., 
        # https://networkx.org/documentation/stable/reference/generators.html
    }

    for name, G in sample_graphs.items():
        print(f"\n===== Graph: {name} =====\n")
        num_perf_matchings = count_perfect_matchings(G)
        print(f"The {name} graph has {num_perf_matchings} perfect matchings.\n")
