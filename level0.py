from turtle import position
from ursina import *
from UrsinaLighting import *
import items
from ursina.shaders import *

#initial variable stuff
wall_side_scale = 0.5
wall_spacing = 5

#initial map stuff
lights_on = Entity()
lights_off = Entity()
wall = Entity(model="cube",
              texture=Texture("resources/levels/level 0/wall.png"),
              scale=(0,0,0),
              collider="mesh",
              position=(5,0,5),
              cubemapIntensity=0,
              shader=basic_lighting_shader,)
floor = Entity(model="cube",
               texture=Texture("resources/levels/level 0/carpet.png"),
               scale=(1000, 1, 1000),
               texture_scale=(1000,1000),
               collider="mesh",
               position=(0,0,0))
               #shader=basic_lighting_shader
ceiling = Entity(model="cube",
                 texture=Texture("resources/levels/level 0/ceiling.png"),
                 scale=(1000, 1, 1000),
                 texture_scale=(1000,1000),
                 collider="mesh",
                 position=(0,6,0))
                 #shader=basic_lighting_shader
collider = Entity(collider="box")
parent_light_entity = Entity()
light = Entity(model="cube", color=color.white, position=(100,5.8,100), scale=(2.2,1.2,4), specularMap=load_texture("resources/levels/level 0/noreflect.png"))




#class stuff
class Chunk():
  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z
    self.structure = Entity(position=(x, y, z))
    self.random_value = random.randint(0, 100)
    if self.random_value < 2:
      self.has_item = True
    else:
      self.has_item = False
  
  def place_door(self, x=0, y=0, z=0, sideways=False):
    if sideways == False:
      duplicate(wall, position=(x-wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.structure)#left side of door
      duplicate(wall, position=(x+wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.structure)#right side of door
      duplicate(wall, position=(x, y+5, z), scale=(wall_spacing * 2, 2, wall_side_scale), parent=self.structure)#top side of door
      duplicate(collider, position=(x-wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5,8,wall_side_scale), parent=self.structure)  
      duplicate(collider, position=(x+wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5,8,wall_side_scale), parent=self.structure)
    else:
      duplicate(wall, position=(x, y, z-wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.structure)#left side of door
      duplicate(wall, position=(x, y, z+wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.structure)#right side of door
      duplicate(wall, position=(x, y+5, z), scale=(wall_side_scale, 2, wall_spacing * 2), parent=self.structure)#top side of door
      duplicate(collider, position=(x, y, z-wall_spacing / 1.5), scale=(wall_side_scale,20,wall_spacing / 1.5), parent=self.structure)
      duplicate(collider, position=(x, y, z+wall_spacing / 1.5), scale=(wall_side_scale,20,wall_spacing / 1.5), parent=self.structure)

      



  def place_wall(self, x=0, y=0, z=0, sideways=False):
    if sideways == False:
      duplicate(wall, position=(x, y, z), scale=(wall_spacing * 2, 20, wall_side_scale), parent=self.structure)
      duplicate(collider, position=(x, y, z), scale=(wall_spacing * 2, 20,wall_side_scale), parent=self.structure)
    else:
      duplicate(wall, position=(x, y, z), scale=(wall_side_scale, 20, wall_spacing * 2), parent=self.structure)
      duplicate(collider, position=(x, y, z), scale=(wall_side_scale, 20,wall_spacing * 2), parent=self.structure)
    
  def place(self):
    if self.has_item == True:
      items.AlmondWater(self.x + wall_spacing, self.y, self.z + wall_spacing).spawn()
        
    light_level = random.randint(0, 1)
    if light_level == 0:
      duplicate(light,
                position=(self.x * 2 - wall_spacing, 5.8, self.z * 2 - wall_spacing),
                texture=Texture("resources/levels/level 0/lightoff.png"),
                parent=lights_off)
    else:
      duplicate(light,
                position=(self.x * 2 - wall_spacing, 5.8, self.z * 2 - wall_spacing),
                texture=Texture("resources/levels/level 0/light.png"),
                parent=lights_on)
      self.light = PointLight(x=self.x * 2 - wall_spacing, y=5.8, z=self.z * 2 - wall_spacing, parent=self.structure)
      
    left_rand = random.randint(0, 2)
    if left_rand == 1:
      second_chance = random.randint(0, 1)
      if second_chance == 1:
        self.place_door(self.x, self.y, self.z - wall_spacing, True)
      else: 
        self.place_wall(self.x, self.y, self.z - wall_spacing, True)
    elif left_rand == 2:
      self.place_wall(self.x, self.y, self.z - wall_spacing, True)
    else:
      pass
    
    top_rand = random.randint(0, 2)
    if top_rand == 1:
      second_chance = random.randint(0, 1)
      if second_chance == 1:
        self.place_door(self.x + wall_spacing, self.y, self.z, False)
      else:
        self.place_wall(self.x + wall_spacing, self.y, self.z, False)
    elif top_rand == 2:
      self.place_wall(self.x + wall_spacing, self.y, self.z, False)
    else:
      pass
    
    #performance
    self.structure.combine()
    self.structure.texture = "resources/levels/level 0/wall.png"