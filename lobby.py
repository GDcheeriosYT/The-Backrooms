from ursina import *
from UrsinaLighting import *

tile = LitObject(model="cube",
                 texture=Texture('resources/levels/lobby/floor_tile.png'),
                 collider="box",
                 smoothness=200,
                 position=(0, -10, 0),
                 tiling=(70, 70),
                 scale=(100, 2, 100))

wall = LitObject(model="cube",
                 texture=Texture('resources/levels/lobby/pool_tile.png'),
                 collider="box",
                 smoothness=200,
                 position=(0, -10, 10),
                 tiling=(30, 150),
                 scale=(100, 200, 5))

ceiling = LitObject(model="cube",
                 texture=Texture('resources/levels/lobby/pool_tile.png'),
                 collider="box",
                 smoothness=200,
                 position=(0, 1, 0),
                 tiling=(70, 70),
                 scale=(100, 1, 100))

ceiling_light = LitObject(model="sphere",
                          color=Vec4(10, 10, 10, 255),
                          position=(0, 0.7, 0),
                          scale=(1, 1, 1))

LitPointLight(position=Vec3(0, -0.6, 0), intensity=0.4, range=100, color=Vec3(1,1,1.3))