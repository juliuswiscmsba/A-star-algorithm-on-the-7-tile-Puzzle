import heapq




def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0
    for i in range(len(from_state)):
        if from_state[i] != 0:
            now = from_state[i]
            goal = to_state.index(now)

            v_now = i//3
            h_now = i%3
            v_goal = goal//3
            h_goal = goal%3
            
            distance += abs(v_now-v_goal)
            distance += abs(h_now-h_goal)
  
    return distance

def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    poss_states=[]
    for i in range(len(state)):
        if state[i] == 0:
            if i//3 == 0:
                new_state = state.copy()
                new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
                poss_states.append(new_state)
            elif i//3 == 1:
                new_state = state.copy()
                new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
                poss_states.append(new_state)
                new_state = state.copy()
                new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
                poss_states.append(new_state)   
            else:
                new_state = state.copy()
                new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
                poss_states.append(new_state)
                
            if i%3 == 0:
                new_state = state.copy()
                new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
                poss_states.append(new_state)
            elif i%3 == 1:
                new_state = state.copy()
                new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
                poss_states.append(new_state)
                new_state = state.copy()
                new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
                poss_states.append(new_state)
            else:
                new_state = state.copy()
                new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
                poss_states.append(new_state)
                
            succ_states=[]    
            [succ_states.append(x) for x in poss_states if x not in succ_states and x != state]
    
    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    g=0
    index=0
    parent_child_dict={}
    parent_child_dict[tuple(state)]= get_succ(state)
    self_index_dict={}
    self_index_dict[-1]=[state,g]
    
    path=[state]
    path_parent=[-1]
    
    pq=[]
    pq_len=[]
    current_state = state.copy()
    
    while current_state != goal_state:
        succ_states = get_succ(current_state)
        for s in succ_states:
            if s not in path:
                #parent_index and g
                for f1 in parent_child_dict:
                    if current_state == list(f1):
                        for f2 in self_index_dict:
                            if current_state == self_index_dict[f2][0]:
                                parent_index = f2
                                parent_g = self_index_dict[f2][1]
                                g = parent_g+1
                        
                
                #h
                h = get_manhattan_distance(s, goal_state)
                heapq.heappush(pq,(g+h, s, (g, h, parent_index)))
                
        #pq length
        pq_len.append(len(pq))

        b = heapq.heappop(pq)
        path.append(b[1])
        path_parent.append(b[2][2])
        current_state = b[1]
                
                
        parent_child_dict[tuple(b[1])] = get_succ(current_state)
        self_index_dict[index] = [b[1], b[2][0]]
        index+=1
    
    #print(path)
    
    #backtrace   
    target = goal_state
    route=[target]
    while target != state:
        for i in range(len(path)):
            if path[i] == target:
                p = path_parent[i]
                target = self_index_dict[p][0]
                route.append(target)
                break;
                
    #print(route[::-1])
    for move, j in enumerate(route[::-1]):
        print('{} h={} moves: {}'.format(j,get_manhattan_distance(j),move))
    print('Max queue length: {}'.format(max(pq_len)))
        

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()

    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    #solve([2,5,1,4,0,6,7,0,3])
    solve([4,3,0,5,1,6,7,2,0])
    print()
