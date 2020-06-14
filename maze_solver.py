#! C:/Users/Admin/AppData/Local/Programs/Python/Python38/python.exe
import argparse
from datetime import datetime

#-------------------------MAZE SOLVER USING BACKTRACKING ALGORITHM-----------------------------------

# findShortestPath is a function which returns False when no path direction is found 
# in given matrix
def findShortestPath(x, y):
	
	#if condition checks whether the end path of x and y exist.if exist then it returns True
	if x == SIZE-1 and y == SIZE -1 and mat[x][y] == 1:
		#if the path exist then visited path will be seen as 1s.
		visited[x][y] = 1
		return True
	#if condition checks whether index of matrix x and y is valid 
	if x >= 0 and x < SIZE and y >= 0 and y < SIZE and mat[x][y] == 1:
		visited[x][y] = 1
		#if condition to check the path on DOWN,if path exist then 
		# returns True else next condition
		if findShortestPath(x + 1, y):
			return True
		#if condition to check the path on RIGHT,if path exist then 
		# returns True else next condition
		if findShortestPath(x,y + 1):
			return True
		#if condition to check the path on UP,if path exist then 
		# returns True else next condition
		if findShortestPath(x - 1, y):
			return True
		#if condition to check the path on LEFT,if path exist then 
		# returns True else returns path as 0's
		if findShortestPath(x, y - 1):
			return True
		#if visited path doesnt exist then marks as 0's
		visited[x][y] = 0
		return False
	return 0

#FinalPath is a function which prints tha visited path of given matrix
def FinalPath( visited ):
	op.write("--------------------------------------------------------------------------")
	op.write("\n"+"Below path is one of the possible destination for given maze"+"\n")
	#looping to get final matrix from visited list
	for i in visited:
		for j in i:
			op.write(" " + str(j) + " ")
		op.write('\n')
	now = datetime.now()
	#Display Time,Date and Day of result printed
	op.write("\n"+"Printed at : " + now.strftime("%a-%d-%B-%y   %X\n" + "*\n"))

#main function
if __name__ == "__main__":
	mat = []
	parser = argparse.ArgumentParser()
	#argument for input file
	parser.add_argument("--input_file", help = "Input file",default="./input.txt")
	#argument for output fie
	parser.add_argument("--output_file", help = "Output file",default="./output.txt")
	args = parser.parse_args()
	print("\n PROCESS RUNNING SUCCESSFULLY....... \n")
	#input file
	In = open(args.input_file,'r')
	#output fie
	op = open(args.output_file,'a')
	#to get iinput matrix from input file
	for data in In:
		[l.strip('\n\r') for l in data]
		mat.append([int(x) for x in data.split()])
	#SIZE = length of given matrix
	SIZE = len(mat)
	visited = [[0 for x in range(SIZE)] for y in range(SIZE)]
	#initially x and y is 0
	if (findShortestPath(0, 0)):
		FinalPath(visited)
	else:
		#if path doesn't exist for given matrix then output returns  -1(no path found)
		op.write("--------------------------------------------------------------------------")
		op.write("\n-1\n\n")
		op.write("No path found for the given maze")
		now = datetime.now()
		op.write("\n\n"+"Printed at: " + now.strftime("%a-%d-%B-%y   %X\n" + "*\n"))
	