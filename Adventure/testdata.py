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
