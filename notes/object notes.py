import Special_Random


class WaterGun(object):
    def __init__(self, capacity, distance=30, stock=False):
        # these are things that a water gun should have
        # they should be relevant
        self.capacity = capacity
        self.range = distance
        self.trigger = True # someone's triggered
        self.stock = stock
        self.duration = 5

    def shoot(self, time):
        if self.trigger:
            if self.duration <= 0:
                print("There's no pressure")
            if self.duration < time:
                print("You run out of time after firing for %s seconds", self.duration)
                self.duration = 0
            else:
                print("You shoot for %s seconds" % time)
                self.duration -= time
        else:
            print("there's no pressure")
    def pump(self):
        self.duration = 5
        print("You pump the tank back to full pressure")

mywatergun = WaterGun(5.2, 40, True)
yourwatergun = WaterGun(1.0, 1, False)
Wiebewatergun = WaterGun(9999999999, 99999999999, True)
yahir_water_gun = WaterGun(0.1)

mywatergun.shoot(5)
Wiebewatergun.shoot(8)
yahir_water_gun.shoot(9)

mywatergun.pump()
mywatergun.shoot(5)
print(Special_Random.randomwiebe.special_random())