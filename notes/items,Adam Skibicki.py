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


# Excaliburs
True_Excalibur = Excalibur(7.5, 25, "swing/bash/circular lazer", 7, True, "Long", True)
Excalibur = Excalibur(7.5, 25, "swing/bash", 7, True, "Long", False)

# Bows
Wiebes_Bow = Bow(0, 99999999999999, "ranged arrow/close bash", 99999999999999, True, "Holy")
Dominics_bow = Bow(9999999999999, .0000000000000001, "ranged arrow/close bash", .00000000000000000001, False, "Flint")

# Elemental bows
Elijahs_bow = ElementalBow(2.5, 97, "Ranged arrow/call of the horses", 9999, True, "Earth", "Horse")
Garfields_bow = ElementalBow(.5, 20, "ranged arrow/distraction by lasagna", 200, True, "Fire", "Lasagna")

# Staffs
yahirs_staff = Staff(1, 15, "slap/thrust", 6, False, True, None)
OogaBoogas_staff = Staff(.5, 50, "whack/flying throw", 10, False, True, "Nature magic(specifically birds)")

# Potions
Health_Potion = Potion(2, 0, "Consumable", 0, 1, "player.health += 20")
Acidic_Potion = Potion(5, 20, "thrown", 20, 1, "breaks down their cells")

# Normal swords
Jordans_sword = Sword(5, 50, "bash/slash/swing", 10, True, "Zweihänder")
Shaggys_sword = Sword(0, 99999999999999999999999999999999999999999999999, "All", 99999999999999999999999999999999999999,
                      9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
                      "All")

# Gloves
Jorges_gloves = Gloves(2, 20, "close range punch/jab", 2.5, False, True)
Thanos_gloves = Gloves(10, 999999999999999999, "snap/punch", 9999999999999999999, False, True)
Wibes_gloves = Gloves(-2, -20, "you hurt yourself and they feel the pain", -20, True, False)

# hats
My_Hat = Hats(.5, 0, "none", 0, 10, "cap")

# cappy
Cappy = Cappy(0, 0, "throw/mind control", 5, 3, "ghost hat", "If air self.bounces = 1 else self.bounces = 2")

# chestpiece
my_chestpiece = ChestPiece(5, 0, "None", 0, 20, "iron plate armor")

# Weibe
Weibe = Weibe("?", 999999999, "changes enemys code", True, "")

# Dominic
Dominic = Dominic(20, 50, "bash", 9, False)