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
except:
  install("ursina")
  from ursina import *
  from ursina.prefabs.first_person_controller import FirstPersonController

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

#window setup
window.title = 'The Backrooms'          # The window title
window.borderless = False               # Show a border
window.fullscreen = False                # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter
window.vsync = False

#texture setup
Texture.default_filtering = "mipmap"

#console setup
application.print_warnings = False


#player
player = br_player.player("GDcheerios")

#entities
Lighter = LitObject(model="sphere", color=color.white, position=(4, 3, 0)).add_script(SmoothFollow(target=player, offset=[0, 1, 0], speed=1))
Lighter_light = LitPointLight(range=5, intensity=10, position=Vec3(4, 3, 0))

#map
parent_wall_entity = Entity()
parent_light_entity = Entity()

hum = Audio("resources\levels\level 0\Backrooms sound.mp3", loop=True)

floor = LitObject(model="cube",
               texture=Texture("resources/levels/level 0/carpet.png"),
               scale=(1000, 2, 1000),
               collider="mesh",
               tiling=(300,300),
               position=(0,0,0),
               specularMap=load_texture("resources/levels/level 0/noreflect.png"),
               cubemapIntensity=0)
wall = LitObject(model="cube",
              texture=Texture("resources/levels/level 0/wall.png"),
              scale=(0,0,0),
              tiling=(0.5, 2),
              collider="box",
              position=(5,0,5),
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

#lights
light = LitObject(model="cube", texture=Texture("resources/levels/level 0/light.png"), color=color.white, position=(0,5.8,0), scale=(2.2,1.2,4), specularMap=load_texture("resources/levels/level 0/noreflect.png"))
LitPointLight(position=Vec3(0,4,0), intensity=2)

#map construction
class BackroomSegment():
  def __init__(self, x=0, y=0, z=0, type=["+", "T", "|"], distance=5, scale=(5, 20, 5), light_intensity=2, light_height=4):
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
    self.light_intensity = light_intensity
    self.light_height = light_height
    
  def create_segment(self):
    if self.type == "+":
      duplicate(wall,
                scale=self.scale,
                position=(self.x + self.distance, self.y, self.z + self.distance),
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(wall,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z - self.distance),
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(wall,
                scale=self.scale,
                position=(self.x + self.distance, self.y, self.z - self.distance),
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(wall,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z + self.distance),
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(light,
                position=(self.x, 5.8, self.z),
                parent=parent_light_entity)
      LitPointLight(position=Vec3(self.x,self.light_height,self.z), intensity=self.light_intensity)
    elif self.type == "T":
      rot = random.randint(1, 4)
      if rot == 1:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
        LitPointLight(position=Vec3(self.x,self.light_height,self.z), intensity=self.light_intensity)
      elif rot == 2:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x - self.distance, self.y, self.z),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
        LitPointLight(position=Vec3(self.x,self.light_height,self.z), intensity=self.light_intensity)
      elif rot == 3:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
        LitPointLight(position=Vec3(self.x,self.light_height,self.z), intensity=self.light_intensity)
      elif rot == 4:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x + self.distance, self.y, self.z),
                  parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
        duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
        LitPointLight(position=Vec3(self.x,self.light_height,self.z), intensity=self.light_intensity)
      elif self.type == "|":
        rot = random.randint(1,2)
        if rot == 1:
          duplicate(wall,
                    scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                    position=(self.x, self.y, self.z - self.distance),
                    parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
          duplicate(wall,
                    scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                    position=(self.x, self.y, self.z + self.distance),
                    parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
          duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
          LitPointLight(position=Vec3(self.x,self.light_height,self.z), intensity=self.light_intensity)
        elif rot == 2:
          duplicate(wall,
                    scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                    position=(self.x - self.distance, self.y, self.z),
                    parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
          duplicate(wall,
                    scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                    position=(self.x + self.distance, self.y, self.z),
                    parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
          duplicate(light,
                  position=(self.x, 5.8, self.z),
                  parent=parent_light_entity)
          LitPointLight(position=Vec3(self.x,self.light_height,self.z), intensity=self.light_intensity)

list_of_cords=[]

def map_generation():
  min = 5
  max = 20
  print(f"the map is {min} by {max}")
  diff = max - min
  multiplier = 15
  z = min
  x = min
  while z <= diff:
    while x <= diff:
      cords = [x, z]
      percent = int((z /  diff) * 100)
      if percent < 0:
        percent = 0
      print(f"initializing cords: {cords} {percent}%")
      global list_of_cords
      list_of_cords.append(cords)
      x += 1
    x = min
    z += 1
  
  count = 0
  print("done!")
  time.sleep(0.5)
  for cord in list_of_cords:
    if cord[0] <= -abs(diff) or cord[0] >= diff:
      cord[0] = cord[0]
      if cord[1] <= -abs(diff) or cord[1] >= diff:
        cord[1] = cord[1]
      elif cord[1] == 0:
        cord[1] = None
      else:
        cord[1] = cord[1] * multiplier
    elif cord[0] == 0:
      cord[0] = None
      if cord[1] <= -abs(diff) or cord[1] >= diff:
        cord[1] = cord[1]
      elif cord[1] == 0:
        cord[1] = None
      else:
        cord[1] = cord[1] * multiplier
    else:
      cord[0] = cord[0] * multiplier
      if cord[1] <= -abs(diff) or cord[1] >= diff:
        cord[1] = cord[1]
      elif cord[1] == 0:
        cord[1] = None
      else:
        cord[1] = cord[1] * multiplier
    
    if cord[0] == None or cord[1] == None:
      print(f"map generation: -{cords} {int((list_of_cords.index(cord) / len(list_of_cords)) * 100)}% --- SKIPPED ENTITTY CREATION")
    else:
      cords = (cord[0], cord[1]) #converting into tuple
      print(f"map generation: {cords} {int((list_of_cords.index(cord) / len(list_of_cords)) * 100)}%")
      BackroomSegment(cords[0], 0, cords[1]).create_segment()
      
      
    count+=1
  
  print("done!")
  time.sleep(0.5)

map_generation()
        
player.spawn(0, 2, 0)

def update():
  if held_keys["shift"]:
    player.speed = 10
  else:
    player.speed = 5

app.run()