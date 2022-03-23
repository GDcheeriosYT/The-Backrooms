from turtle import position
from ursina import *

class AlmondWater():
  def __init__(self, x=0, y=0, z=0, hydration=40):
    self.x = x
    self.y = y
    self.z = z
    self.hydration = hydration
  
  def spawn(self, chunk_entity=Entity()):
    self.object = Entity(model="resources/items/almond water/bottle.obj",
                         scale=(0.02,0.02,0.02),
                         position=(self.x, self.y + 0.6, self.z),
                         parent=chunk_entity)
  
  def get_type(self):
    return("almond water")

  def delete(self):
    self.object.disable()