from xml.dom.minidom import Entity
import entity

f = open("entity_dict.txt", "w+")
entity_amount = int(input("how many entities are there? "))
entities = {}

def dict_appender(entity, rarity):
  global entities
  entities[entity] = rarity
  
for i in range(entity_amount):
  x = 0
  for instance in entity.entity.instances:
    print(x, instance)
    x += 1
  
  entity_picker = entity.entity.instances[int(input("which one? "))]
  
  rarity = int(input("rarity: "))
  dict_appender(entity_picker, rarity)

f.write(str(entities))
f.close()