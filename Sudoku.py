import random


class SudokuSolver:

	@staticmethod
	def find_empty(matrix):
		"""

		:param matrix: 9x9 list matrix
		:return: tuple containing x and y coord of empty entry
		"""
		for y in range(9):
			for x in range(9):
				if matrix[y][x] == 0:
					return y, x

	@staticmethod
	def is_valid(coord, value, matrix):
		"""

		:param coord: tuple containing x,y coord of entry to be checked
		:param value: value of entry being checked
		:param matrix: 9x9 list matrix
		:return: True if valid, else None
		"""
		# Get the row and column from the coordinate
		row, column = coord

		# Check the row
		if value in matrix[row]:
			return

		# Check the column for each row of the matrix
		for i in matrix:
			if i[column] == value:
				return

		# Check the square
		y_start = (row // 3) * 3
		y_slice = slice(y_start, y_start + 3)
		x_start = (column // 3) * 3
		x_slice = slice(x_start, x_start + 3)
		sq_lists = [x[x_slice] for x in matrix[y_slice]]
		for sq in sq_lists:
			if value in sq:
				return

		return True

	def solve_puzzle(self, matrix):
		"""

		:param matrix: 9x9 list matrix
		:return: solved 9x9 list matrix
		"""
		# Find an empty cell
		cell = self.find_empty(matrix)
		if cell:
			for x in range(1, 10):
				# If the value is accepted add it to the coord
				if self.is_valid(cell, x, matrix):
					row, column = cell
					matrix[row][column] = x

					# If the puzzle is solved
					if self.solve_puzzle(matrix):
						return matrix

					matrix[row][column] = 0
		else:
			return matrix

	def generate_puzzle(self):
		"""

		:return: 9x9 list matrix
		"""
		sample = random.sample(range(1, 10), 9)
		# Create a matrix of 'empty' values
		puzzle = [[0 for _ in range(9)] for _ in range(9)]
		# Populate the first square with a randomised list of values
		for row in range(3):
			for column in range(3):
				puzzle[row][column] = sample[0]
				sample.pop(0)
		# Solve the rest of the puzzle
		self.solve_puzzle(puzzle)
		# Remove random values
		for y in puzzle:
			zero_indexes = random.sample(range(9), 5)
			for index in zero_indexes:
				y[index] = 0
		return puzzle

	@staticmethod
	def print_puzzle(puzzle):
		"""

		:param puzzle: 9x9 list martix
		"""
		for i, row in enumerate(puzzle):
			if i > 0 and i % 3 == 0:
				print('---------------------')
			for j, col in enumerate(row):
				if j > 0 and j % 3 == 0:
					print(f"| {col}", end=' ')
				elif j == 8:
					print(col)
				else:
					print(col, end=' ')
