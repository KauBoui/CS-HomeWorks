#Author: Errol Bucy
#Date: 10-30-20

# To build the transition from a text file the file needs to be formated as so:
# Line 1 : The states the pushdown automata is currently in
# Line 2 : The states the pushdown automata transitions to
# Line 3 : The input the pushdown automata is to read  ('*' denotes the empty string)
# Line 4 : The characters to pop from the stack
# Line 5 : The characters to push from the stack
# Line 6 : The accept states 
# Line 7 : The start state

# Example:
# 11122344556 #
# 12423345566
# a**b*cb*c*c
# ***a$****$*
# a**********
# 36
# 1

def Build_Transition_Function_From_State_Graph(graph_edges, edge_input_symbols: str, edge_top_stack: str, edge_push_stack: str):
    assert len(graph_edges) == len(edge_input_symbols) == len(edge_top_stack) == len(edge_push_stack)
    Domain = []
    Range = []
    for i in range(len(graph_edges)):
        in_state, input_symbol, top_stack = graph_edges[i][0], edge_input_symbols[i], edge_top_stack[i]
        Domain.append((in_state, input_symbol, top_stack))
        out_state, push_stack = graph_edges[i][1], edge_push_stack[i]
        Range.append((out_state, push_stack))
    
    transition_function = dict(zip(Domain,Range))
    return transition_function 

def Parse_TextFile_And_Build_Function(filename: str):
    with open(filename, "r") as file:
        file_lines = file.readlines()
        clean_lines = [line.rstrip() for line in file_lines]
        assert len(clean_lines) == 7
        assert len(clean_lines[0]) == len(clean_lines[1]) == len(clean_lines[2]) ==len(clean_lines[3]) == len(clean_lines[4])
        accept_state_indices = []
        for i in range(len(clean_lines[5])):
            accept_state_indices.append(int(clean_lines[5][i]) - 1)
        start_state_index = int(clean_lines[6]) -1
        graph_edges = []
        for i in range(len(clean_lines[0])):
            graph_edges.append((int(clean_lines[0][i]), int(clean_lines[1][i])))
        edge_input_symbols = str(clean_lines[2])
        edge_top_stack = str(clean_lines[3])
        edge_push_stack = str(clean_lines[4])
        states = list(dict.fromkeys(clean_lines[0]))
        return accept_state_indices, start_state_index, states, Build_Transition_Function_From_State_Graph(graph_edges, edge_input_symbols, edge_top_stack, edge_push_stack)

#                                                                                                           Your File_Path Here!
accept_state_indices, start_state_index, states ,transition_function = Parse_TextFile_And_Build_Function("CS-HomeWorks/Theory_of_Computation/PushDown_Simulator/graph.txt")
#      (in_state, input, pop_stack) : (out_state, push_stack)
# transition function:  {(1,'a','*'):(1,'a'),
#                        (1,'*','*'):(2,'*'),
#                        (1,'*','*'):(4,'*'),
#                        (2,'b','a'):(2,'*'),
#                        (2,'*','$'):(3,'*'),
#                        (3,'c','*'):(3,'*'),
#                        (4,'b','*'):(4,'*'),
#                        (4,'*','*'):(5,'*'),
#                        (5,'c','a'):(5,'*'),
#                        (5,'*','$'):(6,'*'),
#                        (6,'c','*'):(6,'*')}
# start state: 1
# accept states: 3, 6

start_state = states[start_state_index]
accept_states = [states[i] for i in accept_state_indices]
transition_domain = list(transition_function.keys())
transition_range = list(transition_function.values())

def simualate_PDA(inpt: str, current_state: int, stck: list, stts: list):
    states =  stts
    state = current_state
    Input = inpt
    stack = stck
    if not Input and stack ==[''] and state in accept_states: #Base Case: if input is empty and the current state is an accept state return True
        return True 
    possible_moves = [] 
    for i in range(len(transition_domain)):
        if transition_domain[i][0] == state:
            # Moves are valid if the input in the transition function matches the given input
            # Or if the input in the transtition function is empty
            if transition_domain[i][1] == '*' or transition_domain[i][1] == Input[0]:
                # Moves are vilid if the stack value is equal to the top of the stack
                # Or if the pop_stack value is the empty string
                if transition_domain[i][2] == '*' or transition_domain[i][2] == stack[0]:
                    possible_moves.append((transition_domain[i],transition_range[i])) 
    for move in possible_moves:
        if move[0][1] != '*': #If input value is not empty then the input needs to be chopped in front, because we've already worked on that value
            Input = Input[1:]
        if move[0][2] != '*': #If pop_stack value not equal to the empty string pop the stack.
            stack = stack[1:]
        if move[1][1] != '*': #If push_stack value not equal to the empty string push the value to the stack.
            stack.insert(0,move[1][1])
        state = states[move[1][0] - 1] # update the state based on the transition function
        if simualate_PDA(Input, state, stack) == True: #Recurse with the updated input, state, and stack.
            return True                                #This handles non-determinism by only returning something if there is a valid path. 
    else:
        return False

string_to_read = input("Input for the PDA:  ")
print(simualate_PDA(string_to_read, start_state, ["$"], states))


