import numpy as np
def joltage(string):
    banks = string.split('\n')
    joltage_sum = 0

    for bank in banks[:-1]:
        vec = np.array(list(bank))
        digits = []
        for i in range(1,13):
            k = np.argmax(vec[0:len(vec)-(12-i)])
            digits.append(vec[k])
            vec = vec[k+1:]
        
        max_joltage = "".join(digits)
        print(f"Bank: {bank} - Max Joltage: {max_joltage}")
        joltage_sum += int(max_joltage)
    return joltage_sum

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 day3_p2.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = f.read()

    result = joltage(lines)
    print(result)

