from turtle import position
from ursina import *
from UrsinaLighting import *
from ursina.shaders import *
import items
import json

#initial variable stuff
wall_side_scale = 0.5
wall_spacing = 5
with open("data/program_info.json", "r") as f:
  program_info = json.load(f)
chunk_types=[]
list_of_cords={}

hum = Audio("resources\levels\level 0\Backrooms sound.mp3", loop=True)
hum.volume = 0.1
def play_audio():
  hum.play()

def pause_audio():
  hum.pause()


#initial map stuff
wall = LitObject(model="cube",
              texture=Texture("resources/levels/level 0/wall.png"),
              scale=(0,0,0),
              collider="box",
              position=(5,0,5),
              specularMap=load_texture("resources/levels/level 0/noreflect.png"),
              cubemapIntensity=0)
floor = LitObject(model="cube",
               texture=Texture("resources/levels/level 0/carpet.png"),
               scale=(1000, 1, 1000),
               collider="mesh",
               tiling=(250,250),
               position=(0,0,0),
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
floor.disable()
ceiling.disable()
collider = Entity(collider="box")
light = Entity(model="cube", color=color.white, position=(100,-1,100), scale=(2.2,1.2,4))


#class stuff
class level:
  def __init__(self, seed, chunks=5):
    self.seed = seed
    self.chunks = chunks

  def generate():
    print("hello")




class SubChunk: #represents every segment in NormalChunk class
  def __init__(self, x=0, y=0, z=0, has_item=None, has_pillar=None):
    self.x = x
    self.y = y
    self.z = z
    self.structure = Entity(position=(x, y, z))
    self.light_object = LitObject(position=(x, y, z))
    self.item = LitObject(position=(x, y, z))
    self.random_value = random.randint(0, 100)
    self.collision_structure = Entity(position=(x, y, z))
    if has_item == None:
      if self.random_value < 2:
        self.has_item = True
      else:
        self.has_item = False
    else:
      self.has_item = has_item
    if has_pillar == None:
      if self.random_value <= 25:
        self.has_pillar = True
      else:
        self.has_pillar = False
    else:
      self.has_pillar = has_pillar
  
  def delete(self):
    self.structure.disable()
    try:
      self.item.disable()
    except:
      self.item.delete()
    self.light_object.disable()
    self.collision_structure.disable()
  
  
  def place_pillar(self, x=0, y=0, z=0):
    duplicate(wall, position=(x,y,z), scale=(1,10,1), parent=self.structure)
    duplicate(collider, position=(x,y,z), scale=(1,10,1), parent=self.collision_structure)
  
  
  
  
  def place_door(self, x=0, y=0, z=0, sideways=False):
    if sideways == False:
      duplicate(wall, position=(x-wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.structure)#left side of door
      duplicate(wall, position=(x+wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.structure)#right side of door
      duplicate(wall, position=(x, y+5, z), scale=(wall_spacing * 2, 2, wall_side_scale), parent=self.structure)#top side of door
      duplicate(collider, position=(x-wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.collision_structure)
      duplicate(collider, position=(x+wall_spacing / 1.5, y, z), scale=(wall_spacing / 1.5, 8, wall_side_scale), parent=self.collision_structure)      
    else:
      duplicate(wall, position=(x, y, z-wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.structure)#left side of door
      duplicate(wall, position=(x, y, z+wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.structure)#right side of door
      duplicate(wall, position=(x, y+5, z), scale=(wall_side_scale, 2, wall_spacing * 2), parent=self.structure)#top side of door
      duplicate(collider, position=(x, y, z-wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.collision_structure)
      duplicate(collider, position=(x, y, z+wall_spacing / 1.5), scale=(wall_side_scale, 8, wall_spacing / 1.5), parent=self.collision_structure)
  
  
  
  
  def place_wall(self, x=0, y=0, z=0, sideways=False):
    if sideways == False:
      duplicate(wall, position=(x, y, z), scale=(wall_spacing * 2, 20, wall_side_scale), parent=self.structure)
      duplicate(collider, position=(x, y, z), scale=(wall_spacing * 2, 20, wall_side_scale), parent=self.collision_structure)
    else:
      duplicate(wall, position=(x, y, z), scale=(wall_side_scale, 20, wall_spacing * 2), parent=self.structure)
      duplicate(collider, position=(x, y, z), scale=(wall_side_scale, 20, wall_spacing * 2), parent=self.collision_structure)
    
  def place(self):
    if self.has_item == True:
      self.item = random.randint(1, 1)
      if self.item == 1:
        self.item = items.AlmondWater(self.x, self.y, self.z)
        self.item.spawn()
      else:
        self.item = Entity(position=(self.x, self.y, self.z))
    else:
      self.items = Entity(position=(self.x, self.y, self.z))
    
    if self.has_pillar == True:
      self.place_pillar(self.x + wall_spacing, self.y, self.z + wall_spacing)
    
        
    light_level = random.randint(0, 1)
    if light_level == 0:
      self.light_object = Entity(model="cube", 
                                scale=(2.2,1.2,4),
                                position=(self.x * 2 - wall_spacing, self.y+5.8, self.z * 2 - wall_spacing),
                                texture=Texture("resources/levels/level 0/lightoff.png"))
    else:
      self.light_object = Entity(model="cube", 
                                scale=(2.2,1.2,4),
                                position=(self.x * 2 - wall_spacing, self.y+5.8, self.z * 2 - wall_spacing),
                                texture=Texture("resources/levels/level 0/light.png"))
      self.light = LitPointLight(position=Vec3(self.x * 2 - wall_spacing, self.y+4, self.z * 2 - wall_spacing), intensity=1, color=rgb(248, 252, 150))
      
    left_rand = random.randint(0, 2)
    if left_rand == 1:
        self.place_door(self.x, self.y, self.z - wall_spacing, True)
    elif left_rand == 2:
      self.place_wall(self.x, self.y, self.z - wall_spacing, True)
    else:
      pass
    
    top_rand = random.randint(0, 2)
    if top_rand == 1:
      self.place_door(self.x + wall_spacing, self.y, self.z, False)
    elif top_rand == 2:
      self.place_wall(self.x + wall_spacing, self.y, self.z, False)
    else:
      pass
    
    #duplicate(floor, position=(self.x, self.y, self.z), scale=(wall_spacing, 0, wall_spacing))
    #duplicate(ceiling, position=(self.x, self.y+6, self.z), scale=(wall_spacing, 0, wall_spacing))
    
    
    
    

class NormalChunk:
  def __init__(self, x, y, z, size=20):
    self.x = x
    self.y = y
    self.z = z
    self.size = size
    self.chunks = []
    
  def place(self):
    row = 0
    collumn = 0
    while row <= self.size:
      while collumn <= self.size:
        print(f"generating normalchunks {row}:{collumn}")
        chunk = SubChunk(self.x + (collumn * wall_spacing), self.y, self.z + (row * wall_spacing))
        self.chunks.append(chunk)
        chunk.place()
        collumn += 1
      row += 1
      collumn = 0
  
  def delete(self):
    for chunk in self.chunks:
      chunk.delete()
    
    self.chunks = []
  
  def get_type(self):
    return(f"NormalChunk at {self.x, self.y, self.z} and {self.size}")




class IrregularChunk:
  def __init__(self, x, y, z, size=20, placements=10):
    self.x = x
    self.y = y
    self.z = z
    self.size = size
    self.placements = placements
    self.pieces = []
  
  def place(self):
    for i in range(self.placements):
      random_up = random.randint((self.size * wall_spacing) - ((self.size * wall_spacing) * 2), (self.size * wall_spacing))
      random_side = random.randint((self.size * wall_spacing) - ((self.size * wall_spacing) * 2), (self.size * wall_spacing))
      random_scale1 = random.randint(self.size - (self.size * 2), self.size)
      random_scale2 = random.randint(self.size - (self.size * 2), self.size)
      piece = LitObject(model="cube",
              texture=Texture("resources/levels/level 0/wall.png"),
              scale=(random_scale1, 10, random_scale2),
              collider="box",
              position=(self.x + random_up, self.y, self.z + random_side),
              specularMap=load_texture("resources/levels/level 0/noreflect.png"),
              cubemapIntensity=0)
      self.pieces.append(piece)
  
  def delete(self):
    for piece in self.pieces:
      piece.disable()
    
    self.pieces = []
  
  def get_type(self):
    return(f"IrregularChunk at {self.x, self.y, self.z} with size of {self.size} containing {self.placements} placements")
      


class Chunk:
  def __init__(self, size=20, type="normal", position=(0,0,0), varients=5):
    self.size = size
    self.type = type
    self.position = position
    self.varients = varients
  
  def create(self):
    global list_of_cords
    global chunk_types
    chunk_types.append(self.type)
    new_chunk = []
    while z <= self.size:
      while x <= self.size:
        cords = [x, z]
        percent = int((z /  self.size) * 100)
        if percent < 0:
          percent = 0
        print(f"generating {self.position} varient {self.type}: {cords} {percent}%")
        new_chunk.append(cords)
        x += 1
      x = min
      z += 1
  


