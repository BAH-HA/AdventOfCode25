def paper_rolls(string):
    grid = make_coord_grid(string)
    final_sum = 0

    NEIGHBORS_8 = [
        1,      # right
        -1,     # left
        1j,     # down
        -1j,    # up
        1 + 1j,   # down-right
        1 - 1j,   # up-right
        -1 + 1j,  # down-left
        -1 - 1j,  # up-left
    ]

    for coord in grid:
        count = 0
        if grid[coord] == '@':
            for direction in NEIGHBORS_8:
                neighbor_coord = coord + direction
                if neighbor_coord in grid:
                    if grid[neighbor_coord] ==  '@':
                        count += 1
            if count < 4:
                final_sum += 1
        
    return final_sum


def make_coord_grid(string):
    lines = string.split('\n')
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x + y * 1j)] = lines[y][x]

    return grid

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day4_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = paper_rolls(lines)
    print(result)

