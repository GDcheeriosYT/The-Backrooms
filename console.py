from ursina import *
from game import *
from level0 import *
from player import *
from items import *

class Console:
  def __init__(self, open=False):
    self.console = Entity(parent="camera.ui")
    self.console_background = Entity(model="cube", color=rgb(30, 180, 30, 200), parent=self.console)
    self.console_output_area = Entity(model="cube", color=rgb(0, 0, 0), parent=self.console)
    self.console_output = []
    self.open = open
    
  
  def appear(self):
    self.console.enable()
    self.open = True
  
  def disappear(self):
    self.console.disable()
    self.open = False
     
  def test_output(self, text):
    self.console_output.append(text)