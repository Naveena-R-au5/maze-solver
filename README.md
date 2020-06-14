# maze-solver
maze solver using backtracking algorithm in python

## Description

A Maze is a N*N binary matrix of blocks where source starts from 0 0 i.e uppermost of matrix and destination is the final path in the matrix i.e., matrix[SIZE-1][SIZE-1].In this algorithm,if a person starts from source and has to reach the destination then he/she can move in 4 directions UP,DOWN,LEFT,RIGHT.
and also the person can not move in direction where there is a block.Path only valid when there is no blocks.

## Backtracking algorithm

In this algorithm a N*N binary matrix i.e (0's and 1's) is taken.here o's represents blocked path(cant move) and 1's represent unblocked path(can move).the binary Matrix is seen as below:-

1 0 0
1 1 0
1 1 1

3*3 matrix 

in this above matrix source starts from top[index(0 0)] and should reach destination[index(2 2)]

[1] 0  0
 1  1  0
 1  1 [1]

we can store the visited matrix path in seperate list as if path exists it stores 1 else 0.Once the source reaches destination then the other numbers in matrix will become 0 only the final path is shown with 1's in matrix as below:-

1 0 0
1 0 0
1 1 1

if the person can't move up or bottom ,then he/she can move to left or right to find the path.
If none of the four moves (down, right, up, or left) are possible,then move back and change his/her current path (backtracking).

## Execution

- I have used CLI & File handling to display output of this project in output.txt file.
- To run this project provide input and output file path along with maze_solver.py file in cmd  prompt.
eg. mazer_solver.py [--input_file input.txt] [--output_file output.txt]
-Also can run(Run-Script.bat)file to get the output.

## Modules 

- Argparse - For Command-line option and argument parsing.
- datetime - To show the date and time of execution.







