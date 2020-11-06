"""

The Manhattan distance is the number of moves that a tile would have make to get to its correct position assuming that it was not blocked.

For example, the Manhattan distance between the tiles 1 and the 8 below is 3
(the '1' tile would have to go one space right and two down which is three moves altogether).

-------------------------
|       |   1   |       |
-------------------------
|       |       |       |
-------------------------
|       |       |   8   |
-------------------------

You are to write a heuristic function which will take two parameters representing the start and
the goal positions in an 8 puzzle and compute a heuristic evaluation of the start position using the Manhattan distance of each tile.

The function will be called h and the positions will be represented as a 9 character string containing the digits 1 to 8 and the blank character.

Example:

The call h(" 12345678", "1238 4756") will produce an evaluation of 14,
whereas the call h("1 3824756", "1238 4756") will produce an evaluation of 1 as only one tile has to move and
that tile has to move one place. Note that the blank is not a tile.

"""

def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"

    distance = 0
    start,start_dict = make_board(start)
    goal,goal_dict = make_board(goal)
    for row in range(3):
        for col in range(3):
            if start[row][col] != goal[row][col] and start[row][col].isdigit():
                x1 = start_dict[start[row][col]][0] #look at dictionary for the co-ordinates
                y1 = start_dict[start[row][col]][1]
                x2 = goal_dict[start[row][col]][0] #look at goal dictionary for same key.
                y2 = goal_dict[start[row][col]][1]

                distance += abs(x1 - x2)+ abs(y1 - y2)  #manhattan distance formula
    return distance

def make_board(name):
    board = [ ['-' for c in range(3)] for r in range(3)]
    puzzleDict = {}
    i = 0
    for row in range(3):
        for col in range(3):
            board[row][col] = name[i]
            puzzleDict[name[i]] = (row,col)     #make a dictionary for co-ordinates
            i += 1
    return board, puzzleDict

def main():
    # = 14
    a = " 12345678"
    b = "1238 4756"
    print("manhattan distance formula: ", a, "and ", b)
    print(h(a, b))


    # = 1
    c = "1 3824756"
    d = "1238 4756"
    print("manhattan distance formula: ", c, "and ", d)
    print(h(c, d))

if __name__ == "__main__":
   main()
