class Room(object):
    def __init__(self, name, description="", north=None, east=None, south=None, west=None, check=None, up=None,
                 down=None, items=[]):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.check = check
        self.items = items


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


class Cultist(Character):
    def __init__(self, name, health, weapon, armor, level):
        super(Cultist, self).__init__(name, health, weapon, armor)
        self.level = level


class RubberDuck(Character):
    def __init__(self, name, health, weapon, armor, person):
        super(RubberDuck, self). __init__(name, health, weapon, armor)
        self.person = person


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

'''
    def get(self, inventory):
        print()
        Room.self.items
'''


class Item(object):
    def __init__(self, name, weight, damage, attack_type, distance):
        self.name = name
        self.weight = weight
        self.damage = damage
        self.attack_type = attack_type
        self.distance = distance


class Armor(Item):
    def __init__(self, name, weight, damage, attack_type, distance, defense):
        super(Armor, self).__init__(name, weight, damage, attack_type, distance)
        self.defense = defense


class Hats(Armor):
    def __init__(self, name, weight, damage, attack_type, distance, defense, hat_type):
        super(Hats, self).__init__(name, weight, damage, attack_type, distance, defense)
        self.hat_type = hat_type


class Cappy(Hats):
    def __init__(self, name, weight, damage, attack_type, distance, defense, hat_type, bounces):
        super(Cappy, self).__init__(name, weight, damage, attack_type, distance, defense, hat_type)
        self.bounces = bounces


class ChestPiece(Armor):
    def __init__(self,name, weight, damage, attack_type, distance, defense, chest_piece_type):
        super(ChestPiece, self).__init__(name, weight, damage, attack_type, distance, defense)
        self.chest_piece_type = chest_piece_type


class LegArmor(Armor):
    def __init__(self, name, weight, damage, attack_type, distance, defense, leg_type_armor):
        super(LegArmor, self).__init__(name, weight, damage, attack_type, distance, defense)
        self.leg_type_armor = leg_type_armor


class Shoes(Armor):
    def __init__(self, name, weight, damage, attack_type, distance, defense, shoe_size):
        super(Shoes, self).__init__(name, weight, damage, attack_type, distance, defense)
        self.shoe_size = shoe_size


class Melee(Item):
    def __init__(self, name, weight, damage, attack_type, distance, sharpness):
        super(Melee, self).__init__(name, weight, damage, attack_type, distance)
        self.sharpness = sharpness


class Dominic(Melee):
    def __init__(self, name, weight, damage, attack_type, distance, sharpness):
        super(Dominic, self).__init__(name, weight, damage, attack_type, distance, sharpness)
        self.jokes = None


class Consumables(Item):
    def __init__(self, name, weight, damage, attack_type, distance, ammunition):
        super(Consumables, self).__init__(name, weight, damage, attack_type, distance)
        self.ammunition = ammunition


class Elijah(Consumables):
    def __init__(self, name, weight, damage, attack_type, distance, ammunition):
        super(Elijah, self).__init__(name, weight, damage, attack_type, distance, ammunition)
        self.smash_skill = True


class Ranged(Item):
    def __init__(self, name, weight, damage, attack_type, distance, quality):
        super(Ranged, self).__init__(name, weight, damage, attack_type, distance)
        self.quality = quality


class Weibe(Ranged):
    def __init__(self, name, weight, damage, attack_type, distance, quality, computer):
        super(Weibe, self).__init__(name, weight, damage, attack_type, distance, quality)
        self.computer = computer


class Staff(Melee, Ranged):
    def __init__(self, name, weight, damage, attack_type, distance, quality, magic_type):
        Ranged.__init__(self, name, weight, damage, attack_type, distance, quality)
        self.magic_type = magic_type


class Sword(Melee):
    def __init__(self, name, weight, damage, attack_type, distance, sharpness, blade_type):
        super(Sword, self).__init__(name, weight, damage, attack_type, distance, sharpness)
        self.blade_type = blade_type


class Bow(Ranged):
    def __init__(self, name, weight, damage, attack_type, distance, quality, arrow_type):
        super(Bow, self).__init__(name, weight, damage, attack_type, distance, quality)
        self.arrow_type = arrow_type


class Potion(Consumables):
    def __init__(self, name, weight, damage, attack_type, distance, ammunition, potion_effect):
        super(Potion, self).__init__(name, weight, damage, attack_type, distance, ammunition)
        self.potion_effect = potion_effect


class Excalibur(Sword):
    def __init__(self, name, weight, damage, attack_type, distance, sharpness, blade_type, holy_aura):
        super(Excalibur, self).__init__(name, weight, damage, attack_type, distance, sharpness, blade_type)
        self.holy_aura = holy_aura


class ElementalBow(Bow):
    def __init__(self, name, weight, damage, attack_type, distance, quality, arrow_type, element_type):
        super(ElementalBow, self).__init__(name, weight, damage, attack_type, distance, quality, arrow_type)
        self.element_type = element_type


