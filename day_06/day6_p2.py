def cephalopod_math(string):
    parsed_list = string.split("\n")
    parsed_list.pop()# Remove the last empty element 
    numeric_values_list = []#List of lists of numeric values
    operators = parsed_list[-1].split()
    final_values = []
    
    i = len(parsed_list[0]) - 1
    while i >= 0:
        numeric_values = []
        num = ""
        
        while True:
            checker = True #To check if we reached an empty column
            for j in range(len(parsed_list) - 1):
                if parsed_list[j][i] != " ":
                    num += parsed_list[j][i]
                    checker = False
        
            if num != "":
                numeric_values.append(int(num))
                num = ""

            i -= 1
            if checker or i < 0:
                numeric_values_list.append(numeric_values)
                break
        

    numeric_values_list.reverse()

    for i in range(len(numeric_values_list)):
        operator = operators[i]
        numeric_values = numeric_values_list[i]
        
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

        