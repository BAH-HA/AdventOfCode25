from collections import deque
from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = True
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

        # Convert the first element to a list of characters removing brackets
        machine_list[i][0] = list(machine_list[i][0][1:-1])

        # Convert the button options to lists of strings
        machine_list[i][1:-1] = [option[1:-1].split(',') for option in machine_list[i][1:-1]]

        # Initial state with all lights off
        initial_state = tuple(['.'] * len(machine_list[i][0])) 


        expected = machine_list[i][0]
        button_options = machine_list[i][1:-1]

        #BFS to find the shortest sequence of button presses
        queue = deque()
        queue.append((initial_state, 0))  # (current_state, button press count)

        visited = set()
        found = False
        while queue and not found:
            current_state, press_count = queue.popleft()

            if list(current_state) == expected:
                print(f"  Minimum button presses required: {press_count}\n")
                result += press_count
                found = True
                break

            for button_indices in button_options:
                # Convert string indices to integers
                indices = [int(idx) for idx in button_indices]
                new_state = toggle_state_lights(current_state, indices)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, press_count + 1))
        
    return result


def toggle_state_lights(current_state, button_indices):
        """Applies button press to state and returns the new state tuple."""
        # Convert tuple to list for mutable modification
        new_lights = list(current_state)
        
        for index in button_indices:
            # Toggle: '.' -> '#' or '#' -> '.'
            if new_lights[index] == '.':
                new_lights[index] = '#'
            else:
                new_lights[index] = '.'
        
        # Return as immutable tuple for hashing
        return tuple(new_lights)



def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

if __name__ == "__main__":
    machines()
    print(f"Execution time: {time() - ts} seconds")

