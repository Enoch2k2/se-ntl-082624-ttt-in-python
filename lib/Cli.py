
from Global import clear
from Game import Game
from Player import Player

class Cli():

  def start(self):
    clear()
    print("Welcome to Tic Tac Toe!")
    self.menu()

  def menu(self):
    print("")
    print("Type '1' for a 0 player game")
    print("Type '2' for a 1 player game")
    print("Type '3' for a 2 player game")
    print("Type 'exit' to exit program")
    print("")

    self.menu_selection()

  def menu_selection(self):
    user_input = input("Enter Here: ")

    if user_input == "1":
      clear()
      print("Starting 0 player game, Coming Soon!")
      self.menu()
    elif user_input == "2":
      clear()
      print("Starting 1 player game, Coming Soon!")
      
      self.menu()
    elif user_input == "3":
      clear()
      input("Press any key to start 2 player game")
      player_1 = Player("X")
      player_2 = Player("O")
      game = Game(player_1=player_1, player_2=player_2)
      game.start()
      clear()
      self.menu()
    elif user_input == "exit":
      clear()
      input("Press any key to exit program")
    else:
      clear()
      print("Invalid Selection, Please Try Again...")
      self.menu()
    
