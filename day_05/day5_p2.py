def fresh_ingredients(string):
    aux_list = string.split("\n\n")
    range_list = aux_list[0].split("\n")

    num_ingredients = 0

    #Sort ranges by their starting point
    range_list.sort(key=lambda x: int(x.split("-")[0]))

    #Merge overlapping ranges
    merged_ranges = []
    for r in range_list:
        r_split = r.split("-")
        start, end = int(r_split[0]), int(r_split[1])
        if not merged_ranges:
            merged_ranges.append([start, end])
        else:
            last_range = merged_ranges[-1]
            if start <= last_range[1] + 1:
                last_range[1] = max(last_range[1], end)
            else:
                merged_ranges.append([start, end])


    for r in merged_ranges:    
        num_ingredients += r[1] - r[0] + 1
        
    
    return num_ingredients


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day5_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = fresh_ingredients(lines)
    print(result)

