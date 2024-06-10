# Markov Decision Process (MDP) Reinforcement Learning Python Implementation
# Using 'n' iterations where n = [5, 10, 15, 20, 50, 100]
# Created by: Leo Martinez III in Spring 2024

# define the constants and the overall grid size/features (all uppercase)
ROWS = 5
COLS = 5
ACTIONS = ['up', 'down', 'left', 'right'] # set of actions available
TERMINAL_STATES = {(0, 4): 10, (1, 2): -2, (2, 3): 8, (4, 2): 6} # fixed values
BLOCKED_STATES = [(1, 1), (1, 3), (1, 4), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 3), (4, 4)] # inaccessible
REWARD = -0.5
DISCOUNT_FACTOR = 0.9 # gamma value
ITERATIONS = [5, 10, 15, 20, 50, 100] # can add any number you like to the list

# function to check if a state is valid and not blocked
def is_valid_state(state):
    return (0 <= state[0] < ROWS) and (0 <= state[1] < COLS) and (state not in BLOCKED_STATES)

# function to calculate the value of a state using the Bellman equation
def calculate_value(state, values):
    if state in TERMINAL_STATES:
        return TERMINAL_STATES[state]
    
    max_value = float("-inf") # negative infinity to start (build up afterwards)
    for action in ACTIONS: # can move up, down, left, or right (unless blocked)
        if action == 'up':
            next_state = (state[0] - 1, state[1]) # move up
        elif action == 'down':
            next_state = (state[0] + 1, state[1]) # move down
        elif action == 'left':
            next_state = (state[0], state[1] - 1) # move left
        elif action == 'right':
            next_state = (state[0], state[1] + 1) # move right
        
        if is_valid_state(next_state): # ensure it is not a blocked state
            intended_value = 0.8 * values[next_state]
            right_angle_value = 0.1 * (values[state] if state in values else 0)
            opposite_value = 0.1 * (values[state] if state in values else 0)
            action_value = REWARD + DISCOUNT_FACTOR * (intended_value + right_angle_value + opposite_value)
            max_value = max(max_value, action_value) # (bellman's equation implementation)
    
    return max_value

# initialize values to 0 for all states (all rows and columns)
values = {}
for row in range(ROWS):
    for col in range(COLS):
        state = (row, col)
        if is_valid_state(state):
            values[state] = 0

# perform value iteration
for iteration in range(max(ITERATIONS) + 1):
    new_values = {}
    for state in values:
        new_values[state] = calculate_value(state, values)
    values = new_values
    
    if iteration in ITERATIONS:
        print(f'\nUtility values after {iteration} iterations:') # n iterations
        for state, value in sorted(values.items()):
            print(f'{state} Utility: {value:.2f}') # using a precision of 2 decimals
