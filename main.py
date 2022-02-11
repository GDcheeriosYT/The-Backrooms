
import subprocess
import sys
import time
import asyncio
import json


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
import game.entity as br_entity
import game.player as br_player
import game.buttons
from game.levels.level0 import wall_placement_management as wpm

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

chunk = Entity(model="cube",
               scale=(15, 100, 15),
               color=rgb(0,0,0,a=0))

'''chunks = Entity(model="cube",
               scale=(15, 100, 15),
               color=rgb(0,0,0,a=255))'''

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
  def __init__(self, x=0, y=0, z=0, distance=5, scale=(5, 12, 5), is_blank=False):
    self.x = x
    self.y = y
    self.z = z
    self.type = type
    self.distance = distance
    self.scale = scale
    self.is_blank = is_blank
    
  def create_segment(self):
    
    def place(placement):
      print(placement)
      duplicate(wall,
                scale=self.scale,
                position=placement,
                parent=parent_wall_entity,
                specularMap=load_texture("resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(collider,
                scale=self.scale,
                position=placement)
    
    if self.is_blank == False:
      positions = wpm.manage_segment(segment=wpm.random_segment(), output=True, rotate=random.randint(0, 3))
    elif self.is_blank == True:
      positions = wpm.manage_segment(segment="blank.json", output=True)
    for position in positions:
      if position == "top left":
        placement = (self.x + self.distance, self.y, self.z - self.distance)
        place(placement)
      elif position == "top":
        placement = (self.x + self.distance, self.y, self.z)
        place(placement)
      elif position == "top right":
        placement = (self.x + self.distance, self.y, self.z + self.distance)
        place(placement)
      elif position == "left":
        placement = (self.x, self.y, self.z - self.distance)
        place(placement)
      elif position == "center":
        placement = (self.x, self.y, self.z)
        place(placement)
      elif position == "right":
        placement = (self.x, self.y, self.z + self.distance)
        place(placement)
      elif position == "bottom left":
        placement = (self.x - self.distance, self.y, self.z - self.distance)
        place(placement)
      elif position == "bottom":
        placement = (self.x - self.distance, self.y, self.z)
        place(placement)
      elif position == "bottom right":
        placement = (self.x - self.distance, self.y, self.z + self.distance)
        place(placement)
      else:
        pass
            
list_of_cords=[]

def map_generation(seed, min, max, load = False):
  '''
  generates a maze if load is False
  
  load : boolean
  '''
  
  global list_of_cords
  multiplier = 15
  light_intensity = [0, 1, 1, 1, 1, 1]
  if load == False:
    random.seed(seed)
    print(f"the map is {min} by {max}")
    diff = max - min
    z = min
    x = min
    map_data = {}
    map_data["min"] = min
    map_data["max"] = max
    map_data["seed"] = seed
    map_data["cords"] = {} 
    while z <= diff:
      map_data["cords"][z] = []
      while x <= diff:
        cords = [x, z]
        percent = int((z /  diff) * 100)
        if percent < 0:
          percent = 0
        print(f"initializing cords: {cords} {percent}%")
        list_of_cords.append(cords)
        map_data["cords"][z].append(x)
        x += 1
      x = min
      z += 1
    
    count = 0
    print("done!")
    time.sleep(0.5)
    for cord in list_of_cords:
      cords = (cord[0] * multiplier, cord[1] * multiplier) #converting into tuple
      print(f"map generation: {cords} {int((list_of_cords.index(cord) / len(list_of_cords)) * 100)}%")
      if cords[0] == 0 and cords[1] == 0:
        BackroomSegment(cords[0], 0, cords[1], is_blank=True).create_segment()
      else:
        BackroomSegment(cords[0], 0, cords[1]).create_segment()
      duplicate(light,
                position=(cords[0], 5.8, cords[1]),
                parent=parent_light_entity)
      LitPointLight(position=Vec3(cords[0],4,cords[1]), intensity=light_intensity[random.randint(0,5)], color=rgb(248, 252, 150))
      duplicate(chunk, position=(cords[0], 0, cords[1]))
      
      count+=1
      
    with open("data/level0_data.json", "w+") as SD:
      segment_data = json.dump(map_data, SD, sort_keys = False)
        
      
  else:
    with open("data/level0_data.json", "r") as SD:
      segment_data = json.load(SD)
    
    random.seed(segment_data["seed"])
    
    for z_cord in segment_data["cords"]:
      z_cord = int(z_cord)
      for x_cord in segment_data["cords"][str(z_cord)]:
        cords = [int(z_cord), x_cord]
        percent = int((int(z_cord) /  len(segment_data)) * 100)
        if percent < 0:
          percent = 0
        print(f"loading cords: {cords} {percent}%")
        list_of_cords.append(cords)
    for cord in list_of_cords:
      cords = (cord[0] * multiplier, cord[1] * multiplier) #converting into tuple
      print(f"map generation: {cords} {int((list_of_cords.index(cord) / len(list_of_cords)) * 100)}%")
      if cords[0] == 0 and cords[1] == 0:
        BackroomSegment(cords[0], 0, cords[1], is_blank=True).create_segment()
      else:
        BackroomSegment(cords[0], 0, cords[1]).create_segment()
      duplicate(light,
                position=(cords[0], 5.8, cords[1]),
                parent=parent_light_entity)
      LitPointLight(position=Vec3(cords[0],4,cords[1]), intensity=light_intensity[random.randint(0,5)], color=rgb(248, 252, 150))
      duplicate(chunk, position=(cords[0], 0, cords[1]))
    
  #perfmorance
  parent_wall_entity.combine()
  parent_light_entity.combine()

  parent_wall_entity.texture = "resources/levels/level 0/wall.png"

  hum.play()
  print("done!")
  time.sleep(0.5)
  
with open("data/program_info.json", "r+") as PI:
  try:
    player_info = json.load(PI)
    player = br_player.Player(player_info["name"], color=(player_info["color"][0], player_info["color"][1], player_info["color"][2]))
  except:
    with open("data/program_info.json", "a+") as PI:
      player_info = {}

      name = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat shall your name be?\n")
      player_info["name"] = name
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
      player_info["color"] = (R, G, B)
      print(player_info)
      json.dump(player_info, PI, indent=4)

      player = br_player.Player(name, color=(R,G,B))
      print("Thank You!")
    
    

singleplayer_or_multiplayer = input("S=M would you like singleplayer or multiplayer?\n")

if singleplayer_or_multiplayer == "s" or singleplayer_or_multiplayer == "S":
  load = input("Y=N would you like to generate a new map?\n")
  if load == "y" or load == "Y":
    seed = input("seed: ")
    map_generation(seed, int(input("min: ")), int(input("max: ")))
    player.spawn()
  else:
    with open("data/level0_data.json", "r") as SD:
      segment_data = json.load(SD)
      
    map_generation("", segment_data["min"], segment_data["max"], True)
    player.spawn()
  
  def update():
    if held_keys["f"]:
      chunk.color=rgb(0,0,0,a=50)
    else:
      chunk.color=rgb(0,0,0,a=0)
    if held_keys["shift"]:
      player.controller.speed = 10
    else:
      player.controller.speed = 5
    
else:
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

app.run()
