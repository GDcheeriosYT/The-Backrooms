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

app = Ursina()

#player
GDcheerios = br_player.player("GDcheerios", y=3)

#map
floor = Entity(model="cube",
               texture="resources/levels/level 0/carpet.png",
               scale=(100, 1, 100),
               collider="mesh", texture_scale=(3,3),
               position=(0,0,0),
               shaders=lit_with_shadows_shader)
wall = Entity(model="cube",
              texture="resources/levels/level 0/wall.png",
              scale=(10, 20, 5), texture_scale=(1, 2),
              collider="box",
              position=(5,0,5),
              shaders=lit_with_shadows_shader)
ceiling = Entity(model="cube",
                 texture="resources/levels/level 0/ceiling.png",
                 scale=(100, 1, 100),
                 texture_scale=(7,7),
                 collider="mesh",
                 position=(0,6,0),
                 shaders=lit_with_shadows_shader)


#entities
test = Entity(model="resources/player/person.obj", position=(-5,0,-5), scale=(0.15))
test.add_script(SmoothFollow(target=GDcheerios, offset=[0, 0, 0], speed=0.5, rotation_speed=1, rotation_offset=[1,0,1]))

name = Text(text=f"test",
            parent=test,
            y=26,
            x=-1,
            Billboard=True,
            world_scale=17)

#lights
light = Entity(model="cube", texture="resources/levels/level 0/light.png", position=(0,5.8,0), scale=(2.2,1.2,4))


#map construction
duplicate(wall, position=(10, 10, 10))

#window setup
window.title = 'The Backrooms'          # The window title
window.borderless = False               # Show a border
window.fullscreen = False                # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

app.run()