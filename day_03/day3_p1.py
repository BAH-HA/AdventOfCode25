def joltage(string):
    banks = string.splitlines()
    joltage_sum = 0
    for bank in banks:
        max_joltage = "00"
        for i in range(len(bank)):
            joltage = int(bank[i])
            if joltage > int(max_joltage[0]) and i != len(bank) - 1:
                max_joltage = str(joltage * 10)
            elif joltage > int(max_joltage[1]):
                max_joltage = str(int(max_joltage[0]) * 10 + joltage)
                
        print(f"Bank: {bank} - Max Joltage: {max_joltage}")
        joltage_sum += int(max_joltage)
    return joltage_sum


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day3_p1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = joltage(lines)
    print(result)

