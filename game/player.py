from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class player(FirstPersonController):
  def __init__(self, name="player", color="white",):
    self.name = name
  
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
    super().__init__(
      model="resources/player/person.obj",
      gravity=1,
      height=,
      position=(x,y,z),
      scale=0.15,
      speed=5,
      jump_height=0,
      collider="box",
    )
    