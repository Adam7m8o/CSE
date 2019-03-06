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
    def __init__(self, weight, damage, attack_type, distance, ammo):
        super(Ranged, self).__init__(weight, damage, attack_type, distance)
        self.ammo = ammo


class Staff(Melee, Ranged):
    def __init__(self, weight, damage, attack_type, distance, sharpness, ammo=20):
        Melee.__init__(self, weight, damage, attack_type, distance, sharpness)
        Ranged.__init__(self, weight, damage, attack_type, distance, ammo)
        self.magic_type = []


class Sword(Melee):
    def __init__(self, weight, damage, attack_type, distance, sharpness, blade_type):
        super(Sword, self).__init__(weight, damage, attack_type, distance, sharpness)
        self.blade_type = blade_type


class Bow(Ranged):
    def __init__(self, weight, damage, attack_type, distance, ammo, arrow_type):
        super(Bow, self).__init__(weight, damage, attack_type, distance, ammo)
        self.arrow_type = arrow_type


class Potion(Consumables):
    def __init__(self, weight, damage, attack_type, distance, ammunition, potion_effect):
        super(Potion, self).__init__(weight, damage, attack_type, distance, ammunition)
        self.potion_effect = potion_effect


class Excalibur(Sword):
    def __init__(self, weight, damage, attack_type, distance, sharpness, blade_type):
        super(Excalibur, self).__init__(weight, damage, attack_type, distance, sharpness, blade_type)
        self.holy_aura = True


Excalibur = Excalibur("7.5 pounds", "25", "swing/bash", "7 feet", True, "Long")
True_Excalibur = Excalibur("7 pounds", "50", "swing")
