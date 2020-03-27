
import board
import player

score = 0
grid = board.make_board(6, 6)
# Creates randomly generated numbers.
board.create_elements(grid)
# Checks for already existing match and replaces it with other randomly generated numbers.
board.check_match(grid)

while score < 500:
	# Checks if a possible match exists.
	if board.change_x_elements(grid) or board.change_y_elements(grid):
		# Displays the valid board to the user.
		board.print_pretty_board(grid)
		# Prompts the user on where to switch.
		player.switch_elements(grid)
		if board.x_match_made(grid):
			# Replaces matched elements in the row.
			board.replace_x_matched(grid)
			score += 50
			# If a match is made after replacing it is replaced and points are awarded.
			while board.x_match_made(grid) or board.y_match_made(grid):
				if board.x_match_made(grid):
					board.replace_x_matched(grid)
					score += 50
				elif board.y_match_made(grid):
					board.replace_y_matched(grid)
					score += 50
			print('Your current score is ' + str(score))
		elif board.y_match_made(grid):
			# Replaces elements made in the columns.
			board.replace_y_matched(grid)
			score += 50
			# If a match is made after replacing it is replaced and points are awarded.
			while board.x_match_made(grid) or board.y_match_made(grid):
				if board.x_match_made(grid):
					board.replace_x_matched(grid)
					score += 50
				elif board.y_match_made(grid):
					board.replace_y_matched(grid)
					score += 50
			print('Your current score is ' + str(score))
		else:
			value = player.hint_move(grid)
			print('****INVALID MOVE****')
			print('Hint Move')
			print(value)
			player.switch_elements(grid)
			if board.x_match_made(grid):
				# Replaces matched elements in the row.
				board.replace_x_matched(grid)
				score += 50
				# If a match is made after replacing it is replaced and points are awarded.
				while board.x_match_made(grid) or board.y_match_made(grid):
					if board.x_match_made(grid):
						board.replace_x_matched(grid)
						score += 50
					elif board.y_match_made(grid):
						board.replace_y_matched(grid)
						score += 50
				print('Your current score is ' + str(score))
			elif board.y_match_made(grid):
				# Replaces elements made in the columns.
				board.replace_y_matched(grid)
				score += 50
				# If a match is made after replacing it is replaced and points are awarded.
				while board.x_match_made(grid) or board.y_match_made(grid):
					if board.x_match_made(grid):
						board.replace_x_matched(grid)
						score += 50
					elif board.y_match_made(grid):
						board.replace_y_matched(grid)
						score += 50
				print('Your current score is ' + str(score))

	# Creates a new board if there no match in the existing board.
	else:
    	# Creates randomly generated numbers.
		board.create_elements(grid)
		# Checks for already existing match and replaces it with other randomly generated numbers.
		board.check_match(grid)
print('================')
print('END OF GAME')
print('Your score is ' + str(score))
print('================')

