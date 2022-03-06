
import subprocess
import sys
import time
import asyncio
import json
program_info = open("data/program_info.json")
program_info = json.load(program_info)


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
from player import *
import buttons
from game import *




app = Ursina()

#levels
#import level0

#window setup
window.title = 'The Backrooms'
window.borderless = program_info["graphics"]["borderless"]
window.fullscreen = program_info["graphics"]["fullscreen"]
window.fps_counter.enabled = program_info["graphics"]["show fps"]
window.vsync = program_info["graphics"]["vsync"]

#texture setup
Texture.default_filtering = "mipmap"

#console setup
application.print_warnings = False



chunks = []



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

  print("done!")
  #time.sleep(0.5)
  
'''def delayed_chunkload():
    load_chunks()
    invoke(delayed_chunkload, delay = 1)

invoke(delayed_chunkload, delay = 0.1)'''

#main menu
singleplayer = Button(text="singleplayer", position=(0, 0.3), scale=(0.4, 0.2))
multiplayer = Button(text="multiplayer", position=(0, 0), scale=(0.4, 0.2))
options = Button(text="options", position=(0, -0.3), scale=(0.4, 0.2))
quithowto = Text("quit(shift + q)", position=(-0.078, -0.42))

def singleplayer_instance():
  global game_instance
  game_instance = Game()
  global player
  player = Player(program_info["player"]["name"], color=(program_info["player"]["color"][0], program_info["player"]["color"][1], program_info["player"]["color"][2]))
  singleplayer.disable()
  multiplayer.disable()
  options.disable()
  quithowto.disable()
  game_instance.add_player(player)
  player.spawn(12, -6, 0)
  player.set_immunity(True)
  lobby.players(game_instance)

def multiplayer_join_info():
  singleplayer.disable()
  multiplayer.disable()
  options.disable()
  quithowto.disable()
  server_ip = TextField(text="ip", position=(0, 0))
  server_port = TextField(text="port", position=(0, -0.2))
  
singleplayer.on_click = singleplayer_instance
multiplayer.on_click = multiplayer_join_info

import lobby


app.run()