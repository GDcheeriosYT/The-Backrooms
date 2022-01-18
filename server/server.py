import subprocess
import sys
import time

def install(package):
    print(f"installing requirement {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
  from ursinanetworking import *
except:
  install("ursinanetworking")
  from ursinanetworking import *