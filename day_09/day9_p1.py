from time import time
ts = time()

def largest_rectangle_area(string):
    string = string.split('\n')
    string.pop()  # Remove trailing newline if present
    string = [
        (int(x), int(y)) 
        for item in string 
        for x, y in [item.split(',')]
    ]

    max_area = 0
    for coord1 in string:
        for coord2 in string:
            max_area = max(max_area, calc_area(coord1[0], coord1[1], coord2[0], coord2[1]))
    return max_area

def calc_area(x1, y1, x2, y2):
    width = abs(int(x2) - int(x1)) + 1
    height = abs(int(y2) - int(y1)) + 1
    return width * height



if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day9_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = largest_rectangle_area(lines)
    print(result)
    print("Execution time:", time() - ts)