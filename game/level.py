class level:
  def __init__(self, name, number, description, entities):
    self.name = name
    self.number = number
    self.description = description
    self.entities = entities

The_Lobby = level("The Lobby", 0, "Level 0 is a non-linear space, resembling the back rooms of a retail outlet. All rooms in Level 0 appear uniform and share superficial features such as yellowed wallpaper, damp carpet, and inconsistently placed fluorescent lighting. However, no two rooms within Level 0 are identical.", {'Hound': 20, 'Facelings': 20, 'Lighter': 2})




class room:
  def __init__(self, name):
    None