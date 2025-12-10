from math import sqrt
import networkx as nx

def connect_junction_boxes(string):
    """Parse the input string and return a list of junction box coordinates."""
    boxes_coords = []
    connection_pairs = []
    G = nx.Graph()
    number_of_connections = 1000
    number_of_largest_components = 3
    
    #Parse input string to extract junction box coordinates
    for line in string.strip().split("\n"):
        x, y, z = map(int, line.split(","))
        boxes_coords.append((x, y, z))

    #Create graph nodes from all the junction boxes coordinates
    G.add_nodes_from(boxes_coords)

    #Calculate all possible straight-line distances between junction boxes
    for i in range(len(boxes_coords)):
        for j in range(i + 1, len(boxes_coords)):
            dist, coord1, coord2 = straight_line_distance(boxes_coords[i], boxes_coords[j])
            connection_pairs.append((dist, coord1, coord2))

    #Find the first 1000 shortest connections between junction boxes
    #based on straight-line distance
    connection_pairs.sort(key=lambda x: x[0])
    connection_pairs = connection_pairs[:number_of_connections]

    #Add edges to the graph based on the selected connection pairs
    for dist, coord1, coord2 in connection_pairs:
        if not nx.has_path(G, coord1, coord2):
            G.add_edge(coord1, coord2, weight=dist)
        
    components = list(nx.connected_components(G))

    #get the 3 largest connected components
    components.sort(key=lambda x: len(x), reverse=True)
    largest_components = components[:number_of_largest_components]
    
    total_distance = 1

    for component in largest_components:
        total_distance *= len(component)
    


    return total_distance





def straight_line_distance(coord1, coord2):
    """Calculate the straight-line (Euclidean) distance between two 3D-coordinates."""

    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), coord1, coord2
    

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day8_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = connect_junction_boxes(lines)
    print(result)