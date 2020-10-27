"""
A heuristic can be used to guide a search from a start position to a goal.

In the 8 puzzle, one heuristic will be the number of tiles out of place.
Write a function that will take a start position and a goal position as parameters and will return the number of tiles out of place.

The function will be called h and the positions will be represented as a 9 character string containing the digits 1 to 8 and the blank character.

Example:

The call h(" 12345678", "1238 4756") will produce an evaluation of 8 as there are 8 tiles out of place,
whereas the call h("1 3824756", "1238 4756") will produce an evaluation of 1 as only one tile is out of place.
Note that the blank is not a tile.

"""

def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"

    tiles_num = 0
    for i in range(0, len(start)):
        if start[i] != goal[i] and start[i].isdigit():
            tiles_num += 1

    return tiles_num

def main():
    # = 8
   print(h(" 12345678", "1238 4756"))

   # = 1
   print(h("1 3824756", "1238 4756"))

if __name__ == "__main__":
   main()
