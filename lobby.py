from pyexpat import model
from ursina import *
from UrsinaLighting import *
import player as br_player

player = br_player.Player("GDcheerios", color=(0, 180, 0))
player.spawn(10, -7, 10)

#audio
water_ambiance = Audio("resources/levels/lobby/water_ambiance.mp3", loop=True)
water_ambiance.volume = 0.3
water_ambiance.play()

#variables
light_range = 100
light_intensity = 0.2


#main room
floor = LitObject(model="cube", texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(-30, -6, 0), tiling=(35, 35), scale=(40, 0.1, 40))
floor = LitObject(model="cube", texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(30, -6, 0), tiling=(35, 16), scale=(40, 0.1, 40))
floor = LitObject(model="cube", texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(0, -6, 30), tiling=(35, 35), scale=(40, 0.1, 40))
floor = LitObject(model="cube", texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(0, -6, -30), tiling=(35, 35), scale=(40, 0.1, 40))
floor = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(0, -12, 0), tiling=(30, 30), scale=(40, 2, 40))
ceiling = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(0, 1, 0), tiling=(70, 70), scale=(40, 1, 40))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(0, -10, 20), tiling=(10, 6), scale=(40, 30, 1))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(0, -10, -20), tiling=(10, 6), scale=(40, 30, 1))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), smoothness=100, position=(20, -10, 0), tiling=(10, 6), scale=(1, 30, 40))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(-20, -10, 15), tiling=(6, 6), scale=(1, 30, 20))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(-20, -10, -15), tiling=(6, 6), scale=(1, 30, 20))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(0, -10, 10.48), scale=(40, 8, 1), tiling=(15, 10))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(10.48, -10, 0), scale=(1, 8, 40), tiling=(15, 10))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(0, -10, -10.48), scale=(40, 8, 1), tiling=(15, 10))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(-10.48, -10, 0), scale=(1, 8, 40), tiling=(15, 10))
ceiling_light = LitObject(model="sphere", color=Vec4(10, 10, 10, 255), position=(10, 0.7, 0), scale=(1, 1, 1))
ceiling_light = LitObject(model="sphere", color=Vec4(10, 10, 10, 255), position=(-10, 0.7, 0), scale=(1, 1, 1))
ceiling_light = LitObject(model="sphere", color=Vec4(10, 10, 10, 255), position=(0, 0.7, 10), scale=(1, 1, 1))
ceiling_light = LitObject(model="sphere", color=Vec4(10, 10, 10, 255), position=(0, 0.7, -10), scale=(1, 1, 1))

#buttons
def update():
  if held_keys['f1']:
    import 
    scene.clear()
    

#lighting
LitPointLight(position=Vec3(10, -0.6, 0), intensity=light_intensity, range=light_range, color=Vec3(0,0,0.4))
LitPointLight(position=Vec3(-10, -0.6, 0), intensity=light_intensity, range=light_range, color=Vec3(0,0,0.4))
LitPointLight(position=Vec3(0, -0.6, 10), intensity=light_intensity, range=light_range, color=Vec3(0,0,0.4))
LitPointLight(position=Vec3(0, -0.6, -10), intensity=light_intensity, range=light_range, color=Vec3(0,0,0.4))