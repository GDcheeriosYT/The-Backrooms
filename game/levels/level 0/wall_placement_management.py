import json

def manage_segment(segment, output=False):
  
  '''
  parses a segment and manages positioning of walls
  
  segment : json Object
  ---------------------
  segment to parse
  
  output : Boolean
  ----------------
  if True will show output, good for debugging
  
  '''
  
  with open(f"segments/{segment}.json") as placement_data:
    placement_data = json.load(placement_data)
  
  one_count = 0 #amount of 1's in array
  for row in placement_data:
    if output == True:
      print(f"looking at {row}")
    for number in placement_data[row]:
      if number == 1:
        one_count += 1
        if output == True:
          print("found a 1!")
  
  return(one_count)
  
  
        