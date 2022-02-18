from ursina import *
from UrsinaLighting import *

#lights
light = Entity(model="cube", texture=Texture("../../../resources/levels/level 0/light.png"), color=color.white, position=(100,5.8,100), scale=(2.2,1.2,4), specularMap=load_texture("../../../resources/levels/level 0/noreflect.png"))
LitPointLight(position=Vec3(0,0,0), intensity=1, color=rgb(248, 252, 150))

#map
parent_wall_entity = Entity()
parent_light_entity = Entity()
chunk = Entity(model="cube",
               scale=(15, 100, 15),
               color=rgb(0,0,0,a=0))

'''chunks = Entity(model="cube",
               scale=(15, 100, 15),
               color=rgb(0,0,0,a=255))'''

wall = LitObject(model="cube",
              texture=Texture("../../../resources/levels/level 0/wall.png"),
              scale=(0,0,0),
              collider="box",
              position=(5,0,5),
              specularMap=load_texture("../../../resources/levels/level 0/noreflect.png"),
              cubemapIntensity=0)
collider = Entity(collider="box", scale=(0,0,0), position=(349024859,0,0))

#map construction
class BackroomSegment():
  def __init__(self, x=0, y=0, z=0, distance=5, scale=(5, 12, 5), is_blank=False, light_intensity_rate=[0, 1, 1, 1, 1, 1]):
    self.x = x
    self.y = y
    self.z = z
    self.type = type
    self.distance = distance
    self.scale = scale
    self.is_blank = is_blank
    self.light_intensity_rate = light_intensity_rate
    self.light_level = self.light_intensity_rate[random.randint(0, len(self.light_intensity_rate) - 1)]
    
  def create_segment(self):
    
    def place(placement):
      duplicate(wall,
                scale=self.scale,
                position=placement,
                parent=parent_wall_entity,
                specularMap=load_texture("../../../resources/levels/level 0/noreflect.png"),
                cubemapIntensity=0)
      duplicate(collider,
                scale=self.scale,
                position=placement)
      duplicate(light,
                position=placement,
                parent=parent_light_entity)
      LitPointLight(position=Vec3(placement), intensity=self.light_level, color=rgb(248, 252, 150))
    
    if self.is_blank == False:
      positions = wpm.manage_segment(segment=wpm.random_segment(), rotate=random.randint(0, 3))
    elif self.is_blank == True:
      positions = wpm.manage_segment(segment="blank.json")
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
  
  def get(self):
    data = {
     "x" : self.x,
     "y" : self.y,
     "z" : self.z,
     "type" : self.type,
     "light level" : self.light_level
    }
    
    return(data)
  
  def load(self):
    None
  
  def unload(self):
    None