def invalid_ids(string):
    ids_list = string.split(",")
    invalids = []
    invalids_sum = 0
    for ranges in ids_list:
        range1 = ranges.split("-")[0]
        range2 = ranges.split("-")[1]
        for id in range(int(range1), int(range2)+1):
                if not is_valid(str(id)):
                    invalids.append(id)
                    invalids_sum += int(id)

    
    return invalids_sum


def is_valid(id):
    n = len(id)
    for i in range(1, n // 2 + 1):
         if n % i == 0:
            substr = id[:i]
            if substr * (n // i) == id:
                return False
    return True


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day2_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = invalid_ids(lines)
    print(result)