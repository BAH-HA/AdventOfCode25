import networkx as nx
from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

def devices():
    string = get_input()

    devices = string.split('\n')

    G = nx.DiGraph()

    for device in devices:
        aux = device.split(' ')
        input_device = aux[0][0:3]
        output_devices = aux[1:]

        G.add_node(input_device)
        G.add_edges_from([(input_device, x) for x in output_devices])
    
    # Find all simple paths
    all_paths = list(nx.all_simple_paths(G, "you", "out"))

    return len(all_paths)


def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

if __name__ == "__main__":
    print(devices())
    print(f"Execution time: {time() - ts} seconds")