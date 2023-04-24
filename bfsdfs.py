from collections import deque

class Graph:
    def __init__(self, num_nodes, adj_matrix):
        self.num_nodes = num_nodes
        self.adj_matrix = adj_matrix

    def bfs(self, s_node, e_node):
        queue = deque()
        visited = set()
        trace = dict()
        queue.append(s_node)
        trace[s_node] = None
        while queue:
            current_node = queue.popleft()
            if current_node == e_node:
                break
            visited.add(current_node)
            for neigh, is_conn in enumerate(self.adj_matrix[current_node-1]):
                if is_conn and neigh+1 not in visited and neigh+1 not in queue:
                    queue.append(neigh+1)
                    trace[neigh+1] = current_node
        path = []
        while e_node:
            path.append(e_node)
            e_node = trace[e_node]
        path.reverse()
        print(f"\nThe path from {s_node} to {e_node} using BFS is {' >- '.join(map(str, path))}")

    def dfs(self, s_node, e_node):
        stack = deque()
        visited = set()
        trace = dict()
        stack.append(s_node)
        trace[s_node] = None
        while stack:
            current_node = stack.pop()
            if current_node == e_node:
                break
            visited.add(current_node)
            for neigh, is_conn in enumerate(self.adj_matrix[current_node-1]):
                if is_conn and neigh+1 not in visited and neigh+1 not in stack:
                    stack.append(neigh+1)
                    trace[neigh+1] = current_node
        path = []
        while e_node:
            path.append(e_node)
            e_node = trace[e_node]
        path.reverse()
        print(f"The path from {s_node} to {e_node} using DFS is {' >- '.join(map(str, path))}")

num_nodes = int(input("Enter the number of nodes: "))
node_labels = list(range(1, num_nodes+1))
adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
for i in range(num_nodes):
    connected_nodes = list(map(int, input(f"Enter the nodes connected to {node_labels[i]} (space-separated): ").split()))
    for node in connected_nodes:
        adj_matrix[i][node-1] = 1

graph = Graph(num_nodes, adj_matrix)
s_node = int(input("\nEnter the start node: "))
e_node = int(input("Enter the end node: "))
graph.bfs(s_node, e_node)
graph.dfs(s_node, e_node)


# Enter the number of nodes: 5
# Enter the nodes connected to 1 (space-separated): 2 3
# Enter the nodes connected to 2 (space-separated): 1 3 4 5
# Enter the nodes connected to 3 (space-separated): 1 2 4
# Enter the nodes connected to 4 (space-separated): 2 3 5
# Enter the nodes connected to 5 (space-separated): 2 3

# Enter the start node: 1
# Enter the end node: 5

# The path from 1 to None using BFS is 1 >- 2 >- 5
# The path from 1 to None using DFS is 1 >- 3 >- 4 >- 5