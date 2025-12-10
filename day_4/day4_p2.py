from PIL import Image

def paper_rolls(string):
    grid = make_coord_grid(string)
    final_sum = 0
    frames = []

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

    while True:
        to_remove = []
        for coord in grid:
            count = 0
            if grid[coord] == '@':
                for direction in NEIGHBORS_8:
                    neighbor_coord = coord + direction
                    if neighbor_coord in grid:
                        if grid[neighbor_coord] ==  '@':
                            count += 1
                if count < 4:
                    to_remove.append(coord)
                    final_sum += 1
        
        if not to_remove:
            break

        for coord in to_remove:
            grid[coord] = '.'
        
        #Save frame after each iteration
        frames.append(grid_to_image(grid))

        
    #Scale up frames for better visibility   
    scaled_frames = [f.resize((f.width*10, f.height*10), Image.NEAREST) for f in frames]
    frames = scaled_frames

    #Save as GIF
    frames[0].save("paper_rolls_evolution.gif",
                    save_all=True, 
                    append_images=frames[1:], 
                    duration=300, 
                    loop=0)
    return final_sum


"""Convert grid to image for visualization."""
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
        color = (255, 255, 255) if val == '@' else (0, 0, 0)
        img.putpixel((x, y), color)

    return img

"""Create a coordinate grid from input string."""
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
        print("Usage: python3 day4_p2.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = paper_rolls(lines)
    print(result)