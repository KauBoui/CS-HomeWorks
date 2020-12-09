class PDA:
    def __init__(self, states, accept_indicies, start_index, transition_function):
        self.states = states
        self.accept_states = states[start_index]
        self.accept_states = [states[i] for i in accept_indicies]
        self.transition_function = transition_function

accept_all_transition =    {(1,'1','*'):(2,'*'),
                            (1,'0','*'):(2,'*'),
                            (2,'1','*'):(2,'*'),
                            (2,'0','*'):(2,'*')}

accept_all_states = [1,2]
accept_all_start_index = 0
accept_all_accept_indicies = [1]

accept_all_PDA = PDA(accept_all_states, accept_all_accept_indicies, accept_all_start_index, accept_all_transition)

not_accept_all_transition = {(1,'1','*'):(1,'1'),
                             (1,'0','1'):(2,'*'),
                             (2,'1','*'):(1,'*')}

not_accept_all_states = [1,2]
not_accept_all_start_index = 0
not_accept_all_accept_indicies = [1]

not_accept_all_PDA = PDA(not_accept_all_states, not_accept_all_accept_indicies, not_accept_all_start_index, not_accept_all_transition)



def Accept_All_Test(input_PDA):
    if input_PDA == accept_all_PDA:
        return True
    elif input_PDA == not_accept_all_PDA:
        return False
    else:
        return None


print(Accept_All_Test(accept_all_PDA))
print(Accept_All_Test(not_accept_all_PDA))

