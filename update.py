import sys
import subprocess

def install(package):
    print(f"installing requirement {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
try:
  import GitPython
  import git
except:
  install("GitPython")
  import GitPython
  import git
  
print("checking for updates...")