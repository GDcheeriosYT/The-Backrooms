from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from UrsinaLighting import *

class Player:
  def __init__(self, name, color, health=100, hydration=100, hunger=100, sanity=100, items={}):
    self.name = name
    self.color = color
    self.health = health
    self.hydration = hydration
    self.hunger = hunger
    self.sanity = sanity
    self.items = {}
  
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
    
    self.health_bar = HealthBar(value=self.health,
                                position=(-0.9, -0.3))
    self.hydration_bar = HealthBar(value=self.hydration,
                                   bar_color=color.blue,
                                   position=(-0.9, -0.4))
    
    camera.position = (0,10,0)
  
  def damage(self, damage):
    self.health -= damage
    self.health_bar.value = self.health
    if self.health <= 0:
      self.controller.position = (5, 0, 5)
      self.health = 100
  
  def thirst(self, thirst):
    self.hydration -= thirst
    self.hydration_bar.value = self.hydration
    if self.hydration <= 0:
      self.damage(30)
      self.hydration += 2
  
  def craze(self, craze):
    self.sanity -= craze
    
  def heal(self, heal):
    self.health += heal
    self.health_bar.value = self.health
  
  def hydrate(self, liquid):
    self.hydration += liquid
    self.hydration_bar.value = self.hydration
  
  def uninsane(self, vbucks):
    self.sanity += vbucks