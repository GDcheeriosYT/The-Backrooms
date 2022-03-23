from ursina import *
from game import *
from level0 import *
from player import *
from items import *

class Console:
  def __init__(self, open=False, coordinates=(0,0,0)):
    self.console = Entity(parent=camera.ui, position=(0, 0.25), scale=(2, 0.5))
    self.console_background = Entity(model="cube", color=rgb(80, 80, 80, 120), parent=self.console)
    self.console_output_area = Entity(model="cube", color=rgb(0, 0, 0), position=(0, 0.2), scale=(0.85, 0.7), parent=self.console)
    self.console_output = []
    self.console_input_area = Entity(model="cube", color=rgb(0, 0, 0), position=(0, -0.36), scale=(0.85, 0.2), parent=self.console)
    self.open = open
    self.objects = []
    self.coordinates = coordinates
  
  def out(self, i):  
    self.console_output.append(i)
    print(i)
    
  def appear(self, player_coordinates):
    self.console.enable()
    self.coordinates = player_coordinates
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
  
  
  
  
  #commands  
  def spawn(self, type=None, type2=None, coordinates=(0,0,0)):
    try:
      coordinates = eval(coordinates)
    except:
      pass
    if str(type) == "item":
      if str(type2) == 'almondwater':
        try:
          object = AlmondWater(coordinates[0], coordinates[1], coordinates[2])
          self.objects.append(object)
          object.spawn()
        except:
          object = AlmondWater()
          self.objects.append(object)
          object.spawn()
    elif str(type) == "player":
      object = Player.spawn(x=coordinates[0], y=coordinates[1], z=coordinates[2], preview=True).set_immunity(True)
      self.objects.append(object)
    else:
      self.out(f"tf you want me to do with {type} & {coordinates}")
  
  
  
  
  def clear(self):
    for object in self.objects:
      object.disable()
      self.objects.pop(object)
  
  
  
  
  def list_objects(self):
    for object in self.objects:
      self.out(object.get_type())
  
  
  
  
  def command_help(self):
    self.out('''
help, for help
spawn type type2 (*args), used for spawning items, entities, and test players
clear, clears all things that have been spawned by the console
            ''')
  
  def handle(self, i):
    self.commands = {
      'spawn':self.spawn,
      'clear':self.clear,
      'list':self.list_objects,
      'help':self.command_help
    }
    
    
    args = i.split()
    try:
      try:
        p, params, = args[0], args[1:]
        self.commands[p](*params)
      except:
        self.commands[p]()
    except Exception as poop:
      self.out(f"error in: {i}\n {poop}")
        
  
  def output_log(self):
    for text in self.console_output:
      self.console_output_text.text += (text + "\n")
      self.console_output.pop(0)
    
    if len(str(self.console_output_text.text).splitlines()) >= 13:
      self.console_output_text.text = f"{self.console_output_text.text.splitlines()[len(self.console_output_text.text.splitlines()) - 2]}\n{self.console_output_text.text.splitlines()[len(self.console_output_text.text.splitlines()) - 1]}\n"