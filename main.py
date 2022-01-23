
import subprocess
import sys
import time
import asyncio



print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome To The Backrooms Game")
time.sleep(1.5)
print("Will now begin program setup")
time.sleep(1.5)

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
  import numpy
  
try:
  import webbrowser
except:
  install("webbrowser")
  import webbrowser

from UrsinaLighting import *
from game import entity as br_entity
from game import player as br_player
from game import buttons

app = Ursina()

#map
parent_wall_entity = Entity()
parent_light_entity = Entity()

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

hum = Audio("resources\levels\level 0\Backrooms sound.mp3", loop=True)
hum.volume = 0.3

floor = LitObject(model="cube",
               texture=Texture("resources/levels/level 0/carpet.png"),
               scale=(1000, 1, 1000),
               collider="mesh",
               tiling=(250,250),
               position=(0,0,0),
               specularMap=load_texture("resources/levels/level 0/noreflect.png"),
               cubemapIntensity=0)
wall = LitObject(model="cube",
              texture=Texture("resources/levels/level 0/wall.png"),
              scale=(0,0,0),
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
collider = Entity(collider="box", scale=(0,0,0), position=(349024859,0,0))

#lights
light = Entity(model="cube", texture=Texture("resources/levels/level 0/light.png"), color=color.white, position=(100,5.8,100), scale=(2.2,1.2,4), specularMap=load_texture("resources/levels/level 0/noreflect.png"))
LitPointLight(position=Vec3(0,0,0), intensity=1, color=rgb(248, 252, 150))

#map construction
class BackroomSegment():
  def __init__(self, x=0, y=0, z=0, type=["+", "T", "|"], distance=5, scale=(5, 12, 5)):
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
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(collider,
                scale=self.scale,
                position=(self.x + self.distance, self.y, self.z + self.distance))
      duplicate(wall,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z - self.distance),
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(collider,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z - self.distance))
      duplicate(wall,
                scale=self.scale,
                position=(self.x + self.distance, self.y, self.z - self.distance),
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(collider,
                scale=self.scale,
                position=(self.x + self.distance, self.y, self.z - self.distance))
      duplicate(wall,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z + self.distance),
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(collider,
                scale=self.scale,
                position=(self.x - self.distance, self.y, self.z + self.distance))
    elif self.type == "T":
      rot = random.randint(1, 4)
      if rot == 1:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance))
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance))
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z + self.distance),)
      elif rot == 2:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance))
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z - self.distance))
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x - self.distance, self.y, self.z),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x - self.distance, self.y, self.z))
      elif rot == 3:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x + self.distance, self.y, self.z + self.distance))
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance))
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z - self.distance))
      elif rot == 4:
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z + self.distance))
        duplicate(wall,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=self.scale,
                  position=(self.x - self.distance, self.y, self.z - self.distance))
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x + self.distance, self.y, self.z),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x + self.distance, self.y, self.z))
    elif self.type == "|":
      rot = random.randint(1,2)
      if rot == 1:
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z - self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z - self.distance))
        duplicate(wall,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z + self.distance),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0] * 3, self.scale[1], self.scale[2]),
                  position=(self.x, self.y, self.z + self.distance))
      elif rot == 2:
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x - self.distance, self.y, self.z),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x - self.distance, self.y, self.z))
        duplicate(wall,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x + self.distance, self.y, self.z),
                  parent=parent_wall_entity,
                  specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                  cubemapIntensity=0)
        duplicate(collider,
                  scale=(self.scale[0], self.scale[1], self.scale[2] * 3),
                  position=(self.x + self.distance, self.y, self.z))
        
list_of_cords=[]

def map_generation():
  min = -2
  max = 2
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
    cords = (cord[0] * multiplier, cord[1] * multiplier) #converting into tuple
    print(f"map generation: {cords} {int((list_of_cords.index(cord) / len(list_of_cords)) * 100)}%")
    BackroomSegment(cords[0], 0, cords[1]).create_segment()
    duplicate(light,
              position=(cords[0], 5.8, cords[1]),
              parent=parent_light_entity)
    LitPointLight(position=Vec3(cords[0],4,cords[1]), intensity=1, color=rgb(248, 252, 150))
      
    count+=1
  
  #perfmorance
  parent_wall_entity.combine()
  parent_light_entity.combine()

  parent_wall_entity.texture = "resources/levels/level 0/wall.png"

  hum.play()
  print("done!")
  time.sleep(0.5)

name = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat shall your name be?\n")
time.sleep(0.5)
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{name} Eh?")
time.sleep(1.5)
print("Nice name.")
time.sleep(1.5)
print(f"Well {name}, welcome to the backrooms.")
time.sleep(2)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChoose your color using the following tool:")
time.sleep(3)
webbrowser.open_new_tab('https://www.google.com/search?q=rgb+color+picker&rlz=1C1SQJL_enUS967US967&sxsrf=AOaemvLTpu0WEA2PhK4x_ya_FmXlE1mCCg%3A1642818658427&ei=YmzrYaybGYW2qtsP9rK16AQ&ved=0ahUKEwis1MK0qMT1AhUFm2oFHXZZDU0Q4dUDCA4&uact=5&oq=rgb+color+picker&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEEMyBAgAEEMyBQgAEIAEMgYIABAHEB4yBggAEAcQHjIFCAAQgAQyBQgAEIAEMgYIABAHEB4yBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFD9CVj9CWCFDWgCcAJ4AIABS4gBS5IBATGYAQCgAQHIAQrAAQE&sclient=gws-wiz')
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nUse the R G B on the right to enter the following:")
time.sleep(1.5)
R = int(input("R: "))
G = int(input("G: "))
B = int(input("B: "))

player = br_player.Player(name, color=(R,G,B))

print("Thank You!")
ip = input("Now just enter server ip: ")

Client = UrsinaNetworkingClient(ip, 6990)

@Client.event
def onConnectionEtablished():
    print(f"{name}, {ip} welcomes you!")

@Client.event
def HelloFromServer(content):
    print(f"{content}")

@Client.event
def map_requested(seed):
  map_generation(seed)




#entities
#Lighter = LitObject(model="sphere", color=color.white, position=(4, 3, 0)).add_script(SmoothFollow(target=player, offset=[0, 1, 0], speed=1))
#Lighter_light = LitPointLight(range=5, intensity=10, position=Vec3(4, 3, 0))


Client.send_message("request_map")

print("object count:", len(scene.entities))

'''def update():
  if held_keys["shift"]:
    player.controller.speed = 10
  else:
    player.controller.speed = 5'''

app.run()