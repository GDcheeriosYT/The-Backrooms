from ursina import *
from game import *
from level0 import *
from player import *
from items import *

class Console:
  def __init__(self, open=False):
    self.console = Entity(parent=camera.ui, position=(0, 0.25), scale=(2, 0.5))
    self.console_background = Entity(model="cube", color=rgb(80, 80, 80, 120), parent=self.console)
    self.console_output_area = Entity(model="cube", color=rgb(0, 0, 0), position=(0, 0.2), scale=(0.85, 0.7), parent=self.console)
    self.console_output = []
    self.console_input_area = Entity(model="cube", color=rgb(0, 0, 0), position=(0, -0.36), scale=(0.85, 0.2), parent=self.console)
    self.open = open
  
  def out(self, i):  
    self.console_output.append(i)
    
  def appear(self):
    self.console.enable()
    self.console_output_text = Text(text="", position=(-0.8, 0.5))
    try:
      self.input.enable()
      self.input.text_field.enable()
    except:
      self.input = InputField(max_lines = 1, position=(0, -0.36), scale=(0.85, 0.2), text_field=TextField(position=(-0.8, 0.08), world_parent=self, max_lines=1), parent=self.console)
    self.input.input("enter")
    self.open = True
    
  
  def disappear(self):
    self.console.disable()
    try:
      self.input.disable()
      self.input.text_field.disable()
      self.console_output_text.disable()
    except:
      pass
    self.open = False
  
  def output_log(self):
    for text in self.console_output:
      self.console_output_text.text += (text + "\n")
      self.console_output.pop(0)
    
    if len(str(self.console_output_text.text).splitlines()) == 13:
      self.console_output_text.text = ""