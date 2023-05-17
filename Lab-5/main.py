import random
import timeit
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def generate_sparse_graph(num_nodes, num_edges):
    if num_edges < num_nodes - 1:
        raise ValueError("Invalid number of edges for a sparse graph.")

    graph = nx.Graph()

    # Add nodes to the graph
    graph.add_nodes_from(range(num_nodes))

    # Create a list of all possible edges
    all_edges = [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)]

    # Shuffle the list of edges
    random.shuffle(all_edges)

    # Add edges to the graph until the desired number of edges is reached
    for edge in all_edges[:num_edges]:
        graph.add_edge(*edge)

    return graph


def generate_dense_graph(num_nodes, num_edges):
    if num_edges > (num_nodes * (num_nodes - 1)) // 2:
        raise ValueError("Invalid number of edges for a dense graph.")

    graph = nx.Graph()

    # Add nodes to the graph
    graph.add_nodes_from(range(num_nodes))

    # Create a list of all possible edges
    all_edges = [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)]

    # Shuffle the list of edges
    random.shuffle(all_edges)

    # Add edges to the graph until the desired number of edges is reached
    for edge in all_edges[:num_edges]:
        graph.add_edge(*edge)

    return graph


def dijkstra_algorithm(graph, start_node):
    shortest_paths = {}

    # Run Dijkstra's algorithm on the graph
    for node in graph.nodes():
        if node == start_node:
            shortest_paths[node] = 0
        else:
            shortest_paths[node] = float('inf')

    while len(shortest_paths) != len(graph.nodes()):
        min_distance = float('inf')
        min_node = None

        for node in graph.nodes():
            if node not in shortest_paths:
                continue

            if shortest_paths[node] < min_distance:
                min_distance = shortest_paths[node]
                min_node = node

        for neighbor in graph.neighbors(min_node):
            if neighbor not in shortest_paths:
                shortest_paths[neighbor] = float('inf')

            new_distance = shortest_paths[min_node] + graph[min_node][neighbor]['weight']

            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance

    return shortest_paths


# Example usage for sparse graph
num_nodes_sparse = 10
num_edges_sparse = 15

sparse_graph = generate_sparse_graph(num_nodes_sparse, num_edges_sparse)

# Draw the sparse graph
nx.draw(sparse_graph, with_labels=True)
plt.title("Sparse Graph")
plt.show()

start_node = 0
shortest_paths_sparse = dijkstra_algorithm(sparse_graph, start_node)

print("Shortest Paths from node", start_node)
for node, distance in shortest_paths_sparse.items():
    print("Node:", node, "Distance:", distance)

# Example usage for dense graph
num_nodes_dense = 10
num_edges_dense = 30

dense_graph = generate_dense_graph(num_nodes_dense, num_edges_dense)

# Draw the dense graph
nx.draw(dense_graph, with_labels=True)
plt.title("Dense Graph")
plt.show()

start_node = 0
shortest_paths_dense = dijkstra_algorithm(dense_graph, start_node)
# print("Shortest Paths from node", start_node)
# for node, distance in shortest_paths_dense.items():
# print("Node:", node, "Distance:", distance)


def floyd_warshall_algorithm(graph):
    # Initialize the distance matrix with infinity for all pairs
    num_nodes = graph.number_of_nodes()
    dist = np.full((num_nodes, num_nodes), np.inf)

    for node in graph.nodes():
        dist[node][node] = 0

    # Update the distance matrix with the edge weights
    for u, v, weight in graph.edges.data('weight', default=1):
        dist[u][v] = weight
        dist[v][u] = weight

    # Run the Floyd-Warshall algorithm
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example usage for sparse graph
num_nodes_sparse = 10
num_edges_sparse = 15

sparse_graph = generate_sparse_graph(num_nodes_sparse, num_edges_sparse)

# Draw the sparse graph
nx.draw(sparse_graph, with_labels=True)
plt.title("Sparse Graph")
plt.show()

shortest_paths_sparse = floyd_warshall_algorithm(sparse_graph)