class Gloves(Melee):
    def __init__(self, name, weight, damage, attack_type, distance, sharpness, fit):
        super(Gloves, self).__init__(name, weight, damage, attack_type, distance, sharpness)
        self.fit = fit


# weapons
True_Excalibur = Excalibur("Excalibur", 7.5, 25, "swing/bash/beyblade spin", 7, True, "Long", True)
Shaggys_sword = Sword("Shaggy's Sword", 0, 99999999999999999999999999999999999999999999999, "All", 99999999999999999999,
                      9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
                      "All")
# Bows
Wiebes_Bow = Bow("Wiebe's bow", 0, 99999999999999, "ranged arrow/close bash", 99999999999999, True, "Holy")
Dominics_bow = Bow("Dominic's bow", 9999999999999, .0000000000000001, "ranged arrow/close bash", .00000000000000000001,
                   False, "Flint")

# Elemental bows
Elijahs_bow = ElementalBow("Elijah's bow", 2.5, 97, "Ranged arrow/call of the horses", 9999, True, "Earth", "Horse")
Garfields_bow = ElementalBow("Garfield's bow", .5, 20, "ranged arrow/distraction by lasagna", 200, True, "Fire",
                             "Lasagna")

# Staffs
Yahirs_staff = Staff("Yahir's staff", 1, 50, "magic/bash", 10, True, "Fire")
OogaBoogas_staff = Staff("OogaBooga's Staff", .5, 50, "whack/flying throw", 10, True, "Nature magic(specifically birds)")

# Potions
Health_Potion = Potion("Health potion", 2, 0, "Consumable", 0, 1, "player.health += 20")
LAMB_SAUCE = Potion("Lamb Sauce", 5, 20, "thrown", 20, 1, "breaks down their cells")

# Normal swords
Jordans_sword = Sword("Jordan's sword", 5, 50, "bash/slash/swing", 10, True, "Zweihänder")

# Gloves
Jorges_gloves = Gloves("Jorge's gloves", 2, 20, "close range punch/jab", 2.5, False, True)
Thanos_gloves = Gloves("Thanos gloves", 10, 999999999999999999, "snap/punch", 9999999999999999999, False, True)

# hats
My_Hat = Hats("My hat", .5, 0, "none", 0, 10, "cap")

# cappy
Cappy = Cappy("Cappy", 0, 0, "throw/mind control", 5, 3, "ghost hat", "If air self.bounces = 1 else self.bounces = 2")


# chestpiece
my_chestpiece = ChestPiece("My chestpeice", 5, 0, "None", 0, 20, "iron plate armor")

# Weibe
Weibe = Weibe("Mr.Weibe", "?", 9999999999999999999999999999999, "changes enemy's code", 50, True,
              'MSI GS65 Stealth Thin 15.6-inch')

# Dominic
Dominic = Dominic("Dominic", 20, 50, "bash", 9, False)

# Elijah
Packet_Of_Elijah = Elijah("Packet of Elijah", 12, 500, "Plays game of smash", 200, 6,)

'''
# characters
c1 = Character("Orc1", 100, True_Excalibur, None)
c2 = Character("Shaggy", 9999999999999999999999999999999999999999, Shaggys_sword, None)

c1.attack(c2)
c2.attack(c1)
'''

OMD = Room("Forest", "You Awoke here, there are paths to the East and West", None, "ORD", None, "OLD")
ORD = Room("Forest", "You're surrounded by trees and shrubbery "
                     "there are paths to the North and to the East", "ORM", "OMD", None, None, Shaggys_sword)
OLD = Room("Forest", "You are surrounded by trees and shrubbery, there are paths to the North and West", "OLM", None,
           None, "OMD", Wiebes_Bow)
OLM = Room("Forest", "You're surrounded by trees and shrubbery, there are paths to the North and the south", "OLU",
           None, "OLD", None)
ORM = Room("Forest", "Trees and shrubbery surround you, there are paths to the North and the South,"
                     "There is a small crack in the mossy mountain to the west", "ORU", None, "ORD", "CW1")
ORU = Room("Forest", "You are surrounded by dying trees and shrubbery, there are paths to the West and South", None,
           None, "ORM", "OMU")
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
directions = ["north", "south", "east", "west", "up", "down", "check", "attack"]
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

    # pick up command

    elif "get" in command:
        target_item = command[4:]
        found_item = None
        for thing in player.current_location.items:
            if thing.name == target_item:
                found_item = target_item
        if isinstance(found_item, Item):
            print("You picked up %s" % found_item.name)
            player.inventory.append(found_item)
            for i, item in enumerate(player.current_location.items):
                if item.name == found_item.name:
                    player.current_location.items.pop(i)
        elif found_item is None:
            print("That doesn't exist.")
        else:
            print("You can't pick that up.")
    else:
        print("command not recognized")
