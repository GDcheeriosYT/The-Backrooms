import json
import random
import os

segments = []
for segment in os.listdir("segments/"):
  segments.append(segment)

def manage_segment(segment = segments[random.randint(0, len(segments) - 1)], output=False, rotate = random.randint(0, 3)):
  
  '''
  parses a segment and manages positioning of walls
  
  segment : json Object
  ---------------------
  segment to parse
  
  output : Boolean
  ----------------
  if True will show output, good for debugging
  
  rotate : int
  ----------------
  will rotate using 0 as 0/360 degrees and 3 being 270 degrees if defualt it will be random 0-3
  '''
  
  with open(f"segments/{segment}") as placement_data:
    placement_data = json.load(placement_data)
  
    print("looking at: ", segment)
  wall_placements = []
  for row in placement_data:
    if output == True:
      print(f"looking at {row}")
    collumn = 0
    for number in placement_data[row]:
      
      if number == 1:
        #set position name in row1
        if collumn == 0 and row == "row1":
          wall_placements.append("top left")
        elif collumn == 1 and row == "row1":
          wall_placements.append("top")
        elif collumn == 2 and row == "row1":
          wall_placements.append("top right")
        #set position name in row2
        elif collumn == 0 and row == "row2":
          wall_placements.append("left")
        elif collumn == 1 and row == "row2":
          wall_placements.append("center")
        elif collumn == 2 and row == "row2":
          wall_placements.append("right")
        #set position name in row3
        elif collumn == 0 and row == "row3":
          wall_placements.append("bottom left")
        elif collumn == 1 and row == "row3":
          wall_placements.append("bottom")
        elif collumn == 2 and row == "row3":
          wall_placements.append("bottom right")
        
        one_count += 1
        if output == True:
          print("found a 1!")

      collumn += 1
  
  return(wall_placements)