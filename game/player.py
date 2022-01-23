from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player:
  def __init__(self, name, color):
    self.name = name
    self.color = color
  
  def change_color(self, new_color):
    self.color = new_color
  
  def change_name(self, new_name):
    self.name = new_name
    self.name_label = Text(new_name,
                           parent=self,
                           y=1.5,
                           billboard=True,
                           world_scale=10,
                           x=-5)
  
  def spawn(self, x=0, y=0, z=0):
    self.controller = FirstPersonController(model="resources/player/person.obj",
                                            gravity=1,
                                            position=(x,y,z),
                                            scale=0.15,
                                            speed=5,
                                            jump_height=0,
                                            color=rgb(self.color[0],self.color[1],self.color[2]))
    self.name_label = Text(self.name,
                           parent=self.controller,
                           y=25,
                           billboard=True,
                           world_scale=10,
                           x=-2.5,
                           color=rgb(self.color[0],self.color[1],self.color[2]))
    
    camera.position = (0,10,0)
