import subprocess
import sys
import time
import asyncio
import random
from ursina import *
from UrsinaLighting import *
from game import *

server_name = input("server name: ")
server_password = input("server password(optional): ")

game = Game(server_name, server_password)

def install(package):
    print(f"installing requirement {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
seed = random.randint(0, 99999999999)

try:
  from ursinanetworking import *
except:
  install("ursinanetworking")
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