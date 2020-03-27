import random

def make_board(height, width):
	"""Creates a grid with the specified height and width.

	Args:
		height: An integer that represents the height of grid(rows).
		width: An integer that represents the width(columns).

	Returns:
		A grid with the specified rows and columns.
	"""
	grid = []
	for row in range(0, height):
		# Adds a new row to the grid.
		grid.append([])
		for col in range(0, width):
			# Adds a new column to the grid.
			grid[row].append(0)
	return grid

def create_elements(grid):
	"""Generates elements which are random numbers between 0 and 5.
	   The numbers numbers represents different colors on the the grid.
	   0 - Red
	   1 - Orange
	   2 - Yellow
	   3 - Green
	   4 - Blue
	   5 - Purple
	Args:
		grid: The empty grid that has no elements.

	Returns:
		A grid with randomly generated elements.
	"""
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			# Adds a randomly element to the grid.
			num = random.randint(0, 5)
			grid[row][col] = num
	return grid

def print_pretty_board(grid):
	"""Displays the grid nicely in the consule.

	Args:
		grid: A grid that needs to be shown to the user.

	Returns:
		A grid is displayed nicely in the consule.
	"""
	for row in range(len(grid)):
		print(grid[row])

def x_match(grid):
	"""Checks to see if a match of 3 adjacent numbers in the same
	   row already exists in new created grid.

	Args:
		grid: New created grid.

	Returns:
		A grid with no 3 matching adjacent numbers in a row.
	"""
	for row in range(len(grid)):
		for col in range(len(grid[row]) - 2):
			# Accesses three adjacent numbers in the same row. 
			x_col1 = grid[row][col]
			x_col2 = grid[row][col + 1]
			x_col3 = grid[row][col + 2]
			# Checks to see if the three adjacent numbers match.
			if x_col1 == x_col2 and x_col2 == x_col3:
				# If the numbers match, the first number is replaced by a randomly gerated number. 
				num = random.randint(0, 5)
				if num != x_col1:
					grid[row][col] = num
				else:
					# The first number is only replaced if new number is not equal to the old one.
					while num == x_col1:
						num = random.randint(0, 5)
					grid[row][col] = num
	return grid

def y_match(grid):
	"""Checks to see if match of 3 adjacent numbers in the same
	   column already exists in new created grid.

	Args:
		grid: New created grid.

	Returns:
		A grid with no 3 matching adjacent numbers in the same column.
	"""
	for row in range(len(grid) - 2):
		for col in range(len(grid[row])):
			# Accesses three adjacent numbers in the same column.
			y_row1 = grid[row][col]
			y_row2 = grid[row + 1][col]
			y_row3 = grid[row + 2][col]
			if (y_row1 == y_row2) and (y_row2 == y_row3):
				# If the numbers match, the first number is replaced by a randomly gerated number.
				num = random.randint(0, 5)
				if num != y_row1:
					grid[row][col] = num
				else:
					# The first number is only replaced if new number is not equal to the old one.
					while num == y_row1:
						num = random.randint(0, 5)
					grid[row][col]	= num
	return grid

def check_match(grid):
	"""Checks to see if match of 3 adjacent numbers in the same
	   rows or columns already exists in new created grid and clears it.

	Args:
		grid: New created grid.

	Returns:
		A grid with no 3 matching adjacent numbers in the same row or column.
	"""
	grid1 = x_match(grid)
	grid2 = y_match(grid1)
	return grid2

def x_match_made(grid):
	"""Checks to see if match of 3 adjacent numbers in the same
	   row has been made.

	Args:
		grid: New created grid.

	Returns:
		A boolean value whether a match had been made in the row.
	"""
	for row in range(len(grid)):
		for col in range(len(grid[row]) - 2):
			# Accesses three adjacent numbers in the same row.
			x_col1 = grid[row][col]
			x_col2 = grid[row][col + 1]
			x_col3 = grid[row][col + 2]
			# Returns True if the numbers match.
			if x_col1 == x_col2 and x_col2 == x_col3:
				return True
	return False

def y_match_made(grid):
	"""Checks to see if match of 3 adjacent numbers in the same
	   row has been made.

	Args:
		grid: New created grid.

	Returns:
		A boolean value whether a match had been made in the row.
	"""
	for row in range(len(grid) - 2):
		for col in range(len(grid[row])):
			# Accesses three adjacent numbers in the same column.
			y_row1 = grid[row][col]
			y_row2 = grid[row + 1][col]
			y_row3 = grid[row + 2][col]
			# Returns True if the numbers match.
			if (y_row1 == y_row2) and (y_row2 == y_row3):
				return True
	return False

