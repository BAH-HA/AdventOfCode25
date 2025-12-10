def cephalopod_math(string):
    aux_list = string.split("\n")
    aux_list.pop()  # Remove the last empty element 
    final_values = []
    
    parsed_list = [list(map(str, line.split())) for line in aux_list]

    for i in range(len(parsed_list[0])):
        operator = parsed_list[-1][i]
        numeric_values = list(map(int, [parsed_list[j][i] for j in range(len(parsed_list) - 1)]))
        print(numeric_values)
        print(operator)
        match (operator):
            case "+":
                final_values.append(sum(numeric_values))
            case "*":
                product = 1
                for val in numeric_values:
                    product *= val
                final_values.append(product)
        
    total = 0
    for val in final_values:
        total += int(val)
    return total



if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day6_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = cephalopod_math(lines)
    print(result)

        