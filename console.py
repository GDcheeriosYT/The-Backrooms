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
  def spawn(self, type=None, type2=None, coordinates=None):
    print(type, type2, coordinates)
    if coordinates != None:
      coordinates = eval(coordinates)
      coordinates = (coordinates[0] + self.coordinates[0], coordinates[1] + self.coordinates[1], coordinates[2] + self.coordinates[2])
    else:
      coordinates = self.coordinates
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
    elif str(type) == "bot":
      object = Player.spawn(x=coordinates[0], y=coordinates[1], z=coordinates[2], preview=True, name=type2).set_immunity(True)
      self.objects.append(object)
    else:
      self.out(f"tf you want me to do with {type}, {type2}, & {coordinates}")
  
  
  
  
  def clear(self):
    for object in self.objects:
      object.delete()
    
    self.objects = []
  
  
  
  
  def list_objects(self):
    out_string = ""
    for object in self.objects:
      out_string += f"{object.get_type()}\n"
      
    self.out(out_string)
  
  def generate(self, type=None, type2=None, coordinates=None, size=20, placements=10):
    print(type, type2, coordinates, size, placements)
    if coordinates is not None:
      coordinates = eval(coordinates)
      coordinates = (coordinates[0] + self.coordinates[0], coordinates[1] + self.coordinates[1], coordinates[2] + self.coordinates[2])
    else:
      coordinates = self.coordinates
    if str(type) == "0":
      if str(type2) == "normal":
        NormalChunk(coordinates[0], coordinates[1], coordinates[2], int(size)).place()
      elif str(type2) == "irregular":
        IrregularChunk(coordinates[0], coordinates[1], coordinates[2], int(size), int(placements)).place()
      else:
        self.out("YOU SUCK")
    else:
      self.out(f"attempted: {type, type2, coordinates, size, placements}, but it didn't seem to work")
  
  
  
  
  def command_help(self):
    self.out('''
help, for help
spawn type type2 (*args), used for spawning items, entities, and test players
clear, clears all things that have been spawned by the console
list, lists all the objects spawned
generate level part (coordinates) size placements, generate different sections of levels
            ''')
  
  def handle(self, i):
    self.commands = {
      'spawn':self.spawn,
      'clear':self.clear,
      'list':self.list_objects,
      'generate':self.generate,
      'help':self.command_help
    }
    
    
    args = i.split()
    try:
      p, params, = args[0], args[1:]
      self.commands[p](*params)
    except Exception as poop:
      self.out(f"error in: {i}\n {poop}")
        
  
  def output_log(self):
    for text in self.console_output:
      self.console_output_text.text += (text + "\n")
      self.console_output.pop(0)
    
    if len(str(self.console_output_text.text).splitlines()) >= 13:
      self.console_output_text.text = f"{self.console_output_text.text.splitlines()[len(self.console_output_text.text.splitlines()) - 2]}\n{self.console_output_text.text.splitlines()[len(self.console_output_text.text.splitlines()) - 1]}\n"