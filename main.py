import subprocess
import sys
import time
from turtle import position

def install(package):
    print(f"installing requirement {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#package requirements
try:
  from ursina import *
  from ursina.prefabs.first_person_controller import FirstPersonController
  from ursina.shaders import *
except:
  install("ursina")
  from ursina import *
  from ursina.prefabs.first_person_controller import FirstPersonController
  from ursina.shaders import *

try:
  from ursinanetworking import *
except:
  install("ursinanetworking")
  from ursinanetworking import *

try:
  import numpy
except:
  install("numpy")
  
from UrsinaLighting import *
from msilib.schema import Billboard
from game import entity as br_entity
from game import player as br_player
from game import buttons

random.seed(input("seed: "))

app = Ursina()


#player
player = br_player.player("GDcheerios")

#map
parent_wall_entity = Entity()
parent_light_entity = Entity()

floor = Entity(model="cube",
               texture="resources/levels/level 0/carpet.png",
               scale=(1000, 2, 1000),
               collider="mesh",
               texture_scale=(300,300),
               position=(0,0,0),
               shaders=basic_lighting_shader)
wall = Entity(model="cube",
              texture="resources/levels/level 0/wall.png",
              scale=(0,0,0),
              texture_scale=(0.5, 2),
              collider="box",
              position=(5,0,5),
              shaders=basic_lighting_shader)
ceiling = Entity(model="cube",
                 texture="resources/levels/level 0/ceiling.png",
                 scale=(1000, 1, 1000),
                 texture_scale=(500,500),
                 collider="mesh",
                 position=(0,6,0),
                 shaders=basic_lighting_shader)

#lights
light = Entity(model="cube", texture="resources/levels/level 0/light.png", color=color.white, position=(0,5.8,0), scale=(2.2,1.2,4))
#light_emit = LitPointLight(position=Vec3(0,5.5,0), intensity=1, range=30)

#map construction
class BackroomSegment():
  def __init__(self, x=0, y=0, z=0, type=["+", "T", "|"], distance=5, scale=(5, 20, 5)):
    self.x = x
    self.y = y
    self.z = z
    self.type = type
    self.distance = distance
    self.scale = scale
    try:
      self.type = type[random.randint(0,len(type))]
    except:
      self.type = type
  
  def create_segment(self):
    if self.type == "+":
      duplicate(wall,
                scale=self.scale,
                position=(self.x + self.distance, self.y, self.z + self.distance),
                parent=parent_wall_entity)
      duplicate(wall,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z - self.distance),
                parent=parent_wall_entity)
      duplicate(wall,
                scale=self.scale,
                position=(self.x + self.distance, self.y, self.z - self.distance),
                parent=parent_wall_entity)
      duplicate(wall,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z + self.distance),
                parent=parent_wall_entity)
      duplicate(light,
                position=(self.x, 5.8, self.z),
                parent=parent_light_entity)
    elif self.type == "T":
      rot = random.randint(1, 4)
      if rot == 1:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z + self.distance),
                  parent=parent_wall_entity)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
      elif rot == 2:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x - self.distance, self.y, self.z),
                  parent=parent_wall_entity)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
      elif rot == 3:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z - self.distance),
                  parent=parent_wall_entity)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
      elif rot == 4:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity)
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x + self.distance, self.y, self.z),
                  parent=parent_wall_entity)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
      elif self.type == "|":
        rot = random.randint(1,2)
        if rot == 1:
          duplicate(wall,
                    scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                    position=(self.x, self.y, self.z - self.distance),
                    parent=parent_wall_entity)
          duplicate(wall,
                    scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                    position=(self.x, self.y, self.z + self.distance),
                    parent=parent_wall_entity)
        elif rot == 2:
          duplicate(wall,
                    scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                    position=(self.x - self.distance, self.y, self.z),
                    parent=parent_wall_entity)
          duplicate(wall,
                    scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                    position=(self.x + self.distance, self.y, self.z),
                    parent=parent_wall_entity)

def map_generation():
  list_of_cords=[]
  min = -50
  max = 50
  multiplier = 5
  while len(list_of_cords) < 500:
    cords = (random.randint(random.randint(min, 3), random.randint(3, max))*multiplier, random.randint(random.randint(min, 0), random.randint(0, max)*multiplier))
    print(cords)
    if cords not in list_of_cords:
      list_of_cords.append(cords)
      BackroomSegment(cords[0], 0, cords[1]).create_segment()
  
        
def update():
  if held_keys["shift"]:
    player.speed = 10
  else:
    player.speed = 5
  
#window setup
window.title = 'The Backrooms'          # The window title
window.borderless = False               # Show a border
window.fullscreen = False                # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter
window.vsync = False

player.spawn()

app.run()