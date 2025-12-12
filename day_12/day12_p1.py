from time import time
import functools
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

def presents():
    string = get_input()
    parsed_string = string.split('\n\n')

    grids = parsed_string[-1].split("\n")
    presents = parsed_string[:-1]

    list_of_presents_to_fit = []
    presents_size = [x.count("#") for x in presents]
    count = 0

    for grid in grids:
        dimension = grid.split(": ")[0]
        x, y = dimension.split("x")
        presents_count = grid.split(": ")[1].split(" ")

        grid_size = int(x) * int(y)
        presents_space = 0
        for i, num in enumerate(presents_count):
            presents_space += presents_size[i] * int(num)
        
        if(presents_space < grid_size):
            count += 1

    return count

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

if __name__ == "__main__":
    print(presents())
    print(f"Execution time: {time() - ts} seconds")
