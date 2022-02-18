from ursina import *
from UrsinaLighting import *

floor = LitObject(model="cube",
               texture=Texture("../../../resources/levels/level 0/carpet.png"),
               scale=(1000, 1, 1000),
               collider="mesh",
               tiling=(250,250),
               position=(0,0,0),
               specularMap=load_texture("../../../resources/levels/level 0/noreflect.png"),
               cubemapIntensity=0)
ceiling = LitObject(model="cube",
                 texture=Texture("../../../resources/levels/level 0/ceiling.png"),
                 scale=(1000, 1, 1000),
                 tiling=(500,500),
                 collider="mesh",
                 position=(0,6,0),
                 specularMap=load_texture("../../../resources/levels/level 0/noreflect.png"),
                 cubemapIntensity=0)