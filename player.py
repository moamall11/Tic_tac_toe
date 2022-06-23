import random
import math

class Player:
	"""represents any player"""
	def __init__(self,letter):
		"""initialize the values"""
		self.letter=letter

class Human(Player):
	"""represents the human player"""
	def __init__(self,letter):
		"""initialize the values from the super class""" 
		super().__init__(letter)

	def get_move(self,game):
		val=True
		while val:
			square=input("which square do you choose (0-8)? ")
			try:
				square=int(square)
				if square not in game.available_moves():
					raise ValueError
			except ValueError: #when the input is not a number 
			#or the move is not available raise an error.
				print("invalid move. try again.")
			else:
				game.make_move(square,self.letter)
				val=False
			


class Computer(Player):
	"""represents the computer random player"""
	def __init__(self,letter):
		"""initialize the values from the super class"""
		super().__init__(letter)

	def get_move(self,game):
		"""get a random move"""
		square=random.choice(game.available_moves())
		game.make_move(square,self.letter)

class AI_Computer(Player):
	"""represents the computer with the minimax algorithm"""
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		if len(game.available_moves()) == 9:
			square=random.choice(game.available_moves())
		else:
			square=self.minimax(game,self.letter)['position']
		game.make_move(square,self.letter)

	def minimax(self,game,player):
		"""the algorithm"""
		#determine the other player's letter.
		other_player='X' if player=='O' else 'O'
		available_moves_num=len(game.available_moves())
		#the other player is the computer 
		#when the player is user and vice versa.
		#the position of the move will be determined later.
		if game.current_winner==other_player:
			return {'position':None,'score':1 * (available_moves_num + 1)
			if other_player==self.letter else -1 * (available_moves_num + 1)}
		#when it's a tie.
		elif available_moves_num == 0:
			return {'position':None,'score':0}
		#the best move for the computer is the one that has the highest score
		#and for the user the one that has the lowest score.
		if player==self.letter:
			best={'position':None,'score':-math.inf} #will increase.
		else:
			best={'position':None,'score':math.inf} #will decrease.

		for possible_move in game.available_moves():
			#make the possible move.
			game.make_move(possible_move,player)
			#see what is the best that the other player can do.
			sim_score=self.minimax(game,other_player)
			#undo the move and clear the winner.
			game.board[possible_move]=' '
			game.current_winner=None
			#save the position of the move (will be used in the best move).
			sim_score['position']=possible_move
			#determine the best move so far depending on the score.
			if player==self.letter:
				if sim_score['score'] > best['score']:
					best=sim_score
			else:
				if sim_score['score'] < best['score']:
					best=sim_score
		return best
