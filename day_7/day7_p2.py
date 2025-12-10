import numpy as np

#Add to use numpy to get the real part of the coordinate because it corresponds
#to the column value
def tachyon_beam(string):
    grid, col_count_map = make_coord_grid(string)
    

    down = 1j
    down_right = 1 + 1j
    down_left = -1 + 1j

    for coord in grid:
        if grid[coord] == 'S' or grid[coord] == '|':
            if coord + down in grid.keys():
                if grid[coord + down] == '^': 
                    #if the beam hits a ^ add the number of paths to the left
                    #and right columns and resets the current column
                    if coord + down_right in grid.keys():
                        col_count_map[np.real(coord + down_right)] += col_count_map[np.real(coord)]
                        grid[coord + down_right] = '|'
                    if coord + down_left in grid.keys():
                        col_count_map[np.real(coord + down_left)] += col_count_map[np.real(coord)]
                        grid[coord + down_left] = '|'
                    col_count_map[np.real(coord)] = 0
                else:
                    grid[coord + down] = '|'
                    if grid[coord] == 'S': #Start the timeline count
                        col_count_map[np.real(coord)] = 1

    print_grid(grid)
    timelines_count = 0
    for col in col_count_map:
        timelines_count += col_count_map[col]
         
    return timelines_count

def make_coord_grid(string):
    lines = string.split('\n')
    lines.pop()  # Remove trailing newline if present
    grid = {}
    col = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x + y * 1j)] = lines[y][x]
            col[x] = 0
    return grid, col

def print_grid(grid):
    max_x = int(max(coord.real for coord in grid)) + 1
    max_y = int(max(coord.imag for coord in grid)) + 1

    for y in range(max_y):
        row = ''
        for x in range(max_x):
            row += grid.get(x + y * 1j, ' ')
        print(row)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day7_p2.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = tachyon_beam(lines)
    print(result)

        