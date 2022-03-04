
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




with open("data/program_info.json", "r+") as PI:
  try:
    program_info = json.load(PI)
    player = br_player.Player(program_info["player"]["name"], color=(program_info["player"]["color"][0], program_info["player"]["color"][1], program_info["player"]["color"][2]))
  except:
    with open("data/program_info.json", "a+") as PI:
      program_info = {}
      player_info = {}
      graphics_info = {}

      name = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat shall your name be?\n")
      player_info["name"] = name
      #time.sleep(0.5)
      print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{name} Eh?")
      #time.sleep(1.5)
      print("Nice name.")
      #time.sleep(1.5)
      print(f"Well {name}, welcome to the backrooms.")
      #time.sleep(2)
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChoose your color using the following tool:")
      #time.sleep(3)
      webbrowser.open_new_tab('https://www.google.com/search?q=rgb+color+picker&rlz=1C1SQJL_enUS967US967&sxsrf=AOaemvLTpu0WEA2PhK4x_ya_FmXlE1mCCg%3A1642818658427&ei=YmzrYaybGYW2qtsP9rK16AQ&ved=0ahUKEwis1MK0qMT1AhUFm2oFHXZZDU0Q4dUDCA4&uact=5&oq=rgb+color+picker&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEEMyBAgAEEMyBQgAEIAEMgYIABAHEB4yBggAEAcQHjIFCAAQgAQyBQgAEIAEMgYIABAHEB4yBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFD9CVj9CWCFDWgCcAJ4AIABS4gBS5IBATGYAQCgAQHIAQrAAQE&sclient=gws-wiz')
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nUse the R G B on the right to enter the following:")
      #time.sleep(1.5)
      R = int(input("R: "))
      G = int(input("G: "))
      B = int(input("B: "))
      player_info["color"] = (R, G, B)
      program_info["player"] = player_info
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow choose graphics settings")
      quality = input("H: high graphics setting(NEEDS NASA SUPERCOMPUTER TO RUN WELL)\nL: low graphic settings(YOU SHOULD PROBABLY USE THIS)")
      if quality == "h" or quality == "H":
        graphics_info["quality"] = "high"
      else:
        graphics_info["quality"] = "low"
      
      view_distance = int(input("render distance(60-100 is a good range): "))
      graphics_info["view distance"] = view_distance
      program_info["graphics"] = graphics_info
      print(program_info)
      json.dump(program_info, PI, indent=4)

      player = br_player.Player(name, color=(R,G,B))
      print("Thank You!")




app = Ursina()

#levels
import level0

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









singleplayer_or_multiplayer = input("S=M would you like singleplayer or multiplayer?\n")

def delayed_chunkload():
    load_chunks()
    invoke(delayed_chunkload, delay = 1)

invoke(delayed_chunkload, delay = 0.1)


if singleplayer_or_multiplayer == "s" or singleplayer_or_multiplayer == "S":
  load = input("Y=N would you like to generate a new map?\n")
  if load == "y" or load == "Y":
    seed = input("seed: ")
    map_generation(seed, int(input("min: ")), int(input("max: ")), )
    player.spawn(-5, 0, -5)
  else:
    with open("data/level0_data.json", "r") as SD:
      segment_data = json.load(SD)
      
    map_generation("", segment_data["min"], segment_data["max"], True)
    player.spawn(-5, 0, -5)
  
  def update():
    if held_keys["shift"]:
      player.controller.speed = 10
    else:
      player.controller.speed = 5
    if held_keys["v"]:
      player.damage(1)
    elif held_keys["c"]:
      player.heal(1)
 
    
      
    
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