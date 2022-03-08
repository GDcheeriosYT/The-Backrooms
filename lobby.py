from ursina import *
from UrsinaLighting import *
import player as br_player


#audio
water_ambiance = Audio("resources/levels/lobby/water_ambiance.mp3", loop=True)
water_ambiance.volume = 0.3
water_ambiance.play()

#variables
light_range = 100
light_intensity = 0.3
light_color=Vec3(0, 0, 0.2)
floor_color=rgb(500, 500, 500, 255)

#main room
floor = LitObject(model="cube", color=floor_color, texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(-30, -6, 0), tiling=(5, 5), scale=(40, 0.1, 40))
floor = LitObject(model="cube", color=floor_color, texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(30, -6, 0), tiling=(5, 5), scale=(40, 0.1, 40))
floor = LitObject(model="cube", color=floor_color, texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(0, -6, 30), tiling=(5, 5), scale=(40, 0.1, 40))
floor = LitObject(model="cube", color=floor_color, texture=Texture('resources/levels/lobby/floor_tile.png'), collider="box", smoothness=100, position=(0, -6, -30), tiling=(5, 5), scale=(40, 0.1, 40))
floor = LitObject(model="cube", color=floor_color, texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(0, -12, 0), tiling=(30, 30), scale=(40, 2, 40))
ceiling = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(0, 1, 0), tiling=(20, 20), scale=(100, 1, 100))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(0, -10, 20), tiling=(10, 6), scale=(40, 30, 1))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(0, -10, -20), tiling=(10, 6), scale=(40, 30, 1))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(20, -10, 0), tiling=(10, 6), scale=(1, 30, 40))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(-20, -10, 15), tiling=(6, 6), scale=(1, 30, 20))
wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile.png'), collider="box", smoothness=100, position=(-20, -10, -15), tiling=(6, 6), scale=(1, 30, 20))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(0, -10, 10.48), scale=(40, 8, 1), tiling=(15, 10))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(10.48, -10, 0), scale=(1, 8, 40), tiling=(15, 10))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(0, -10, -10.48), scale=(40, 8, 1), tiling=(15, 10))
pool_wall = LitObject(model="cube", texture=Texture('resources/levels/lobby/pool_tile_under.png'), collider="box", smoothness=100, position=(-10.48, -10, 0), scale=(1, 8, 40), tiling=(15, 10))
ceiling_light = LitObject(model="sphere", color=Vec4(10, 10, 10, 255), position=(0, 0.7, 0), scale=(1, 1, 1))
water = LitObject(position = (0, -7.2, 1), color=rgb(50, 50, 70, 225), scale = 25, water = True, cubemapIntensity = 0.75, ambientStrength = 0.80)
door = LitObject(model="resources/levels/lobby/door.obj", scale=(50, 40, 50), position=(-13, -6.2, -19.5))
screen = LitObject(model="cube", color=rgb(100, 100, 100, 255), position=(19, -4, 0), scale=(0.1, 10, 10))

#lobby functions
def players(game):
  y_val = 0.4
  for player in game.players:
    print(player.name)
    print(player.color)
    Text(f"{player.name}", scale=(2, 2 ), parent=screen, position=(-2, y_val, 0), color=rgb(player.color[0], player.color[1], player.color[2]), billboard=True)
    y_val -= 0.1
