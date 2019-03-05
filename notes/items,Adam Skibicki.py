class Item(object):
    def __init__(self, weight, damage, attack_type, distance):
        self.weight = weight
        self.damage = damage
        self.attack_type = attack_type
        self.distance = distance


class Melee(Item):
    def __init__(self, weight, damage, attack_type, distance):
        super(Melee, self).__init__(weight, damage, attack_type, distance)
        self.sharpness = True


class Consumables(Item):
    def __init__(self, weight, damage, attack_type, distance, ammunition):
        super(Consumables, self).__init__(weight, damage, attack_type, distance)
        self.ammunition = ammunition


class Ranged(Item):
    def __init__(self, weight, damage, attack_type, distance, ammo):
        super(Ranged, self).__init__(weight, damage, attack_type, distance)
        self.ammo = ammo


class Staff(Melee, Ranged):
    def __init__(self, weight, damage, attack_type, distance, sharpness=True, ammo=20):
        Melee.__init__(self, weight, damage, attack_type, distance, sharpness)
        Ranged.__init__(self, weight, damage, attack_type, distance, ammo)
        self.magic_type


class Sword(Melee):
    def __init__(self, weight, damage, attack_type, distance, sharpness):
        super(Sword, self). __init__(weight, damage, attack_type, distance, sharpness)
        self.