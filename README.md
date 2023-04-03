# n Puzzle Problem
## 1- introduction
An instance of the n-puzzle game consists of a board holding $n^2-1$ distinct movable tiles, plus an empty space. The tiles are numbers from the set $1,..,n^2-1$. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this assignment, the blank space is going to be represented with the number $0$. Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order $0,1,… ,n^2−1$. The search space is the set of all possible states reachable from the initial state. The blank space may be swapped with a component in one of the four directions $\{‘Up’, ‘Down’, ‘Left’, ‘Right’\}$, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state.

## II. Algorithm Review

The searches begin by visiting the root node of the search tree, given by the initial state. Among other book-keeping details, three major things happen in sequence in order to visit a node:
- 1. First, we remove a node from the frontier set.
- 2. Second, we check the state against the goal state to determine if a solution has been found.
- 3. Finally, if the result of the check is negative, we then expand the node. To expand a given node, we generate successor nodes adjacent to the current node, and add them to the frontier set. Note that if these successor nodes are already in the frontier, or have already been visited, then they should not be added to the frontier again.

This describes the life-cycle of a visit, and is the basic order of operations for search agents in this assignment—(1) remove, (2) check, and (3) expand. In this assignment, you need to implement the following algorithms:
- DFS
- BFS
- Greedy Best First Search

## Problem repesentation
Lets consider 8-puzzle problem for illustration. In 8-puzzle problem we have a $3\times 3$ grid as given below:
   
1 2 3   
4 0 5   
6 7 8   

In your implementation you need to repesent a given state as a list of elements. The above grid may be represented as:
                                                                                  $[1,2,3,4,0,5,6,7,8]$

Since the empty tile, __0__ occurs at the midlle of the grid then the following four diffferent operations are possible:
- __move right:__ swap 5 and 0. 
- __move left:__ swap 4 and 0.
- __move down:__ swap 7 and 0.
- __move up:__ swap 2 and 0.

Note that, __the empty tile,0__, may occur at any of the nine sqaures of the gird. Thus you have to handle the nine different situations carefully. For your convienence the mentioned situation is implemeted in the function __action__ . Please code the rest of the eigth conditions. 