# print("Shortest Paths:")
# print(shortest_paths_sparse)

# Example usage for dense graph
num_nodes_dense = 10
num_edges_dense = 30

dense_graph = generate_dense_graph(num_nodes_dense, num_edges_dense)

# Draw the dense graph
nx.draw(dense_graph, with_labels=True)
plt.title("Dense Graph")
plt.show()

shortest_paths_dense = floyd_warshall_algorithm(dense_graph)


# print("Shortest Paths:")
# print(shortest_paths_dense)


def calculate_time_complexity_dijkstra(graph_generation_func):
    num_nodes_list = []
    time_sparse_list = []
    time_dense_list = []

    for num_nodes in range(10, 101, 10):
        num_edges_sparse = num_nodes + random.randint(0, num_nodes)
        num_edges_dense = (num_nodes * (num_nodes - 1)) // 2

        sparse_graph = graph_generation_func(num_nodes, num_edges_sparse)
        dense_graph = graph_generation_func(num_nodes, num_edges_dense)

        # Measure the execution time of Dijkstra's algorithm for sparse graph
        start_time = timeit.default_timer()
        dijkstra_algorithm(sparse_graph, 0)
        end_time = timeit.default_timer()
        execution_time_sparse = end_time - start_time

        # Measure the execution time of Dijkstra's algorithm for dense graph
        start_time = timeit.default_timer()
        dijkstra_algorithm(dense_graph, 0)
        end_time = timeit.default_timer()
        execution_time_dense = end_time - start_time

        num_nodes_list.append(num_nodes)
        time_sparse_list.append(execution_time_sparse)
        time_dense_list.append(execution_time_dense)

    return num_nodes_list, time_sparse_list, time_dense_list

# display the time complexity for Dijkstra's algorithm for sparse and dense graphs using matplotlib
num_nodes_list, time_sparse_list, time_dense_list = calculate_time_complexity_dijkstra(generate_sparse_graph)
plt.plot(num_nodes_list, time_sparse_list, label="Sparse Graph")
plt.plot(num_nodes_list, time_dense_list, label="Dense Graph")
plt.xlabel("Number of Nodes")
plt.ylabel("Execution Time (s)")
plt.title("Dijkstra's Algorithm Time Complexity")
plt.legend()
plt.show()

def calculate_time_complexity_floyd_warshall(graph_generation_func):
    num_nodes_list = []
    time_sparse_list = []
    time_dense_list = []

    for num_nodes in range(10, 101, 10):
        num_edges_sparse = num_nodes + random.randint(0, num_nodes)
        num_edges_dense = (num_nodes * (num_nodes - 1)) // 2

        sparse_graph = graph_generation_func(num_nodes, num_edges_sparse)
        dense_graph = graph_generation_func(num_nodes, num_edges_dense)

        # Measure the execution time of Floyd-Warshall algorithm for sparse graph
        start_time = timeit.default_timer()
        floyd_warshall_algorithm(sparse_graph)
        end_time = timeit.default_timer()
        execution_time_sparse = end_time - start_time

        # Measure the execution time of Floyd-Warshall algorithm for dense graph
        start_time = timeit.default_timer()
        floyd_warshall_algorithm(dense_graph)
        end_time = timeit.default_timer()
        execution_time_dense = end_time - start_time

        num_nodes_list.append(num_nodes)
        time_sparse_list.append(execution_time_sparse)
        time_dense_list.append(execution_time_dense)

    return num_nodes_list, time_sparse_list, time_dense_list


# display the time complexity for Floyd-Warshall algorithm for sparse and dense graphs using matplotlib
num_nodes_list, time_sparse_list, time_dense_list = calculate_time_complexity_floyd_warshall(generate_sparse_graph)
plt.plot(num_nodes_list, time_sparse_list, label="Sparse Graph")
plt.plot(num_nodes_list, time_dense_list, label="Dense Graph")
plt.xlabel("Number of Nodes")
plt.ylabel("Execution Time (s)")
plt.title("Floyd-Warshall Algorithm Time Complexity")
plt.legend()
plt.show()