def change_x_elements(grid):
	"""Checks to see if a match of 3 adjacent numbers is possible after
	   a switch has been made in the row.

	Args:
		grid: A created grid.

	Returns:
		A boolean value to check if there is a possible match.
	"""
	for  row in range(len(grid)):
	    for col in range(len(grid[row]) - 1):
	    	# Switches two elements  in a row.
		    first_value = grid[row][col]
		    second_value = grid[row][col + 1]
		    grid[row][col] = second_value
		    grid[row][col + 1] = first_value
		    # Checks if match was made in the rows or columns.
		    if x_match_made(grid) or y_match_made(grid):
		    	# Changes the two elements to their original positions.
		    	grid[row][col] = first_value
		    	grid[row][col + 1] = second_value
		    	return True
		    else:
		    	# If no match was found it returns the two elements to their original position.
		    	grid[row][col] = first_value
		    	grid[row][col + 1] = second_value
	# If no match was found it returns the two elements to their original position.
	grid[row][col] = first_value
	grid[row][col + 1] = second_value
	return False

def change_y_elements(grid):
	"""Checks to see if a match of 3 adjacent numbers is possible after
	   a switch has been made in the column.

	Args:
		grid: A created grid.

	Returns:
		A boolean value to check if there is a possible match.
	"""
	for row in range(len(grid) - 1):
		for col in range(len(grid[row])):
			# Switches two elements  in a row.
			first_value = grid[row][col]
			second_value = grid[row + 1][col]
			grid[row][col] = second_value
			grid[row + 1][col] = first_value
			# Checks if match was made in the rows or columns.
			if x_match_made(grid) or y_match_made(grid):
				# Changes the two elements to their original positions.
				grid[row][col] = first_value
				grid[row + 1][col] = second_value
				return True
			else:
				# Changes the two elements to their original positions.
				grid[row][col] = first_value
				grid[row + 1][col] = second_value
	# Changes the two elements to their original positions.
	grid[row][col] = first_value
	grid[row + 1][col] = second_value
	return False

def replace_x_matched(grid):
	"""Replaces the three matched elements in the same row.

	Args:
		grid: A grid with three matched elements in the same row.

	Returns:
		A grid with matched elements replaced
	"""
	for row in range(len(grid)):
		for col in range(len(grid[row]) - 2):
			# Accesses three adjacent numbers in the same column.
			x_col1 = grid[row][col]
			x_col2 = grid[row][col + 1]
			x_col3 = grid[row][col + 2]
			# Checks to see if three adjacent numbers are the same.
			if x_col1 == x_col2 and x_col2 == x_col3:
				# If its the first row the elements are replaced by randomly generated numbers.
				if row == 0:
					grid[row][col] = random.randint(0, 5)
					grid[row][col + 1] = random.randint(0, 5)
					grid[row][col + 2] = random.randint(0, 5)
				else:
					while row > 0:
						# If row is greater than zero elements are replaced by elements in the previous row.
						grid[row][col] = grid[row - 1][col]
						grid[row][col + 1] = grid[row - 1][col + 1]
						grid[row][col + 2] = grid[row - 1][col + 2]
						row -= 1
					grid[row][col] = random.randint(0, 5)
					grid[row][col + 1] = random.randint(0, 5)
					grid[row][col + 2] = random.randint(0, 5)
	return grid

def replace_y_matched(grid):
	"""Replaces elements in the same column.

	Args:
		grid: A grid with three matched elements in the same column.

	Returns:
		A grid with matched elements replaced.
	"""
	for row in range(len(grid) - 2):
		for col in range(len(grid[row])):
			# Accesses three adjacent numbers in the same column.
			y_row1 = grid[row][col]
			y_row2 = grid[row + 1][col]
			y_row3 = grid[row + 2][col]
			# Checks to see if adjacent elements are the same.
			if y_row1 == y_row2 and y_row2 == y_row3:
				num1 = row - 3
				num2 = row - 2
				num3 = row - 1
				"""Subtracts 3 from the row and checks if new row is greater than 0.
				   If the new row is less than zero, the element is randomly generated.
				   If new row is greater than zero the matched element will be replaced
				   by the element at the new row.
				   The element at the new row is randomly generated.
				"""
				if num3 >= 0:
					grid[row + 2][col] = grid[num3][col]
					grid[num3][col] = random.randint(0, 5)
				else:
					grid[row + 2][col] = random.randint(0, 5)

				if num2 >= 0:
					grid[row + 1][col] = grid[num2][col]
					grid[num2][col] = random.randint(0, 5)
				else:
					grid[row + 1][col] = random.randint(0, 5)
					
				if num1 >= 0:
					grid[row][col] = grid[num1][col]
					grid[num1][col] = random.randint(0, 5)
				else:
					grid[row][col] = random.randint(0, 5)
	return grid




					












	
