def fresh_ingredients(string):
    aux_list = string.split("\n\n")

    ingredients = aux_list[1].split("\n")
    range_list = aux_list[0].split("\n")
    fresh_ing_ids_set = set()
    for ing in ingredients[:-1]:
        for r in range_list:
            r_split = r.split("-")
            if int(ing) in range(int(r_split[0]), int(r_split[1]) + 1):
                fresh_ing_ids_set.add(int(ing))
                break
        
    
    return len(fresh_ing_ids_set)


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

