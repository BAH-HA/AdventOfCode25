import sys
def dials_password(string):
    movs_list = string.split("\n")
    count = 0
    position = 50
    for movs in movs_list[:-1]:
        if "R" in movs:
            position += int(movs[1:])
        else:
            position -= int(movs[1:])
        
        position %= 100
        
        if position == 0:
            count += 1
    return count



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 day1_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = dials_password(lines)
    print(result)
