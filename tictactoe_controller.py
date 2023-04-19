import tictactoe_view, tictactoe_grid
from PyQt5.QtWidgets import QPushButton
from functools import partial


class TictactoeController:
	def __init__(self):
		self.tictactoe_grid_object = tictactoe_grid.TictactoeGrid()
		self.tictactoe_view_object = tictactoe_view.TictactoeView()
		self.connect_widgets()
		self.tictactoe_view_object.show()



	def connect_widgets(self):
		for index_line in range(0, 3):
			for index_column in range(0, 3):
				self.tictactoe_view_object.findChild(QPushButton, f'push_button_{index_line}_{index_column}').clicked.connect(partial(self.update_game, index_line, index_column))

		self.tictactoe_view_object.try_again_button.clicked.connect(self.new_game)


	def update_game(self, index_line, index_column):
		
		if self.tictactoe_grid_object.is_cell_empty(index_line, index_column):
			self.tictactoe_view_object.check_cell(index_line, index_column, self.tictactoe_grid_object.turn)

			self.tictactoe_grid_object.update_grid(index_line, index_column)
			game_state = self.tictactoe_grid_object.get_game_state()

			self.tictactoe_view_object.update_grid_view(game_state)




	def new_game(self):
		self.tictactoe_view_object.reset_view()
		self.tictactoe_grid_object.reset_model()
