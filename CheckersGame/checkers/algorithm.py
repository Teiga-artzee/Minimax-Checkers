######################IMPORTS#################################

from copy import deepcopy
import pygame

#############################################################

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):            #pos= current position board is in, depth = how far into tree to search for move, max_player= looking for min eval or max eval, game= game object
	if depth == 0 or position.winner() != None:
		return position.evaluate(), position
		
	if max_player:
		maxEval = float('-inf')                            #If any move is higher then negative infinty, which all are, eval will be better
		best_move = None
		for move in get_all_moves(position, WHITE, game):         #Passes position into function to get all possible moves, WHITE = hard coded turn, but AI for computer turn, pass through game, for every single move it is evaluated
			evaluation = minimax(move, depth - 1, False, game)[0] #evaluation of moves call minimax function with given depth of tree desired.
			maxEval = max(maxEval, evaluation)                    #Now that we have evaluation, we now know how good it is
			if maxEval == evaluation:
				best_move = move                                  #Set as best move to make
		return maxEval, best_move
	
	
	else:
		minEval = float('inf')                                    #Consider for trying to get lowest score (min player)
		best_move = None                                          #consider what red(player) may do against player
		for move in get_all_moves(position, RED, game):           #The idea behind this is that red would always try to do their best and vice versa
			evaluation = minimax(move, depth - 1, True, game)[0]  #So considering what move opponet would do helps improve AI game play
			minEval = min(minEval, evaluation)
			if minEval == evaluation:
				best_move = move
		return minEval, best_move
	
###########################################################

#################GO THROUGH ALL POSSIBLE MOVES SIMULATION##

def simulate_move(piece, move, board, game, skip):
	board.move(piece, move[0], move[1])
	if skip:
		board.remove(skip)
		
	return board

##############GET ALL POSSIBLE MOVES FOR PIECE############
	
def get_all_moves(board, color, game): 
	moves = []
	
	for piece in board.get_all_pieces(color):                                #LOOP through all pieces of color on board
		valid_moves = board.get_valid_moves(piece)                           #Get all valid moves of piece on board
		for move, skip in valid_moves.items():                                #move through move dictionary
			temp_board = deepcopy(board)  
			temp_piece = temp_board.get_piece(piece.row, piece.col)                                   #Need to modify board to know new position w/o actually modify REAL game board--used for trying out moves for al
			new_board = simulate_move(temp_piece, move, temp_board, game, skip)   #If you make this move, new board will look like this.
			moves.append(new_board)
			
	return moves