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


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %s damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """this method moves a character to a new location

        :param new_location: the variable containing a room object
        """
        self.current_location = new_location


class Item(object):
    def __init__(self, weight, damage, attack_type, distance):
        self.weight = weight
        self.damage = damage
        self.attack_type = attack_type
        self.distance = distance


class Armor(Item):
    def __init__(self, weight, damage, attack_type, distance, defense):
        super(Armor, self).__init__(weight, damage, attack_type, distance)
        self.defense = defense


class Hats(Armor):
    def __init__(self, weight, damage, attack_type, distance, defense, hat_type):
        super(Hats, self).__init__(weight, damage, attack_type, distance, defense)
        self.hat_type = hat_type


class Cappy(Hats):
    def __init__(self, weight, damage, attack_type, distance, defense, hat_type, bounces):
        super(Cappy, self).__init__(weight, damage, attack_type, distance, defense, hat_type)
        self.bounces = bounces


class ChestPiece(Armor):
    def __init__(self, weight, damage, attack_type, distance, defense, chest_piece_type):
        super(ChestPiece, self).__init__(weight, damage, attack_type, distance, defense)
        self.chest_piece_type = chest_piece_type


class LegArmor(Armor):
    def __init__(self, weight, damage, attack_type, distance, defense, leg_type_armor):
        super(LegArmor, self).__init__(weight, damage, attack_type, distance, defense)
        self.leg_type_armor = leg_type_armor


class Shoes(Armor):
    def __init__(self, weight, damage, attack_type, distance, defense, shoe_size):
        super(Shoes, self).__init__(weight, damage, attack_type, distance, defense)
        self.shoe_size = shoe_size


class Melee(Item):
    def __init__(self, weight, damage, attack_type, distance, sharpness):
        super(Melee, self).__init__(weight, damage, attack_type, distance)
        self.sharpness = sharpness


class Dominic(Melee):
    def __init__(self, weight, damage, attack_type, distance, sharpness):
        super(Dominic, self).__init__(weight, damage, attack_type, distance, sharpness)
        self.jokes = None


class Consumables(Item):
    def __init__(self, weight, damage, attack_type, distance, ammunition):
        super(Consumables, self).__init__(weight, damage, attack_type, distance)
        self.ammunition = ammunition


class Elijah(Consumables):
    def __init__(self, weight, damage, attack_type, distance, ammunition):
        super(Elijah, self).__init__(weight, damage, attack_type, distance, ammunition)
        self.smash_skill = True


class Ranged(Item):
    def __init__(self, weight, damage, attack_type, distance, quality):
        super(Ranged, self).__init__(weight, damage, attack_type, distance)
        self.quality = quality


class Weibe(Ranged):
    def __init__(self, weight, damage, attack_type, distance, quality, computer):
        super(Weibe, self).__init__(weight, damage, attack_type, distance, quality)
        self.computer = computer


class Staff(Melee, Ranged):
    def __init__(self, weight, damage, attack_type, distance, sharpness, quality, magic_type):
        Melee.__init__(self, weight, damage, attack_type, distance, sharpness)
        Ranged.__init__(self, weight, damage, attack_type, distance, quality)
        self.magic_type = magic_type


class Sword(Melee):
    def __init__(self, weight, damage, attack_type, distance, sharpness, blade_type):
        super(Sword, self).__init__(weight, damage, attack_type, distance, sharpness)
        self.blade_type = blade_type


class Bow(Ranged):
    def __init__(self, weight, damage, attack_type, distance, quality, arrow_type):
        super(Bow, self).__init__(weight, damage, attack_type, distance, quality)
        self.arrow_type = arrow_type


class Potion(Consumables):
    def __init__(self, weight, damage, attack_type, distance, ammunition, potion_effect):
        super(Potion, self).__init__(weight, damage, attack_type, distance, ammunition)
        self.potion_effect = potion_effect


class Excalibur(Sword):
    def __init__(self, weight, damage, attack_type, distance, sharpness, blade_type, holy_aura):
        super(Excalibur, self).__init__(weight, damage, attack_type, distance, sharpness, blade_type)
        self.holy_aura = holy_aura


class ElementalBow(Bow):
    def __init__(self, weight, damage, attack_type, distance, quality, arrow_type, element_type):
        super(ElementalBow, self).__init__(weight, damage, attack_type, distance, quality, arrow_type)
        self.element_type = element_type


class Gloves(Melee):
    def __init__(self, weight, damage, attack_type, distance, sharpness, fit):
        super(Gloves, self).__init__(weight, damage, attack_type, distance, sharpness)
        self.fit = fit


class Cultist(object):
    def __init__(self):
        self.Health = 20
        self.Damage = 10
        self.Name = Cultist


# weapons
True_Excalibur = Excalibur(7.5, 25, "swing/bash/beyblade spin", 7, True, "Long", True)
Shaggys_sword = Sword(0, 99999999999999999999999999999999999999999999999, "All", 99999999999999999999999999999999999999,
                      9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
                      "All")

# characters
c1 = Character("Orc1", 100, True_Excalibur, None)
c2 = Character("Shaggy", 9999999999999999999999999999999999999999, Shaggys_sword, None)

c1.attack(c2)
c2.attack(c1)

OMD = Room("Forest", "You Awoke here, there are paths to the East and West", None, "ORD", None, "OLD")
ORD = Room("Forest", "Your'e surrounded by trees and shrubbery, there's glint from one of the bushes "
                     "there are paths to the North and to the East", "ORM", "OMD", None, None)
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
                     " layer of moss", "MW2", "ORU", None, "OLU")
OLU = Room("Forest", "You are surrounded by trees and shrubbery, there are paths to the East and the South", None,
           "OMU", "OLM", None)
OMM = Room("Cave", "There is a bit of light filtering into the cave, there is a path to the east", None, "ORM", None,
           "CV1")
CV1 = Room("Cave", "you are in the dark you cannot continue further", None, "OMM", None, None)
MW2 = Room("Mossy wall", "It's a mossy wall", "PDS1", None, "OMU", None)
PDC = Room("purple duck scanner", "It's a purple duck scanner", )
RDCE = ("Rubber duck cult entrance", "This is the entrance to the rubber duck cult, there are white walls to the "
                                     "East and West, and a door with a purple duck scanner to the north",)
PDS1 = Room("A duck scanner", "A scanner for level purple ducks", "RDCE", None, "MW2", None)

player = Player(OMD)

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
