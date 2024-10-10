class Player():
  def __init__(self, token):
    self.token = token

  def move(self):
    user_input = input(f"{ self.token }'s Turn: Enter (1-9): ")
    index = int(user_input) - 1
    return index