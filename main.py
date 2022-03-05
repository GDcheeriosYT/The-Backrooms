
import subprocess
import sys
import time
import asyncio
import json


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome To The Backrooms Game")
#time.sleep(1.5)
print("Will now begin program setup")
#time.sleep(1.5)

#package requirements
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursinanetworking import *
import numpy
import webbrowser
from UrsinaLighting import *
import player as br_player
import buttons




app = Ursina()

#levels
#import level0

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
hum.volume = 0.1

chunks = []

program_info = open("data/program_info.json")
program_info = json.load(program_info)


def load_chunks():
  distance_mult = 2
  current_location = (player.controller.position[0] / distance_mult, player.controller.position[1] / distance_mult, player.controller.position[2] / distance_mult)
  current_location = Entity(position=current_location)
  #print(distance(chunks[0].structure, current_location))
  print("debug: loading chunks")
  if program_info["graphics"]["quality"] == "high":
    for chunk in chunks:
      if distance(chunk.structure, current_location) > program_info["graphics"]["view distance"]:
        chunk.structure.disable()
        chunk.light_object.disable()
        try:
          if distance(chunk.light, current_location) > program_info["graphics"]["view distance"] / 2:
            chunk.light.setIntensity(0)
            chunk.item.disable()
        except:
            pass
      else:
        chunk.structure.enable()
        chunk.light_object.enable()
        try:
          if distance(chunk.light, current_location) < program_info["graphics"]["view distance"] / 2:
            chunk.light.setIntensity(1)
            chunk.item.enable()
        except:
            pass
          
          
          
          
  else:
    for chunk in chunks:
      if distance(chunk.structure, current_location) > program_info["graphics"]["view distance"]:
        chunk.structure.disable()
      else:
        chunk.structure.enable()
        try:
          if distance(chunk.light_structure, current_location) < program_info["graphics"]["view distance"] / 2:
            chunk.light_structure.enable()
            chunk.item.enable()
        except:
            pass
      try:
        if distance(chunk.light_structure, current_location) > program_info["graphics"]["view distance"] / 2:
          chunk.light_structure.disable()
          chunk.item.disable()
      except:
          pass
      if distance(chunk.structure, current_location) > program_info["graphics"]["view distance"] / 4:
        chunk.collision_structure.disable()
      else:
        chunk.collision_structure.enable()








def map_generation(seed, min, max, load = False):
  global chunks
  '''
  generates a maze if load is False
  
  load : boolean
  '''
  
  global list_of_cords
  multiplier = 5
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
    while z <= max:
      while x <= max:
        cords = [x, z]
        percent = int((z /  diff) * 100)
        if percent < 0:
          percent = 0
        print(f"initializing cords: {cords} {percent}%")
        list_of_cords.append(cords)
        x += 1
      x = min
      z += 1
    print("done!")
    #time.sleep(0.5)
    for cord in list_of_cords:
      cords = (cord[0] * multiplier, cord[1] * multiplier) #converting into tuple
      print(f"map generation: {cords} {int((list_of_cords.index(cord) / len(list_of_cords)) * 100)}%")
      thing = level0.Chunk(cords[0], 0, cords[1])
      chunks.append(thing)
      thing.place()
      
    with open("data/level0_data.json", "w+") as SD:
      segment_data = json.dump(map_data, SD, sort_keys = False)
      
      
      
      
  else:
    with open("data/level0_data.json", "r") as SD:
      segment_data = json.load(SD)
    
    random.seed(segment_data["seed"])
    
    print(f"the map is {min} by {max}")
    diff = max - min
    z = min
    x = min
    while z <= max:
      while x <= max:
        cords = [x, z]
        percent = int((z /  diff) * 100)
        if percent < 0:
          percent = 0
        print(f"initializing cords: {cords} {percent}%")
        list_of_cords.append(cords)
        x += 1
      x = min
      z += 1
    print("done!")
    for cord in list_of_cords:
      cords = (cord[0] * multiplier, cord[1] * multiplier) #converting into tuple
      print(f"map generation: {cords} {int((list_of_cords.index(cord) / len(list_of_cords)) * 100)}%")
      thing = level0.Chunk(cords[0], 0, cords[1])
      chunks.append(thing)
      thing.place()
    
    print(chunks)

  hum.play()
  print("done!")
  #time.sleep(0.5)








'''def delayed_chunkload():
    load_chunks()
    invoke(delayed_chunkload, delay = 1)

invoke(delayed_chunkload, delay = 0.1)'''


import lobby
player = br_player.Player(program_info["player"]["name"], color=(0, 180, 0))
player.spawn(0, -7, 0)

app.run()