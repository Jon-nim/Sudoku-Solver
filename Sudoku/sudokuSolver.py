from pygame import *
from random import randint
from copy import deepcopy
#Example of backtracking: not for optimization looking for ALL solutions. AKA brute force approach to solving problems.
# depth first search





class Sudoku(object):
	def __init__(self):
		self.puzzleSolution = []
		self.puzzleEasy = []
		self.puzzleNormal = []
		self.puzzleHard = []

		self.createPuzzle()
		self.makeEasy()
		self.makeNormal()
		self.makeHard()

	def createPuzzle(self):
		newGrid = [[0,0,0,  0,0,0,  0,0,0],
				   [0,0,0,  0,0,0,  0,0,0],
				   [0,0,0,  0,0,0,  0,0,0],

				   [0,0,0,  0,0,0,  0,0,0],
				   [0,0,0,  0,0,0,  0,0,0],
				   [0,0,0,  0,0,0,  0,0,0],

				   [0,0,0,  0,0,0,  0,0,0], 
				   [0,0,0,  0,0,0,  0,0,0],
				   [0,0,0,  0,0,0,  0,0,0]]

		for num in range(3):
			i = num * 3
			array = [1,2,3,4,5,6,7,8,9]
			for j in range(3):
				newGrid[0+i][j+i] = array.pop(randint(0,len(array)-1))
				newGrid[1+i][j+i] = array.pop(randint(0,len(array)-1))
				newGrid[2+i][j+i] = array.pop(randint(0,len(array)-1))
		self.puzzleSolution = Node(newGrid).solvePuzzleSetup()


	
	def makeEasy(self):
		self.puzzleEasy = deepcopy(self.puzzleSolution)

		easy = 43
		pos = 0
		while easy > 0:
			###########
			if pos > 7:
				pos = 0
			###########

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll()
				if self.puzzleEasy[x][y] == 0:
					continue
				self.puzzleEasy[x][y] = 0
				easy -= 1

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll() + 3
				if self.puzzleEasy[x][y] == 0:
					continue
				self.puzzleEasy[x][y] = 0
				easy -= 1

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll() +  + 6
				if self.puzzleEasy[x][y] == 0:
					continue
				self.puzzleEasy[x][y] = 0
				easy -= 1 
			pos += 3


	def makeHard(self):
		self.puzzleHard = deepcopy(self.puzzleSolution)
		hard = 56
		pos = 0
		while hard > 0:
			###########
			if pos > 7:
				pos = 0
			###########

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll()
				if self.puzzleHard[x][y] == 0:
					continue
				self.puzzleHard[x][y] = 0
				hard -= 1

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll() + 3
				if self.puzzleHard[x][y] == 0:
					continue
				self.puzzleHard[x][y] = 0
				hard -= 1

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll() +  + 6
				if self.puzzleHard[x][y] == 0:
					continue
				self.puzzleHard[x][y] = 0
				hard -= 1 
			pos += 3



	def makeNormal(self):
		self.puzzleNormal = deepcopy(self.puzzleSolution)
		normal = 51
		pos = 0
		while normal > 0:
			###########
			if pos > 7:
				pos = 0
			###########

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll()
				if self.puzzleNormal[x][y] == 0:
					continue
				self.puzzleNormal[x][y] = 0
				normal -= 1

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll() + 3
				if self.puzzleNormal[x][y] == 0:
					continue
				self.puzzleNormal[x][y] = 0
				normal -= 1

			for i in range(self.roll()):
				x = self.roll() + pos
				y = self.roll() +  + 6
				if self.puzzleNormal[x][y] == 0:
					continue
				self.puzzleNormal[x][y] = 0
				normal -= 1 
			pos += 3
	
	
	
	def roll(self):
		return randint(0,2)




	def printPuzzle(self, x):
		for i in x:
			for spot in i:
				print(str(spot) + ",",end = '')
			print('\n')
		print('\n' +'\n')
	
		


class Node(object):
	def __init__(self, puzzle, row = 0, collumn = 0, num = 0):
		self.puzzle = puzzle
		self.posRow = row
		self.posCollumn = collumn
		self.num = num

	#conditions:
	#1: cant be on the row
	#2: cant be on the collumn
	#3: cant be in 3x3 box

	#possible to simplify it by just doing if possible[num]: return true

	#checking the row to check if Num is present

	def Con1(self, puzzle, row, num):
		for i in range(9):
			if num == puzzle[row][i]:
				return False
		return True

	#check the collumn to see if Num is present
	def Con2(self, puzzle, collumn, num):
		for i in range(9):
			if num == puzzle[i][collumn]:
				return False
		return True
	
	#checking the box to see if the number is present
	def Con3(self, puzzle, row, collumn, num): #if the number is in the box return false
		boxRow = round((row - 1) / 3) #used to calculate which box row it's in
		boxCollumn = round((collumn - 1) /3)# calculate which box collumn
		for r in range(3):
			for c in range(3):
				if num == puzzle[(boxRow *3) + r][(boxCollumn * 3)	+ c]: #wrong row collumn
					return False
		return True

	def checkCon(self, puzzle, row, collumn, num):
		if self.Con1(puzzle, row, num):
			if self.Con2(puzzle,collumn, num):
				if self.Con3(puzzle, row, collumn, num):
					return True
		return False

	def solvePuzzleSetup(self):
		self.puzzle = self.solvePuzzle()
		return self.puzzle
	
	def printPuzzle(self):
		for i in self.puzzle:
			for spot in i:
				print(str(spot) + ",",end = '')
			print('\n')
	print('\n' +'\n')

	def solvePuzzle(self):
		#exit condition
		if self.posRow == 9: 
			return self.puzzle

		#If number is already present
		elif self.puzzle[self.posRow][self.posCollumn] > 0:
			if self.posCollumn > 7:
				x = Node(self.puzzle, self.posRow + 1, 0)
				y = x.solvePuzzle()
				if y != None:
					return y
			else:
				x = Node(self.puzzle, self.posRow, self.posCollumn + 1)
				y = x.solvePuzzle()
				if y != None:
					return y
		#default case
		else:
			for i in range(9):
				num = i + 1
				self.puzzle[self.posRow][self.posCollumn] = 0
				if self.checkCon(self.puzzle, self.posRow, self.posCollumn, num):
					if self.posCollumn > 7:
						self.puzzle[self.posRow][self.posCollumn] = num
						x = Node(self.puzzle, self.posRow + 1, 0)
						y = x.solvePuzzle()
						if y != None:
							return y
					else:
						self.puzzle[self.posRow][self.posCollumn] = num
						x = Node(self.puzzle, self.posRow, self.posCollumn + 1)
						y = x.solvePuzzle()
						if y != None:
							return y
		return None
