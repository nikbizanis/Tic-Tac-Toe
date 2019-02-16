
from game_functionalities import functionalities
from globals import config



# Displays the board and asks for markers assignment
functionalities.display_board()
config.markers = functionalities.marker_assignment()


# The game starts!
while True:

	# Player makes a move
	if config.turn == 1:
		position = int(input("Player 1 make your move: "))

		if functionalities.occupied(position):
			print("This position is occupied. Make another move.")
			continue

		functionalities.place_marker(config.markers[config.turn-1], position)
		config.player1_moves.append(position)

		if functionalities.check_winning(config.player1_moves):
			print("Player 1 wins!")
			break
	else:
		position = int(input("Player 2 make your move: "))

		if functionalities.occupied(position):
			print("This position is occupied. Make another move.")
			continue

		functionalities.place_marker(config.markers[config.turn-1], position)
		config.player2_moves.append(position)

		if functionalities.check_winning(config.player2_moves):
			print("Player 2 wins!")
			break

	if " " not in config.board:
		print("It's a draw")	# If the board got full the game stops with a draw
		break

	config.turn = functionalities.toggle_turn(config.turn)
