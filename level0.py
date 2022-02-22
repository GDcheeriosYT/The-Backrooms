from turtle import position
from ursina import *
from UrsinaLighting import *
import items

#initial variable stuff
wall_side_scale = 0.5
wall_spacing = 5

#initial map stuff
wall = LitObject(model="cube",
              texture=Texture("resources/levels/level 0/wall.png"),
              scale=(0,0,0),
              collider="box",
              position=(5,0,5),
              specularMap=load_texture("resources/levels/level 0/noreflect.png"),
              cubemapIntensity=0)
floor = LitObject(model="cube",
               texture=Texture("resources/levels/level 0/carpet.png"),
               scale=(1000, 1, 1000),
               collider="mesh",
               tiling=(250,250),
               position=(0,0,0),
               specularMap=load_texture("resources/levels/level 0/noreflect.png"),
               cubemapIntensity=0)
ceiling = LitObject(model="cube",
                 texture=Texture("resources/levels/level 0/ceiling.png"),
                 scale=(1000, 1, 1000),
                 tiling=(500,500),
                 collider="mesh",
                 position=(0,6,0),
                 specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                 cubemapIntensity=0)
parent_light_entity = Entity()
light = Entity(model="cube", color=color.white, position=(100,5.8,100), scale=(2.2,1.2,4), specularMap=load_texture("resources/levels/level 0/noreflect.png"))




#class stuff
class Chunk():
  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z
    self.structure = Entity(position=(x, y, z))
  
  def place_door(self, x=0, y=0, z=0, sideways=False):
    if sideways == False:
      duplicate(wall, position=(x-wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.structure)#left side of door
      duplicate(wall, position=(x+wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.structure)#right side of door
      duplicate(wall, position=(x, y+5, z), scale=(wall_spacing * 2, 2, wall_side_scale), parent=self.structure)#top side of door
      #duplicate(collider, position=(x-wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5,8,wall_side_scale))  
      #duplicate(collider, position=(x+wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5,8,wall_side_scale))
    else:
      duplicate(wall, position=(x, y, z-wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.structure)#left side of door
      duplicate(wall, position=(x, y, z+wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.structure)#right side of door
      duplicate(wall, position=(x, y+5, z), scale=(wall_side_scale, 2, wall_spacing * 2), parent=self.structure)#top side of door
      #duplicate(collider, position=(x, y, z-wall_spacing / 1.5), scale=(wall_side_scale,20,wall_spacing / 1.5))
      #duplicate(collider, position=(x, y, z+wall_spacing / 1.5), scale=(wall_side_scale,20,wall_spacing / 1.5))

  #LitPointLight(intensity=100, color=rgb(248, 252, 150))
      



  def place_wall(self, x=0, y=0, z=0, sideways=False):
    if sideways == False:
      duplicate(wall, position=(x, y, z), scale=(wall_spacing * 2, 20, wall_side_scale), parent=self.structure)
      #duplicate(collider, position=(x, y, z), scale=(wall_spacing * 2, 20,wall_side_scale))
    else:
      duplicate(wall, position=(x, y, z), scale=(wall_side_scale, 20, wall_spacing * 2), parent=self.structure)
      #duplicate(collider, position=(x, y, z), scale=(wall_side_scale, 20,wall_spacing * 2))
    
  def place(self):
    spawn_item_chance = random.randint(0, 100)
    if spawn_item_chance <= 2:
      items.AlmondWater(self.x + wall_spacing, self.y, self.z + wall_spacing).spawn(self.structure)
    light_level = random.randint(0, 1)
    if light_level == 0:
      duplicate(light,
                position=(self.x - wall_spacing, 5.8, self.z - wall_spacing),
                texture=Texture("resources/levels/level 0/lightoff.png"),
                parent=self.structure)
    else:
      duplicate(light,
                position=(self.x - wall_spacing, 5.8, self.z - wall_spacing),
                texture=Texture("resources/levels/level 0/light.png"),
                parent=self.structure)
      LitPointLight(position=Vec3(self.x * 2- wall_spacing, 4, self.z * 2 - wall_spacing), intensity=light_level, color=rgb(248, 252, 150))
      
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