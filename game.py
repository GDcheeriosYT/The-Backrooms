import json
import random

class Game:
  def __init__(self, name="game", password="", player_amount=0, players=[], status="game starting up", level="lobby", seed=random.randint(0, 999999999999)):
    self.name = name
    self.password = password
    self.player_amount = player_amount
    self.players = players
    self.status = status
    self.level = level
    self.seed = seed
  
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
  
  def update_status(self):
    self.status = f"{self.level} | {self.player_amount} players"
  
  def set_level(self, level):
    self.level = level
  
  def get_seed(self):
    return(self.seed)