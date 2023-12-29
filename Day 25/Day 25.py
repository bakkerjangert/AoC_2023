import networkx as nx


def girvan_newman_algorithm(G):
    # Make a copy of the original graph to avoid modifying it
    G_copy = G.copy()

    # Iterate until the graph is fully disconnected
    while nx.number_connected_components(G_copy) == 1:
        # Calculate edge betweenness centrality
        edge_betweenness = nx.edge_betweenness_centrality(G_copy)

        # Find the edge with the highest betweenness centrality
        max_betweenness_edge = max(edge_betweenness, key=edge_betweenness.get)

        # Remove the edge with the highest betweenness centrality
        G_copy.remove_edge(*max_betweenness_edge)

    # Identify communities based on connected components
    communities = list(nx.connected_components(G_copy))
    return communities

file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()


graph = nx.Graph()
single_connections = []
for line in data:
    key = line.split(':')[0]
    values = list(line.split(': ')[1].split(' '))
    for value in values:
        graph.add_edge(key, value)
        single_connections.append((key, value))

for i in range(len(single_connections) - 2):
    for j in range(i + 1, len(single_connections) - 1):
        for k in range(j + 1, len(single_connections) - 1):
            sub_graph = graph.copy()
            sub_graph.remove_edge(single_connections[i][0], single_connections[i][1])
            sub_graph.remove_edge(single_connections[j][0], single_connections[j][1])
            sub_graph.remove_edge(single_connections[k][0], single_connections[k][1])
            communities = girvan_newman_algorithm(sub_graph)
            if len(communities) == 2:
                print(f'Part 1: {len(communities[0]) * len(communities[1])}')
                exit()
