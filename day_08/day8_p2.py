from math import sqrt
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle # Used to cycle through colors

# Define a palette of distinct colors for the components
COLOR_PALETTE = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe']
COLOR_CYCLE = cycle(COLOR_PALETTE)
PERMANENT_COLOR_MAP = {}

def connect_junction_boxes(string):
    """Parse the input string and return a list of junction box coordinates."""
    boxes_coords = []
    connection_pairs = []
    G = nx.Graph()

    
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


    final_coord1 = None
    final_coord2 = None

    #Comment if theres no plotting needed
    # --- DYNAMIC PLOTTING INITIALIZATION FIX ---
    plt.ion()  # Turn on interactive mode for live updating plots
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    Edge_count = 0
    # --- END INITIALIZATION ---

    #Add edges to the graph based on the selected connection pairs
    
    for dist, coord1, coord2 in connection_pairs:

        if not nx.has_path(G, coord1, coord2):
            G.add_edge(coord1, coord2, weight=dist)
            Edge_count += 1
            #Comment if theres no plotting needed
            if Edge_count % 10 == 0 or Edge_count == len(boxes_coords) - 1:
                create_3D_plot(G)
            ###########################################################
            if(len(list(nx.connected_components(G)))==1):
                final_coord1 = coord1
                final_coord2 = coord2
                break
        
    
    plt.ioff()#Turn off interactive plotting
    plt.show()#Show the final plot
    
    #Ensure final_coord1 and final_coord2 are not None before calculation
    if final_coord1 and final_coord2:
        return final_coord1[0] * final_coord2[0]
    else:
        #Handle case where graph could not be fully connected (shouldn't happen here)
        return "Graph could not be fully connected."



def create_3D_plot(G):
    """Draws the graph in 3D, coloring nodes persistently by connected component."""

    #Clear the previous plot (if any)
    plt.cla()
    ax = plt.gca() 

    #Declare global variables
    global COLOR_CYCLE 
    global PERMANENT_COLOR_MAP # <-- Use the new map globally

    #Map Nodes to Position and Component Color
    node_coords = {}
    X, Y, Z = [], [], []
    node_colors = []
    plot_color_map = {} # This map assigns the final color to each node

    #Get all connected components
    components_list = list(nx.connected_components(G))
    
    # --- Persistence Logic ---
    
    #Determine the ID for each component and assign/retrieve its color
    for component_set in components_list:
        #Use the 'canonical' node ID for the component (e.g., the smallest tuple)
        #This ID will remain the same for the component until it merges.
        component_id = min(component_set) 
        
        #Check if this component ID already has a color
        if component_id not in PERMANENT_COLOR_MAP:
            #If new, assign the next color from the cycle
            new_color = next(COLOR_CYCLE)
            PERMANENT_COLOR_MAP[component_id] = new_color
        
        #Retrieve the (now guaranteed) persistent color
        persistent_color = PERMANENT_COLOR_MAP[component_id]
        
        #Map all nodes in the component to this persistent color
        for node in component_set:
            plot_color_map[node] = persistent_color
    
    #Cleanup/Merge Handling (Optional but recommended)
    #Remove any old IDs from the PERMANENT_COLOR_MAP that no longer exist 
    #as independent components. This happens when a component merges.
    current_ids = {min(c) for c in components_list}
    keys_to_delete = [
        key for key in PERMANENT_COLOR_MAP if key not in current_ids
    ]
    for key in keys_to_delete:
        del PERMANENT_COLOR_MAP[key]

    #Reset color cycle for safety (keeps the palette fresh)
    COLOR_CYCLE = cycle(COLOR_PALETTE) 

    #Prepare data arrays for plotting
    for node in G.nodes():
        x, y, z = node
        node_coords[node] = (x, y, z)
        X.append(x)
        Y.append(y)
        Z.append(z)
        node_colors.append(plot_color_map[node]) # Use the persistently mapped color

    #Plot the Nodes (Scatter Plot)
    ax.scatter(X, Y, Z, c=node_colors, s=10, depthshade=True) # Changed s=50

    #Plot the Edges (Lines)
    for edge in G.edges():
        node1 = edge[0]
        node2 = edge[1]

        x_start, y_start, z_start = node_coords[node1]
        x_end, y_end, z_end = node_coords[node2]
        
        # Edges should take the color of their component
        edge_color = plot_color_map[node1] 
        
        ax.plot(
            [x_start, x_end], 
            [y_start, y_end], 
            [z_start, z_end], 
            c=edge_color, 
            alpha=0.6, 
            linestyle='-'
        )
    
    #Set Axes and Title
    ax.set_xlabel("X Axis"); ax.set_ylabel("Y Axis"); ax.set_zlabel("Z Axis")
    plt.title(f"3D Graph: {len(components_list)} Connected Components")
    plt.pause(0.0000001)
    return

def straight_line_distance(coord1, coord2):
    """Calculate the straight-line (Euclidean) distance between two 3D-coordinates."""

    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), coord1, coord2
    


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day8_p2.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = connect_junction_boxes(lines)
    print(result)