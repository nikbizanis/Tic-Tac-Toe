
# Global variables of the game
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
winningCombs = [{1,4,7}, {1,2,3}, {2,5,8}, {3,6,9}, {4,5,6}, {7,8,9}, {1,5,9}]
markers = []
turn = 1		# Who's turn it is to play
player1_moves = []
player2_moves = []




def display_board():
# Print the tic tac toe board

	print("\n" * 100)

	print('   |   |   ')
	print(' {} | {} | {} '.format(board[1], board[2], board[3]))
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' {} | {} | {} '.format(board[4], board[5], board[6]))
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' {} | {} | {} '.format(board[7], board[8], board[9]))
	print('   |   |   ')



def check_winning(moves):
# Check if player's moves include a winning combination to stop the game
	
	moves = set(moves)

	for combination in winningCombs:
		if combination.intersection(moves) == combination:
			return True
	
	return False



def marker_assignment():
# Assigns markers to players according to their preferences - reading from input
	
	while True:
		firstMarker = input("Player 1, do you wish to use X or O?")

		if firstMarker.upper() == "X" or firstMarker.upper() == "O":
			break

	if firstMarker.upper() == "X":
		return ["X", "O"]
	else:
		return ["O", "X"]



def place_marker(marker, position):
# Assigns marker to the board and move to the respective player
	
	board[position] = marker
	display_board()


    

def toggle_turn(play_turn):
# Toggles the player turn to play
	
	if play_turn == 1:
		play_turn+=1
	else:
		play_turn-=1

	return play_turn



def occupied(pos):
# Check if that particular position is occupied on the board

	if board[pos] != " ":
		return True
	else:
		return False



# Displays the board and asks for markers assignment
display_board()
markers = marker_assignment()


# The game starts!
while True:
	# Player makes a move

	if turn == 1:
		position = int(input("Player 1 make your move: "))

		if occupied(position):
			print("This position is occupied. Make another move.")
			continue

		place_marker(markers[turn-1], position)
		player1_moves.append(position)

		if check_winning(player1_moves):
			print("Player 1 wins!")
			break
	else:
		position = int(input("Player 2 make your move: "))

		if occupied(position):
			print("This position is occupied. Make another move.")
			continue

		place_marker(markers[turn-1], position)
		player2_moves.append(position)

		if check_winning(player2_moves):
			print("Player 2 wins!")
			break

	if " " not in board:
		print("It's a draw")	# If the board got full the game stops with a draw
		break

	turn = toggle_turn(turn)
