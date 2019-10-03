# -*- coding: utf-8 -*-
'''Ideas for text adventure data structures'''

kitchen = ["Kitchen", "This is the kitchen."]
livingRoom = ["Living Room", "There's a dusty sofa here."]
bedroom = ["Bedroom", "There is a creepy doll here."]

rooms = [kitchen, livingRoom, bedroom]

for room in rooms:
    print("You are in", room[0])
    print("Description: ", room[1])
    print()
    print("Moving to next room...")

#we could use dictionaries
kitchenDescription = "This is the Kitchen"
kitchenExits = {"east":"Living Room"}
KitchenInfo = [kitchenDescription, kitchenExits]

lrDescription = "There's a dusty sofa here."
lrExits={"west":"Kitchen",
         "south":"Bedroom"}
lrInfo= [lrDescription, lrExits]

BedroomDescription = "There is a creepy doll here."
BedroomExits = {"west":"Living Room",
                "north":"Bedroom"}
BedroomInfo = [BedroomDescription, BedroomExits]

roomDict = {
    "Kitchen": ["This is the kitchen.", {"east":"Living Room"}],
    "Living Room":["There's a dusty sofa here.",{"west":"Kitchen", "south":"Bedroom"}],
    "Bedroom":"There is a creepy doll here."
    }
