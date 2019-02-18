import matplotlib.pyplot as plt
import networkx as nx

graph_1 = {
    'S': set(['A', 'D']),
    'A': set(['S', 'B']),
    'D': set(['S', 'E']),
    'B': set(['A', 'E', 'C']),
    'C': set(['B']),
    'E': set(['D', 'B', 'F']),
    'F': set(['E', 'G']),
    'G': set(['F'])
}
graph_2 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}


def create_arrow_graph(graph_nodes):
    graph = nx.Graph()
    for k, v in graph_nodes.items():
        graph.add_node(k)
    for k, v in graph_nodes.items():
        for each in v:
            graph.add_edge(k, each)

    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()


def dfs(graph, start):
    visited, stack = list(), [start]
    while stack:
        print('\n')
        print('visited =>' + str(visited))
        print('stack =>'+str(stack))
        vertex = stack.pop()
        print('vertex =>' + str(vertex))
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(item for item in list(graph[vertex]) if item not in visited)
    return visited


def bfs(graph, start):
    visited,  queue = list(), [start]
    while queue:
        print('\n')
        print('visited =>' + str(visited))
        print('queue =>'+str(queue))
        vertex = queue.pop(0)
        print('vertex =>' + str(vertex))
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(item for item in list(graph[vertex]) if item not in visited)
    return visited


if __name__ == '__main__':

    # create_arrow_graph(graph_1)
    # print(dfs(graph_2, 'A'))
    print(bfs(graph_1, 'S'))
