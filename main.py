import json
program_info = open("data/program_info.json")
program_info = json.load(program_info)


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome To The Backrooms Game")
#time.sleep(1.5)
print("Will now begin program setup")
#time.sleep(1.5)

#package requirements
from ursina import *
from ursinanetworking import *
from UrsinaLighting import *

app = Ursina()
from player import *
from game import *
from console import *

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
  
console = Console() #initialize console instance
console.disappear()

#main menu
singleplayer = Button(text="singleplayer", position=(-0.7, -0.1), scale=(0.4, 0.07))
multiplayer = Button(text="multiplayer", position=(-0.7, -0.2), scale=(0.4, 0.07))
options = Button(text="options", position=(-0.7, -0.3), scale=(0.4, 0.07))
leave = Button(text="quit", position=(-0.7, -0.4), scale=(0.4, 0.07))
wall = LitObject(model="cube", texture=Texture("resources/levels/level 0/logowall.png"), scale=(10,10,2), collider="box", position=(5,0,5), specularMap=load_texture("resources/levels/level 0/noreflect.png"), cubemapIntensity=0)
wall2 = LitObject(model="cube", texture=Texture("resources/levels/level 0/wall.png"), scale=(10,10,2), collider="box", position=(-10, 0, 5), specularMap=load_texture("resources/levels/level 0/noreflect.png"), cubemapIntensity=0)
wall3 = LitObject(model="cube", texture=Texture("resources/levels/level 0/wall.png"), scale=(2,10,10), collider="box", position=(-6, 0, 10), specularMap=load_texture("resources/levels/level 0/noreflect.png"), cubemapIntensity=0)
wall4 = LitObject(model="cube", texture=Texture("resources/levels/level 0/wall.png"), scale=(10,10,2), collider="box", position=(0, 0, 15), specularMap=load_texture("resources/levels/level 0/noreflect.png"), cubemapIntensity=0)
floor = LitObject(model="cube", texture=Texture("resources/levels/level 0/carpet.png"), scale=(1000, 1, 1000), collider="mesh", tiling=(250,250), position=(0,-3,0), specularMap=load_texture("resources/levels/level 0/noreflect.png"), cubemapIntensity=0)
ceiling = LitObject(model="cube", texture=Texture("resources/levels/level 0/ceiling.png"), scale=(1000, 1, 1000), tiling=(500,500), collider="mesh", position=(0,3,0), specularMap=load_texture("resources/levels/level 0/noreflect.png"), cubemapIntensity=0)
light = LitPointLight(position=Vec3(-5,0,-4), intensity=1, range=25, color=rgb(248, 252, 150))
player_preview = Player(program_info["player"]["name"], color=(program_info["player"]["color"][0], program_info["player"]["color"][1], program_info["player"]["color"][2]))
player_preview.spawn(-2, -2.45, 0, preview=True)
player_preview.set_immunity(True)
player_preview.name_label.x=1.5
player = Player(program_info["player"]["name"], color=(program_info["player"]["color"][0], program_info["player"]["color"][1], program_info["player"]["color"][2]))
def singleplayer_instance():
  global game_instance
  game_instance = Game()
  global player
  global player_preview
  singleplayer.disable()
  multiplayer.disable()
  options.disable()
  leave.disable()
  game_instance.add_player(player)
  player.spawn(12, -6, 0)
  player.set_immunity(True)
  wall.disable()
  wall2.disable()
  wall3.disable()
  wall4.disable()
  floor.disable()
  ceiling.disable()
  player_preview.controller.disable()
  del player_preview
  import lobby
  light.setPosition(Vec3(0,-0.6, 0))
  lobby.players(game_instance)

def multiplayer_menu():
  singleplayer.disable()
  multiplayer.disable()
  options.disable()
  leave.disable()
  server_ip = TextField(text="ip", position=(0, 0))
  server_port = TextField(text="port", position=(0, -0.2))

def options_menu():
  singleplayer.disable()
  multiplayer.disable()
  options.disable()
  leave.disable()
  fullscreen = Button(text="fullscreen", position=(-0.7, -0.1), scale=(0.4, 0.07))
  #borderless = Button(text="borderless", position=(-0.7, -0.2), scale=(0.4, 0.07))
  show_fps = Button(text="show fps", position=(-0.7, -0.2), scale=(0.4, 0.07))
  back = Button(text="back", position=(-0.7, -0.3), scale=(0.4, 0.07))
  def fullscreen_toggle():
    global program_info
    if program_info["graphics"]["fullscreen"] == True:
      program_info["graphics"]["fullscreen"] = False
      window.fullscreen = False
      json.dump(program_info, open("data/program_info.json", "w"), indent=4)
      program_info = json.load(open("data/program_info.json"))
    else:
      program_info["graphics"]["fullscreen"] = True
      window.fullscreen = True
      json.dump(program_info, open("data/program_info.json", "w"), indent=4)
      program_info = json.load(open("data/program_info.json"))
  
  def borderless_toggle():
    global program_info
    if program_info["graphics"]["borderless"] == True:
      program_info["graphics"]["borderless"] = False
      window.borderless = False
      json.dump(program_info, open("data/program_info.json", "w"), indent=4)
      program_info = json.load(open("data/program_info.json"))
    else:
      program_info["graphics"]["fullscreen"] = True
      window.borderless = True
      json.dump(program_info, open("data/program_info.json", "w"), indent=4)
      program_info = json.load(open("data/program_info.json"))
  
  def show_fps_toggle():
    global program_info
    if program_info["graphics"]["show fps"] == True:
      program_info["graphics"]["show fps"] = False
      window.fps_counter = False
      json.dump(program_info, open("data/program_info.json", "w"), indent=4)
      program_info = json.load(open("data/program_info.json"))
    else:
      program_info["graphics"]["show fps"] = True
      window.fps_counter = True
      json.dump(program_info, open("data/program_info.json", "w"), indent=4)
      program_info = json.load(open("data/program_info.json"))
  
  def back_thing():
    fullscreen.disable()
    #borderless.disable()
    show_fps.disable()
    singleplayer.enable()
    multiplayer.enable()
    options.enable()
    leave.enable()
    back.disable()
    
  
  fullscreen.on_click = fullscreen_toggle
  #borderless.on_click = borderless_toggle
  show_fps.on_click = show_fps_toggle
  back.on_click = back_thing

singleplayer.on_click = singleplayer_instance
multiplayer.on_click = multiplayer_menu
options.on_click = options_menu

leave.on_click = quit

def input(key):
  if key == "t":
    print("bruh")

def update():
  if held_keys["shift"]:
    player.controller.speed = 10
  else:
    player.controller.speed = 5

def input(key):
  if key == "c":
    if console.open == False:
      console.appear()
    else:
      console.disappear()
      
  if key == "enter" and console.open == True:
    console.console_output.append(console.input.text)
    print(console.input.text)
    console.input.text = ""
    console.output_log()

app.run()