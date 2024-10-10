from Global import clear

class Board():

  def __init__(self, cells=[" ", " ", " ", " ", " ", " ", " ", " ", " "]):
    self.cells = cells
  
  def display(self):
    clear()
    print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
    print("-----------")
    print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
    print("-----------")
    print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
    print("")

  def update(self, index, token):
    self.cells[index] = token

  def position_taken(self, index):
    return self.cells[index] != " "
  
  def valid_move(self, index):
    return index in range(0, 9) and not self.position_taken(index)
  
