import random
import networkx as nx
import matplotlib.pyplot as plt
import prettytable as pt

def create_balanced_tree(num_nodes):
    return nx.balanced_tree(2, int(num_nodes/2)-1)

def create_unbalanced_tree(num_nodes):
    unbalanced_tree = nx.DiGraph()
    unbalanced_tree.add_node(0)
    for i in range(1, num_nodes):
        parent = random.randint(0, i-1)
        unbalanced_tree.add_edge(parent, i)
    return unbalanced_tree

def draw_trees(balanced_tree, unbalanced_tree):
    fig, axs = plt.subplots(ncols=2, figsize=(10, 5))
    nx.draw(balanced_tree, with_labels=True, ax=axs[0])
    axs[0].set_title('Balanced Binary Tree')
    nx.draw(unbalanced_tree, with_labels=True, ax=axs[1])
    axs[1].set_title('Unbalanced Binary Tree')
    plt.show()

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(graph[vertex]) - set(visited))
    return visited

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

def time_complexity(graph, start, traversal_func):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(graph[vertex]) - set(visited))
    return len(visited)

# Define the number of nodes
num_nodes = random.randint(8, 15)

# Create the trees
balanced_tree = create_balanced_tree(num_nodes)
unbalanced_tree = create_unbalanced_tree(num_nodes)

# Draw the trees side by side
draw_trees(balanced_tree, unbalanced_tree)

# Define the starting node
start_node = 0

# Calculate the time complexities
bfs_balanced_time = time_complexity(balanced_tree, start_node, bfs)
bfs_unbalanced_time = time_complexity(unbalanced_tree, start_node, bfs)
dfs_balanced_time = time_complexity(balanced_tree, start_node, dfs)
dfs_unbalanced_time = time_complexity(unbalanced_tree, start_node, dfs)

# display time complexities for BFS and DFS on balanced and unbalanced trees in a table
table = pt.PrettyTable()
table.field_names = ["", "BFS Balanced", "BFS Unbalanced", "DFS Balanced", "DFS Unbalanced"]
table.add_row(["Time Complexity", bfs_balanced_time, bfs_unbalanced_time, dfs_balanced_time, dfs_unbalanced_time])
print(table)

