class Item(object):
    def __init__(self, weight, damage, attack_type, distance):
        self.weight = weight
        self.damage = damage
        self.attack_type = attack_type
        self.distance = distance


class Melee(Item):
    def __init__(self, weight, damage, attack_type, distance, sharpness):
        super(Melee, self).__init__(weight, damage, attack_type, distance)
        self.sharpness = sharpness


class Consumables(Item):
    def __init__(self, weight, damage, attack_type, distance, ammunition):
        super(Consumables, self).__init__(weight, damage, attack_type, distance)
        self.ammunition = ammunition


class Ranged(Item):
    def __init__(self, weight, damage, attack_type, distance, quality):
        super(Ranged, self).__init__(weight, damage, attack_type, distance)
        self.quality = quality


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


class Elemental_Bow(Bow):
    def __init__(self, weight, damage, attack_type, distance, quality, arrow_type, element_type):
        super(Elemental_Bow, self).__init__(weight, damage, attack_type, distance, quality, arrow_type)
        self.element_type = element_type



# Excaliburs
True_Excalibur = Excalibur(7.5, 25, "swing/bash/circular lazer", 7, True, "Long", True)
Excalibur = Excalibur(7.5, 25, "swing/bash", 7, True, "Long", False)

# Bows
Wiebes_Bow = Bow(0, 99999999999999, "ranged arrow/close bash", 99999999999999, True, "Holy")
Dominics_bow = Bow(9999999999999, .0000000000000001, "ranged arrow/close bash", .00000000000000000001, False, "Flint")

# Elemental bows
Elijahs_bow = Elemental_Bow(2.5, 97, "Ranged arrow/call of the horses", 9999, True, "Earth", "Horse")
Garfields_bow = Elemental_Bow(.5, 20, "ranged arrow/distraction by lasagna", 200, True, "Fire", "Lasagna")

# Staffs
yahirs_staff = Staff(1, 15, "slap/thrust", 6, False, True, None)
OogaBoogas_staff = Staff(.5, 50, "whack/flying throw", 10, False, True, "Nature magic(specifically birds)")

# Potions
Health_Potion = Potion(2, 0, "Consumable", 0, 1, "player.health += 20")
Acidic_Potion = Potion(5, 20, "thrown", 20, 1, "breaks down their cells")

#