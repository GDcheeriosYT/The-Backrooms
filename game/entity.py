class entity:
  instances = []
  def __init__(self, name, id, model, description):
    """creates an entity

    Args:
        name (string): the name of the entity
        id (int): the id of the entity from backrooms
        description (string): the description of the entity
    """
    self.name = name
    self.id = id
    self.model = model
    self.description = description
    entity.instances.append(self.name)
  
  def get_name(self):
    return(self.name)
  
  def get_id(self):
    return(self.id)
  
  def get_model(self):
    return(self.model)
  
  def get_description(self):
    return(self.description)

The_Windows = entity("The Windows", 2, "resources/entities/The Windows/model.png", "The Windows are creatures in the shape of a Window. The Window has a figure inside, always pointing at the target. If the target is unaware of the creature, it will attack immediately.")
Hound = entity("Hound", 8, "resources/entities/Hound/model.png", "The name Hound comes from the dog-like nature of these Entities, crawling on all fours and mauling anyone that provokes them. Hounds are humanoids with a strange biology, with arms and legs that are built for travel on all fours. They are very, VERY dangerous and become agitated when they see someone in a hostile state, but can be intimidated.")
Facelings = entity("Facelings", 9, "resources/entities/Facelings/model.png", "Facelings are a general term for faceless people that roam the backrooms. There are multiple types, each with varying levels of hostility. They are one of the most populous entities in the backrooms, and likely one of the first entities you will encounter. The most common two forms are Adult Facelings and Child Facelings, although more have since been discovered. Do not even try to make a joke about this.")
Lighter = entity("Lighter", 0, "resources/entities/Lighter/model.png", "The Lighter is a extremely rare Entity, and is observed as a very bright type of organism that blinds the viewer within a minute easily. Normally its speed is the same as an average human's. Coming near it will cause you to feel hot, touching and making contact with the entity causes one's body to completely ignite and vaporise . To outrun one, the tactic is to run onwards into random areas until the Entity loses track of you. Lighters have little stamina, being able to follow only 75 meters as a limit.")