import numpy

class TictactoeGrid:
	def __init__(self, grid_id=None):
		self.grid_id = grid_id
		self.grid = numpy.zeros((3, 3), dtype=numpy.uint8)
		self.turn = 1
		self.game_in_progress = True
		self.there_is_winner = False

		self.history = []
		


	def is_cell_empty(self, index_line, index_column):
		return self.grid[index_line, index_column] == 0

	def update_grid(self, index_line, index_column):
		self.grid[index_line, index_column] = self.turn
		self.history.append(index_line*3 + index_column)

		self.there_is_winner = (numpy.all(self.grid[0,:] == self.grid[0, 0]) and self.grid[0, 0] != 0 ) or\
						  		(numpy.all(self.grid[1,:] == self.grid[1, 0]) and self.grid[1, 0] != 0 ) or\
						  		(numpy.all(self.grid[2,:] == self.grid[2, 0]) and self.grid[2, 0] != 0 ) or\
						 		(numpy.all(self.grid[:, 0] == self.grid[0,0]) and self.grid[0, 0] != 0 ) or\
						  		(numpy.all(self.grid[:, 1] == self.grid[0,1]) and self.grid[0, 1] != 0 ) or\
						  		(numpy.all(self.grid[:, 2] == self.grid[0,2]) and self.grid[0, 2] != 0 ) or\
						  		(numpy.all(self.grid.diagonal() == self.grid[0,0]) and self.grid[0, 0] != 0)or\
						  		(numpy.all(numpy.fliplr(self.grid).diagonal() == self.grid[0,2]) and self.grid[0, 2] != 0)


		if self.there_is_winner:
			self.game_in_progress = False

		self.game_in_progress = not numpy.all(self.grid != 0) if self.game_in_progress else False


		if self.game_in_progress:
			self.turn = 2 if self.turn == 1 else 1


		
	def reset_model(self):
		self.grid = numpy.zeros((3, 3), dtype=numpy.uint8)
		self.turn = 1
		self.game_in_progress = True
		self.there_is_winner = False


	def get_game_state(self):
		return {"turn" : self.turn,\
				"game_in_progress" : self.game_in_progress,\
				"there_is_winner": self.there_is_winner}

	def __str__(self):
		return f"La grille de la partie :\n{self.grid}"