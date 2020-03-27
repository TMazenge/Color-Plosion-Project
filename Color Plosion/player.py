import board

def get_positions():
  """Creates a grid with the specified height and width.

	Args:
		No arguments

	Returns:
		The direction inwhich the user wants to move.
	"""	
  indices = []
  direction = {}
	# Asks the user for direction to change.
  coordinate = input('Which direction to move (x/y): ')
  if coordinate == 'x':
		# If direction is x, the program asks for the row.
    row = input('What is the row: ')
    direction['row'] = int(row)
  elif coordinate == 'y':
		# If the direction is y, the program asks for the column.
    col = input('What is the column: ')
    direction['col'] = int(col)
	# Asks the user for the intial index to move from.
  initial = input('What is the initial position: ')
  indices.append(int(initial))
	# Asks the user for the final index to move to.
  final = input('What is the final position: ')
  indices.append(int(final))
  direction[coordinate] = indices
  return direction

def hint_move(grid):
	'''Give user hint after first trial.

	Args:
		grid: 6 X 6 generated 2D list.

	Returns:
		A possible move that can be used by the user.
	'''
	possible_move = {}
	for  row in range(len(grid)):
	    for col in range(len(grid[row]) - 1):
	    	# Switches two elements  in a row.
		    first_value = grid[row][col]
		    second_value = grid[row][col + 1]
		    grid[row][col] = second_value
		    grid[row][col + 1] = first_value
		    # Checks if match was made in the rows or columns.
		    if board.x_match_made(grid) or board.y_match_made(grid):
		    	# Changes the two elements to their original positions.
		    	grid[row][col] = first_value
		    	grid[row][col + 1] = second_value
		    	possible_move['row'] = row
		    	possible_move['col'] = col
		    	return possible_move
		    else:
		    	grid[row][col] = first_value
		    	grid[row][col + 1] = second_value
	grid[row][col] = first_value
	grid[row][col + 1] = second_value
	possible_move['row'] = row
	possible_move['col'] = col
	return possible_move	    	

def switch_elements(grid):
	"""Switch elements in the grid as specified by the user.

	Args:
		grid: The created grid.

	Returns:
		Grid after elements had been switched.		
	"""	
	position = get_positions()
	for key in position:
		if key == 'x':
			row = position['row']
      		# Gets the initial index. 
			num1 = position[key][0]
      		# Gets the final index.
			num2 = position[key][1]
			first_value = grid[row][num1]
			second_value = grid[row][num2]
     		# Switches to elements in the given row.
			grid[row][num1] = second_value
			grid[row][num2] = first_value
		elif key == 'y':
			col = position['col']
      		# Gets the initial index.
			num1 = position[key][0]
     		# Gets the final index.
			num2 = position[key][1]
			first_value = grid[num1][col]
			second_value = grid[num2][col]
            # Switches to elements in the given row.
			grid[num1][col] = second_value
			grid[num2][col] = first_value

	# If an invalid move has been made, elements are switchced back.
	if not board.x_match_made(grid) and not board.y_match_made(grid):
		for key in position:
			if key == 'x':
				row = position['row']
	      		# Gets the initial index. 
				num1 = position[key][0]
	      		# Gets the final index.
				num2 = position[key][1]
				first_value = grid[row][num1]
				second_value = grid[row][num2]
	     		# Switches to elements in the given row.
				grid[row][num1] = second_value
				grid[row][num2] = first_value
			elif key == 'y':
				col = position['col']
	      		# Gets the initial index.
				num1 = position[key][0]
	     		# Gets the final index.
				num2 = position[key][1]
				first_value = grid[num1][col]
				second_value = grid[num2][col]
	            # Switches to elements in the given row.
				grid[num1][col] = second_value
				grid[num2][col] = first_value	
	return grid
