from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


graph = Graph()

'''
edges = [
('Bangalore', 'Hubli', 464),
('Bangalore', 'Dharwad', 518),
('Hubli', 'Dharwad', 141)]
'''

edges = [('Mysore', 'Mandya', 66),
('Mysore', 'Chennapatna', 28),
('Mysore', 'Nanjangud', 60),
('Mysore', 'Bandipur', 34),
('Mysore', 'Nagarhole', 34),
('Mysore', 'Somnathpur', 3),
('Mysore', 'Bylakuppe', 108),
('Mandya', 'Chennapatna', 22),
('Mandya', 'Nanjangud', 12),
('Mandya', 'Bandipur', 91),
('Mandya', 'Nagarhole', 121),
('Mandya', 'Somnathpur', 111),
('Mandya', 'Bylakuppe', 71),
('Chennapatna', 'Nanjangud', 39),
('Chennapatna', 'Bandipur', 113),
('Chennapatna', 'Nagarhole', 130),
('Chennapatna', 'Somnathpur', 35),
('Chennapatna', 'Bylakuppe', 40),
('Nanjangud', 'Bandipur', 63),
('Nanjangud', 'Nagarhole', 21),
('Nanjangud', 'Somnathpur', 57),
('Nanjangud', 'Bylakuppe', 83),
('Bandipur', 'Nagarhole', 9),
('Bandipur', 'Somnathpur', 50),
('Bandipur', 'Bylakuppe', 60),
('Nagarhole', 'Somnathpur', 27),
('Nagarhole', 'Bylakuppe', 81),
('Somnathpur', 'Bylakuppe', 90)]


for edge in edges:
    graph.add_edge(*edge)


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        print(next_destinations)
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        
        
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


dijsktra(graph, 'Mysore','Nanjangud')
