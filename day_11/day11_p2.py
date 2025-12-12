from time import time
import functools
ts = time()


# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

def devices():
    nodes = dict() # map node name -> list of connections
    string = get_input()
    devices = string.split("\n")

    for device in devices:
            aux = device.split(' ')
            input_device = aux[0][0:3]
            output_devices = aux[1:]
            nodes[input_device] = output_devices
    
    @functools.cache
    def count_routes(this_node, visited_dac, visited_fft):
        match this_node:
            case 'out': return 1 if (visited_dac and visited_fft) else 0
            case 'dac': visited_dac = True
            case 'fft': visited_fft = True
        return sum(count_routes(link, visited_dac, visited_fft) for link in nodes[this_node])

    return count_routes("svr", False, False)
 
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
