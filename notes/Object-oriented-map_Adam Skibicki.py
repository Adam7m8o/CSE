class Room(object):
    def __init__(self, name, description="", north=None, east=None, south=None, west=None, check=None, up=None,
                 down=None):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.check = check
        self.items = []

class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """this method moves a character to a new location

        :param new_location: the variable containing a room object
        """
        self.current_location = new_location

class Cultist(object):
    def __init__(self):
        self.Health = 20
        self.Damage = 10
        self.Name = Cultist

'''
R19A = Room("R19A", parking_lot)
parking_lot = Room('the parking lot', "blank", R19A)


# option 1
R19A.north = parking_lot
'''

# option 2
# put them in quotes
R19A = Room("R19A", "This is mr wiebe's room", "parking_lot")
parking_lot = Room("The parking lot", "It's a parking lot", "R19A")

player = Player(R19A)

playing = True
directions = ["north", "south", "east", "west", "up", "down", "check"]

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ["q", "quit", 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except AttributeError:
            print("I can't go that way")
        except KeyError:
            print("This key doesn't exist")
    else:
        print("command not recognized")



OMD = Room("Forest", "You Awoke here, there are paths to the East and West", None, "ORD", None, "OLD")
ORD = Room("Forest", "Your'e surrounded by trees and shrubbery, there's glint from one of the bushes "
                     "there are paths to the North and to the East", "ORM", "OMD", None, None )
OLD = Room("Forest", "You are surrounded by trees and shrubbery, there are paths to the North and West", "OLM", None,
           None, "OMD")
OLM = Room("Forest", "You're surrounded by trees and shrubbery, there are paths to the North and the south", "OLU",
           None, "OLD", None)
ORM = Room("Forest", "Trees and shrubbery surround you, there are paths to the North and the South,"
                     "There is a small crack in the mossy mountain to the west", "ORU", None, "ORD", "MW1")
ORU = Room("Forest", "You are surrounded by dying trees and shrubbery, there are paths to the West and South", None,
           None, "ORM", "OMU")
MW1 = Room("Mossy Wall", "It's a mossy wall", None, "ORM", None, None)
OMU = Room("Forest", "You are surrounded by dying trees and shrubbery, the wall to the north is covered in a thick"
                     "layer of moss", "MW2", "ORU", None, "OLU")
OLU = Room("Forest", "You are surrounded by trees and shrubbery, there are paths to the East and the South", None,
           "OMU", "OLM", None)
OMM = Room("Cave", "There is a bit of light filtering into the cave, there is a path to the east", None, "ORM", None,
           "CV1")
CV1 = Room("Cave", "you are in the dark you cannot continue further", None, "OMM", None, None)
MW2 = Room("Mossy wall", "It's a mossy wall", "PDS1", None, "OMU", None)
PDC = Room("purple duck scanner", "It's a purple duck scanner", )
RDCE = ("Rubber duck cult entrance", "This is the entrance to the rubber duck cult, there are white walls to the"
                       "East and West, and a door with a purple duck scanner to the north",)
PDS1 = Room("A duck scanner", "A scanner for level purple ducks", "RDCE", None, "MW2", None)
WW1 = Room("A white wall", "It's a white wall")