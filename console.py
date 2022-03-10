from ursina import *
from game import *
from level0 import *
from player import *
from items import *

class Console:
  def __init__(self):
    self.console = Entity(parent="camera.ui")
    self.console_background = Entity(model="cube", color=rgb(30, 180, 30, 200), parent=self.console)
    self.console_output_area = Entity(model="cube", color=Color.black, parent=self.console)
    self.console_output = []
    
  
  def appear(self):
    self.cosnole.enable()
  
  def disappear(self):
    self.console.disable()
     
  def test_output(self, text):
    self.console_output.append(text)