World = {
    "OMD": {
        'NAME': "Forest",
        'DESCRIPTION': "You Awoke here, there are paths to the East and West",
        'PATHS': {
            'EAST': 'OLD',
            'WEST': 'ORD',
        }
     },
    "OLD": {
        "NAME": "Forest",
        'DESCRIPTION': "You are surrounded by trees and shrubbery, there are paths to the North and West",
        'PATHS': {
            "WEST": "OMD",
            "NORTH": "OLM",
        }
    },
    "ORD": {
        "NAME": "Forest",
        "DESCRIPTION": "Your'e surrounded by trees and shrubbery, there's glint from one of the bushes"
                       " There are paths to the North and to the East",
        "PATHS": {
            "NORTH": "ORM",
            "EAST": "OMD",
        },
    },
    "OLM": {
        "NAME": "Forest",
        "DESCRIPTION": "You're surrounded by trees and shrubbery, there are paths to the North and the south",
        "PATHS": {
            "NORTH": "OLU",
            "SOUTH": "OLD",
        },
    },
    "ORM": {
        "NAME": "Forest",
        "DESCRIPTION": "Trees and shrubbery surround you, there are paths to the North and the South, There is a small"
                       " crack in the mossy mountain to the west",
        "PATHS": {
            "NORTH": "ORU",
            "SOUTH": "ORD",
            "WEST": "MW1"
        },
    },
    "ORU": {
        "NAME": "Forest",
        "DESCRIPTION": "You are surrounded by dying trees and shrubbery, there are paths to the West and South",
        "PATHS": {
            "WEST": "OMU",
            "SOUTH": "ORM",
        },
    },
    "OMU": {
        "NAME": "Forest",
        "DESCRIPTION": "You are surrounded by dying trees and shrubbery, the wall to the north is covered in a thick"
                       " layer of Moss",
        "PATHS": {
            "NORTH": "MW2",
            "EAST": "ORU",
            "WEST": "OLU",
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
                       " further",
        "PATHS": {
            "EAST": "ORM",
        },
    },
    "MW1": {
        "NAME": "Mossy wall",
        "DESCRIPTION": "A mossy wall with a slight crack in the middle, you can't see through it",
        "PATHS": {
            "EAST": "ORM",
            "CHECK": "OMM"
        },
    },
    "MW2": {
        "NAME": "mossy wall",
        "DESCRIPTION": "It is a mossy wall",
        "PATHS": {
            "CHECK": "RDCE",
            "SOUTH": "OMU",
        },
    },
    "RDCE": {
        "NAME": "Rubber Duck Cult entrance",
        "DESCRIPTION": "This is the entrance to the rubber duck cult, there are white walls to the East and West, "
                       "and a door with a purple duck scanner",
        "PATHS": {
            "WEST": "WWW",
            "EAST": "WWR",
            "SOUTH": "OMU"
        },
    },
    "WWW": {
        "NAME": "White wall",
        "DESCRIPTION": "It is a white wall,there are paths to the West and the North",
        "PATHS": {
            "NORTH": "RDCED",
            "WEST": "RDCE"
        },
    },
    "WWR": {
        "NAME": "White wall",
        "DESCRIPTION": "It's a white wall there are paths to the West and to the North",
        "PATHS": {
            "NORTH": "RDCED",
            "WEST": "RDCE"
        },
    },
    "RDCED": {
        "NAME": "Rubber Duck Cult entrance door",
        "DESCRIPTION": "This is the door that leads to the main room of the Rubber Duck Cult, there is a path to the "
                       "South",
        "PATHS": {
            "SOUTH": "RDCE"
        },
    },
}

current_node = World["OMD"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", "CHECK"]
playing = True


while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
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
