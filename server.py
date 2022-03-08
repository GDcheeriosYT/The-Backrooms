import time
import asyncio
import random
from ursina import *
from UrsinaLighting import *
from game import *

server_name = input("server name: ")
server_password = input("server password(optional): ")
seed = input("seed(optional): ")

game = Game(server_name, server_password)

from ursinanetworking import *

print("starting a server...")
Server = UrsinaNetworkingServer("localhost", 6990)

@Server.event
def onClientConnected(Client):
  print(f"{Client} is here!")
  Server.broadcast("HelloFromServer", f"{Client} is here!")
  
@Server.event
def request_map(Client):
  Client.send_message("map_requested", seed)

while True:
    Server.process_net_events()