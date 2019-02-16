
from globals import config


def display_board():
# Print the tic tac toe board

	print("\n" * 100)

	print('   |   |   ')
	print(' {} | {} | {} '.format(config.board[1], config.board[2], config.board[3]))
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' {} | {} | {} '.format(config.board[4], config.board[5], config.board[6]))
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' {} | {} | {} '.format(config.board[7], config.board[8], config.board[9]))
	print('   |   |   ')



def check_winning(moves):
# Check if player's moves include a winning combination to stop the game

	moves = set(moves)

	for combination in config.winningCombs:
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

	config.board[position] = marker
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

	if config.board[pos] != " ":
		return True
	else:
		return False
