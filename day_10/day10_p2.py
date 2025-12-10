from collections import deque
from time import time
from z3 import *
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

def machines():
    string = get_input()
    machine_list = string.split('\n')
    result = 0
    for i, machine in enumerate(machine_list):

        machine_list[i] = machine.split(' ')

        # Convert the last element to a list of strings 
        # removing braces and splitting by comma
        machine_list[i][-1] = list(machine_list[i][-1][1:-1].split(','))

        # Convert the button options to lists of strings
        machine_list[i][1:-1] = [option[1:-1].split(',') for option in machine_list[i][1:-1]]


        buttons_list = []
        num_joltage_points = len(machine_list[i][-1])
        
        # button_option is the list of indices affected by one button
        for button_option_indices_str in machine_list[i][1:-1]:
            # Initialize the button vector to all 0s
            button_vector = [0] * num_joltage_points 
            
            for index_str in button_option_indices_str:
                idx = int(index_str)
                # Set the corresponding position to 1 if it is a valid index
                if 0 <= idx < num_joltage_points:
                    button_vector[idx] = 1
            
            # Add the completed vector to the list
            buttons_list.append(button_vector)

        joltage_requirements = [int(x) for x in machine_list[i][-1]]

        result += solve_with_z3(joltage_requirements, buttons_list)
                
    return result


def solve_with_z3(joltage_requirements, buttons_list):
    s = Optimize()
    num_buttons = len(buttons_list)
    num_joltage_points = len(joltage_requirements)

    m = [Int(f'm_{j}') for j in range(num_buttons)]

    #1st Constraint: All button presses are non-negative 
    for mj in m:
        s.add(mj >= 0)
    
    #2nd Constraint: A * m = R  meaning: buttons_list * m = joltage_requirements
    for i in range(num_joltage_points):
        #Line * column matrix multiplication rule
        equation_sum = 0
        for j in range(num_buttons):
            if buttons_list[j][i]:
                equation_sum += m[j]

        #the constraint, the Line * column sum must 
        #equal the Joltage point on the same index
        s.add(equation_sum == joltage_requirements[i])

    button_presses = sum(m)

    #makes sure that we pick the least amount of button presses needed
    s.minimize(button_presses)

    #makes sure its solvable and gets the min_presses
    if s.check() == sat:
        model = s.model()
        min_presses = model.evaluate(button_presses).as_long()
        return min_presses
    
    return -1



def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

if __name__ == "__main__":
    print(machines())
    print(f"Execution time: {time() - ts} seconds")
