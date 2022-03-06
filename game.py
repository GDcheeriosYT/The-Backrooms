import json

class Game:
  def __init__(self, name="game", password="", player_amount=0, players=[]):
    self.name = name
    self.password = password
    self.player_amount = player_amount
    self.players = players
  
  def set_name(self, new_name):
    self.name = new_name
  
  def set_password(self, new_password):
    self.password = new_password
  
  def add_player(self, player):
    self.players.append(player)
    self.player_amount += 1
  
  def remove_player(self, player):
    self.players.pop(player)
    self.player_amount -= 1