current_node = World["OMD"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True
World = {
    "OMD":{
        'NAME': "Forest",
        'DESCRIPTION': "You Awoke here, there are paths to the East and West",
        'PATHS': {
            'EAST': 'OLD',
            'WEST': 'ORD',
                 },
    "OLD": {
        "NAME": "Forest",
            'DESCRIPTION': "You are surrounded by trees and shrubbery, there are paths to the North and West",
            'PATHS': {
                "WEST": "OMD",
                "NORTH": "OLM",
            },
    "ORD":{
        "NAME": "Forest",
        "DESCRIPTION": "Your'e surrounded by trees and shrubbery, there's glint from one of the bushes"
                       "There are paths to the North and to the West",
        "PATHS":{
            "NORTH": "ORM",
            "WEST": "OMD",
        },
    },
    "OLM": {
        "NAME": "Forest",
        "DESCRIPTION": "You're surrounded by trees and shrubbery, there are paths to the North and the south",
        "PATHS": {
            "NORTH": "OLU",
            "South": "OLD",
        },
    },
    "ORM": {
        "NAME": "Forest",
        "DESCRIPTION": "Trees and shrubbery surround you, there are paths to the North and the South, There is a small"
                       "crack in the mossy mountain to the west",
        "PATHS": {
            "NORTH": "ORD",
            "SOUTH": "ORU",
            "WEST": "MW1"
        },
    },
    "ORU":{
        "NAME": "Forest",
        "DESCRIPTION": "You are surrounded by dying trees and shrubbery, there are paths to the Wast and South",
        "PATHS":{
            "WEST": "OMU",
            "SOUTH": "ORM"
        },
    },
    "OMU": {
        "NAME": "Forest",
        "Description": "You are surrounded by dying trees and shrubbery, the wall to the north is covered in a thick layer of Moss",
        "PATHS":{
            "NORTH": "MW2",
            "EAST": "ORU",
            "WEST": "OLU"
        },
    },
    "OLU": {
        "NAME": "Forest",
        "DESCRIPTION": "You are surrounded by trees and shrubbery, there are paths to the East and the South",
        "PATHS": {
            "EAST": "OMU",
            "SOUTH": "OLM"
        },
    },
    "OMM": {
        "NAME": "Cave entrance",
        "DESCRIPTION": "You are inside the mountain, there is little light shining in through the hole you made in the "
                       "wall, other which allows you to see five feet into the cave, but it is too dark to continue"
                       "further",
        "PATHS": {
            "EAST": "ORM",
            "WEST": ""
        },
    },
    "MW1": {
        "NAME": "Mossy wall",
        "DESCRIPTION": "A mossy wall with a slight crack in the middle, you can't see through it",
        "PATHS": {
            "EAST": "ORM",
        },
    },
    "MW2":{
        "NAME": "mossy wall",
        "DESCRIPTION": "It is a mossy wall",
        "PATHS": {
            "CHECK": "PDC",
            "SOUTH": "OMU",
        },
    },
    "RDCE":{
        "NAME": "Rubber Duck Cult entrance",
        "DESCRIPTION": "This is the entrance to the rubber duck cult, there are white walls to the East and West, and a "
                       "Door with a purple duck scanner",
        "PATHS": {

        },
    },
},

while playing == True:
    command = input(">_")
    if command.lower() in ["q", "quit", 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node["PATHS"][command.upper()]
            current_node = World[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("command not recognized")
