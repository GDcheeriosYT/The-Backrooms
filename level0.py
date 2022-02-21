from ursina import *
from UrsinaLighting import *

#initial variable stuff
wall_side_scale = 0.5
wall_spacing = 5

#initial map stuff
door = Entity()
walls = Entity()
collider = Entity(collider="box")
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

def place_door(x=0, y=0, z=0, sideways=False):
  change = 2
  if sideways == False:
    duplicate(wall, position=(x-change, y, z), scale=(1.5, 20, wall_side_scale), parent=door)#left side of door
    duplicate(wall, position=(x+change, y, z), scale=(1.5, 20, wall_side_scale), parent=door)#right side of door
    duplicate(wall, position=(x, y+5, z), scale=(5, 2, wall_side_scale), parent=door)#top side of door
    duplicate(collider, position=(x-change, y, z), scale=(1,20,wall_side_scale))
    duplicate(collider, position=(x+change, y, z), scale=(1,20,wall_side_scale))
  else:
    duplicate(wall, position=(x, y, z-change), scale=(wall_side_scale, 20, 1.5), parent=door)#left side of door
    duplicate(wall, position=(x, y, z+change), scale=(wall_side_scale, 20, 1.5), parent=door)#right side of door
    duplicate(wall, position=(x, y+5, z), scale=(wall_side_scale, 2, 5), parent=door)#top side of door
    duplicate(collider, position=(x, y, z-change), scale=(wall_side_scale,20,1))
    duplicate(collider, position=(x, y, z+change), scale=(wall_side_scale,20,1))




def place_wall(x=0, y=0, z=0, sideways=False):
  if sideways == False:
    duplicate(wall, position=(x, y, z), scale=(wall_spacing, 20, wall_side_scale), parent=walls)
    duplicate(collider, position=(x, y, z), scale=(wall_spacing,20,wall_side_scale))
  else:
    duplicate(wall, position=(x, y, z), scale=(wall_side_scale, 20, wall_spacing), parent=walls)
    duplicate(collider, position=(x, y, z), scale=(wall_side_scale,20,wall_spacing))



#class stuff
class Chunk():
  def __init__(self, x=0, y=0, z=0, walls=1):
    self.x = x
    self.y = y
    self.z = z
    self.walls = walls
    
  def place(self):
    for wall in range(walls):
      None