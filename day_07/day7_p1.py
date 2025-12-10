from PIL import Image
import numpy as np
def tachyon_beam(string):
    grid, col_num = make_coord_grid(string)
    frames = []
    split_count = 0

    down = 1j
    down_right = 1 + 1j
    down_left = -1 + 1j

    for coord in grid:
        if grid[coord] == 'S' or grid[coord] == '|':
            if coord + down in grid.keys():
                if grid[coord + down] == '^':
                    split = False 
                    if coord + down_right in grid.keys():
                        split = True
                        grid[coord + down_right] = '|'
                    if coord + down_left in grid.keys():
                        split = True
                        grid[coord + down_left] = '|'
                    if split:
                        split_count += 1

                else:
                        grid[coord + down] = '|'
        #everytime we change rows, add the fram so we can make a GIF
        if np.real(coord) == col_num - 1:
            frames.append(grid_to_image(grid))
        

        
    #Scale up frames for better visibility (considerably slower)   
    scaled_frames = [f.resize((f.width*10, f.height*10), Image.NEAREST) for f in frames]
    frames = scaled_frames

    #Save as GIF
    frames[0].save("Tachyon.gif",
                    save_all=True, 
                    append_images=frames[1:], 
                    duration=0.01, 
                    loop=0)
         
    return split_count

def make_coord_grid(string):
    lines = string.split('\n')
    lines.pop()  # Remove trailing newline if present
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x + y * 1j)] = lines[y][x]

    return grid, len(lines[0])


def grid_to_image(grid):
    xs = [int(c.real) for c in grid]
    ys = [int(c.imag) for c in grid]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    w = max_x - min_x + 1
    h = max_y - min_y + 1

    img = Image.new("RGB", (w, h))

    for coord, val in grid.items():
        x = int(coord.real)
        y = int(coord.imag)
        if val == 'S':
            color = (255, 0, 0)
        elif val == '^':
            color = (255, 51, 153) 
        elif val == '|':
            color = (51, 255, 255)
        
        else:
            color = (0, 0, 0) 

        img.putpixel((x, y), color)

    return img

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
        print("Usage: python3 day7_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = tachyon_beam(lines)
    print(result)

        