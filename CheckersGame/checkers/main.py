##########################IMPORTS######################
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax
#######################################################


######################CREATE DISPLAY###################

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")

#######################################################

#############MOUSE LISTENER POSITION FUNCTION##########

def get_row_col_from_mouse(pos):
	x, y = pos
	row = y // SQUARE_SIZE
	col = x // SQUARE_SIZE
	return row, col



######################################################

####################MAIN FUNCTION######################

def main():
	run = True
	#Constant Frame Rate
	clock = pygame.time.Clock()
	#Creates board object
	game = Game(WIN)
	
	
	while run:
		clock.tick(FPS)
		
		
		if game.turn == WHITE:
			value, new_board = minimax(game.get_board(), 3, WHITE, game)   #Number 3 is depth of tree for computer to 'think' through the AI to make move--Higher number = longer wait time
			game.ai_move(new_board)
			
		
		
		if game.winner() != None:
			print(game.winner())
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col = get_row_col_from_mouse(pos)
				game.select(row, col)
				
		game.update()
	
	pygame.quit()



		
main()