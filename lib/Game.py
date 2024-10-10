from Board import Board
from Global import clear

class Game():

  WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
  ]

  def __init__(self, player_1, player_2, board=Board()):
    self.board = board
    self.player_1 = player_1
    self.player_2 = player_2

  def start(self):
    self.board.display()
    while not self.game_over():
      self.turn()

    if self.won():
      input(f"Congratulations Player {self.winner()}, press any key to continue")
    else:
      input("Cat's Game, press any key to continue")

  def turn_count(self):
    tokens = [token for token in self.board.cells if token != " "]
    return len(tokens)

  def turn(self):
    index = self.current_player().move()
    if self.board.valid_move(index):
      self.board.update(index, self.current_player().token)
      self.board.display()
    else:
      clear()
      input("Invalid Move, press any key to continue")
      self.board.display()
      self.turn()

    

  def current_player(self):
    return self.player_1 if self.turn_count() % 2 == 0 else self.player_2
  
  def won(self):
    # horizontal is the same token and not empty
    # verticle is the same token and not empty
    # diagnol is the same token and not empty

    for win_combo in Game.WIN_COMBINATIONS:
      index_1 = win_combo[0]
      index_2 = win_combo[1]
      index_3 = win_combo[2]

      token_1 = self.board.cells[index_1]
      token_2 = self.board.cells[index_2]
      token_3 = self.board.cells[index_3]

      if token_1 == token_2 and token_2 == token_3 and token_1 != " ":
        return True
    return False
  
  def cats_game(self):
    # board is full and someone didn't win the game
    return self.turn_count() == 9 and not self.won()

  
  def game_over(self):
    # if the game is either won or cat's game
    return self.cats_game() or self.won()
  
  def winner(self):
    return self.player_2.token if self.current_player().token == self.player_1.token else self.player_1.token