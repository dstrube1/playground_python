#challenge13
#https://www.linkedin.com/learning/python-code-challenges/solve-a-sudoku?u=2163426

#Solve a sudoku

from itertools import product

""" reset:
puzzle = [	[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0]]
"""

puzzle = [	[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0]]

def solveSudoku(puzzle):
	#Not using deductive reasoning like a human;
	#instead, depth first search of trial and error of every combination
	for (row, col) in product(range(0,9), repeat=2):
		if puzzle[row][col] == 0: #find an unassigned cell
			for num in range(1,10):
				allowed = True #check if num is allowed in row/col/box
				for i in range(0,9):
					if (puzzle[i][col] == num) or (puzzle[row][i] == num) :
						allowed = False
						break #not allowed in row or col
				for (i,j) in product(range(0,3), repeat=2):
					if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
						allowed = False
						break #not allowed in box
				if allowed:
					puzzle[row][col] = num
					trial = solveSudoku(puzzle)
					#if trial := solveSudoku(puzzle): 
					#^Invalid syntax :(
					if trial:
						return trial
					else:
						puzzle[row][col] = 0
			return False #could not place a number in this cell
	return puzzle
	
def printPuzzle(puzzle):
	#replace 0s with *s
	puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
	print()
	for row in range(0,9):
		if ((row % 3 == 0) and (row != 0)): #too many ()s?
			print('-'*33) #horizontal line
		for col in range(0,9):
			if ((col % 3 == 0) and (col != 0)):
				print(" | ", end='') #vertical line
			print('',puzzle[row][col],'', end='')
		print()
	print()

#main
print("unsolved puzzle: ")
printPuzzle(puzzle)

solved = solveSudoku(puzzle)

print("solved puzzle: ")
printPuzzle(solved)