import subprocess
import sys
import time
import asyncio
import random
from ursina import *

def install(package):
    print(f"installing requirement {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
  from ursinanetworking import *
except:
  install("ursinanetworking")
  from ursinanetworking import *

print("starting a server...")
Server = UrsinaNetworkingServer("localhost", 6990)

#map
floor = Entity(model="cube",
               texture="resources/levels/level 0/carpet.png",
               scale=(6000, 0, 6000),
               collider="mesh",
               texture_scale=(5500,5500),
               position=(0,0,0),
               shaders=lit_with_shadows_shader)
wall = Entity(model="cube",
              texture="resources/levels/level 0/wall.png",
              scale=(0,0,0),
              texture_scale=(1, 2),
              collider="box",
              position=(5,0,5),
              shaders=lit_with_shadows_shader)
ceiling = Entity(model="cube",
                 texture="resources/levels/level 0/ceiling.png",
                 scale=(6000, 1, 6000),
                 texture_scale=(3000,3000),
                 collider="mesh",
                 color=color.black,
                 position=(0,6,0),
                 shaders=lit_with_shadows_shader)


#entities
test_player = Entity(model="resources/player/person.obj", position=(-5,0,-5), scale=(0.15))
test_player.add_script(SmoothFollow(target=player, offset=[0, 0, 0], speed=0.5, rotation_speed=1, rotation_offset=[1,0,1]))

name = Text(text="test player",
            parent=test_player,
            y=25,
            x=-6,
            color=color.white,
            billboard=True,
            world_scale=17)

#lights
light = Entity(model="cube", texture="resources/levels/level 0/light.png", position=(0,5.8,0), scale=(2.2,1.2,4))

#map construction
class BackroomSegment():
  def __init__(self, x=0, y=0, z=0, type="+"):
    self.x = x
    self.y = y
    self.z = z
    self.type = type
  
  def create_segment(self):
    if self.type == "+":
      duplicate(scale=(10, 20, 5),
                position=(self.x + 10, self.y, self.x + 10))

while True:
    Server.process_net_events()