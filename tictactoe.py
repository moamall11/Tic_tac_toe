from player import *
import time

class TicTacToe:
	"""represents the game"""
	def __init__(self):
		"""initialize the attributes"""
		#the list of the squares of the board.
		self.board=[' ' for _ in range(9)]
		self.current_winner=None

	def available_moves(self):
		"""returns the numbers of the available moves"""
		return [i for i,letter in enumerate(self.board) if letter==' ']

	def print_board(self):
		"""print the board without numbers"""
		for row in [self.board[i:i+3] for i in range(0,7,3)]:
			print('|',' | '.join(row),'|')

	def print_board_nums(self):
		"""print the board with numbers"""
		for row in [[str(i) for i,letter in enumerate(self.board)][i:i+3]\
		 for i in range(0,7,3)]:
		 	print('|',' | '.join(row),'|')

	def make_move(self,square,letter):
		"""assigns a square to a letter"""
		self.board[square]=letter
		self.current_winner = self.check_winner(square,letter)

	def check_winner(self,square,letter):
		"""check all the possibilities of winning"""
		#check the row.
		row_num=square // 3
		if all(i==letter for i in self.board[row_num*3:(row_num*3)+3]):
			return letter

		#check the column.
		column_num=square % 3
		if all(i==letter for i in [self.board[j] \
			for j in range(column_num,9,3)]):
			return letter

		#check the diagonals (0,2,4,6,8).
		diagonal1=[self.board[j] for j in [0,4,8]] #left to right.
		if all(i==letter for i in diagonal1): 
			return letter
		diagonal2=[self.board[j] for j in [2,4,6]] #right to left.
		if all(i==letter for i in diagonal2): 
			return letter
		#no winning.
		return None


def play(game,x_player,o_player,print_board=True):
	"""the main function of the game returns the letter of the winner"""
	#the letter that will play first.
	letter='X'
	if print_board:
		game.print_board_nums()
	while game.available_moves():
		if letter == 'X':
			x_player.get_move(game)
		else:
			o_player.get_move(game)
		if print_board:
			game.print_board()
		#return the winner
		if game.current_winner:
			if print_board:
				print(letter,'wins!')
			return letter
			
		#change the turn (change letter/switch players).
		letter='O' if letter=='X' else 'X'
		if print_board:
			time.sleep(0.8)

	if print_board:
		print("it's a tie!")

if __name__=='__main__':
	# t=TicTacToe()
	# x_player=Human('X')
	# o_player=AI_Computer('O')
	# play(t,x_player,o_player)
	x_wins=0
	o_wins=0
	ties=0
	
	for _ in range(1000):
		t=TicTacToe()
		x_player=AI_Computer('X')
		o_player=Computer('O')
		result=play(t,x_player,o_player,False)
		if result=='X':
			x_wins+=1
		elif result=='O':
			o_wins+=1
		else:
			ties+=1
	print(f"x_wins={x_wins}\no_wins={o_wins}\nties={ties}")