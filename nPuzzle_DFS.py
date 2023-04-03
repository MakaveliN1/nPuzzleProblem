def actions(s): #This function should return the set of actions (branching factor) of a given state "s"
    actionDic={}
    if s[0]==0:
        actionDic["right"]=[0,1]
        actionDic["down"]=[0,3]
    if s[1]==0:
        actionDic["left"]=[1,0]
        actionDic["right"]=[1,2]
        actionDic["down"]=[1,4]
    if s[2]==0:
        actionDic["left"]=[2,1]
        actionDic["down"]=[2,5]
    if s[3]==0:
        actionDic["up"]=[3,0]
        actionDic["right"]=[3,4]
        actionDic["down"]=[3,6]
    
    if s[4]==0: #If the empty cell occurs at the middle of the grid as illustrated above.
        # move right: swap 5 and 0. i.e. swap the elements of at location 4 and 5
        actionDic["right"]=[4,5]
        # move left: swap 3 and 0. i.e. swap the elements of at location 4 and 2
        actionDic["left"]=[4,3]
        # move down: swap 4 and 7. i.e. swap the elements of at location 4 and 7
        actionDic["down"]=[4,7]
        # move up: swap 2 and 0. i.e. swap the elements of at location 4 and 1
        actionDic["up"]=[4,1]
    if s[5]==0:
        actionDic["up"]=[5,2]
        actionDic["left"]=[5,4]
        actionDic["down"]=[5,8]
    if s[6]==0:
        actionDic["up"]=[6,3]
        actionDic["right"]=[6,7]
    if s[7]==0:
        actionDic["up"]=[7,4]
        actionDic["left"]=[7,6]
        actionDic["right"]=[7,8]
    if s[8]==0:
        actionDic["up"]=[8,5]
        actionDic["left"]=[8,7]
        
    return actionDic
  
    #Test the action function
s=[2,0,3,4,1,5,6,7,8]
print(actions(s))

def results(state,action): #"state" is a list which represent the given state. "action" is a list which
    #contain the indexes of the  locations that to be swaped
    new_state=state.copy()
    new_state[action[0]], new_state[action[1]] = new_state[action[1]], new_state[action[0]]
    return new_state
  
    #Testing the results function
#for the given state "s" the function should retun the following results"
#The set of possible actions for state [1, 2, 3, 4, 0, 5, 6, 7, 8] :
#{'right': [4, 5], 'left': [4, 3], 'down': [4, 7], 'up': [4, 1]}

#The neighbors of the given state, [1, 2, 3, 4, 0, 5, 6, 7, 8]  are:
#[[1, 2, 3, 4, 5, 0, 6, 7, 8], [1, 2, 3, 0, 4, 5, 6, 7, 8], [1, 2, 3, 4, 7, 5, 6, 0, 8], [1, 0, 3, 4, 2, 5, 6, 7, 8]]

s=[2,0,3,4,1,5,6,7,8]
actionlist=actions(s)
print("")
print("The set of possible actions for state", s,":")
print( actionlist)
print("")
successors=[results(s,actionlist[x]) for x in actionlist]
print("The neighbors of the given state,",s," are:")
print(successors)

def neighbors(state):
    successors = []
    actionlist = actions(state) # The list of all possible actions that may be taken in the given state 
    for action in actionlist:
        neighbor = results(state, action) # apply the action to the state to get the new neighbor
        successors.append(neighbor) # add each neighbor into the list "successors"
    return successors
  
#Testing
# For the gien list the output should be:
#[[1, 2, 3, 4, 5, 0, 6, 7, 8],
 #[1, 2, 3, 0, 4, 5, 6, 7, 8],
 #[1, 2, 3, 4, 7, 5, 6, 0, 8],
 #[1, 0, 3, 4, 2, 5, 6, 7, 8]]
    
s=[1,2,3,4,0,5,6,7,8]
neighbors(s)

def goal_test(goal, state):
    ''' check if state equals goal state'''   
    if state == goal:
        return True
    else:
        return False
      
#Test your function!
#for the given input the output must be "False"
goal=[0,1,2,3,4,5,6,7,8]
state=[0,1,2,3,4,5,6,7,8]
print(goal_test(goal, state))

def dfs(start, goal):
    explored = [] # initialize the explored list
    frontier = [start] # initializ the frontier as a list with the start state 
    print('searching from: {} to {}'.format(start, goal))
    while frontier: #repeat while frontier is not empty
        print('Frontier:', frontier) # print current contents of the frontier
        # remove one state form the frontier and store in explore list 
        state = frontier.pop(0) 
        explored.append(state)
        print('')
        print('')
        print('')
        print('Now in:', state) # print the current state
        
         
        # test wheter the current state is goal?
        if goal_test(state,goal): 
            print('Desitnation reached')
            return state
         
        # check whehter the current state has already processed or present in frontier
        for neighbor in neighbors(state):
            if neighbor not in explored and neighbor not in frontier: 
                frontier.append(neighbor)
                            
    print('failure') 
 
initial = [0,1,2,3,4,5,6,7,8]# Define the initial state is a two elemet
goal = [0,1,2,3,4,5,6,7,8] # one liter water in 5lt jug
dfs(initial,goal)
