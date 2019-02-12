class WaterGun(object):
    def __init__(self, capacity, distance, stock):
        # these are things that a water gun should have
        # they should be relevant
        self.capacity = capacity
        self.range = distance
        self.trigger = True #someone's triggered
        self.stock = stock
        self.duration = 5

    def shoot(self, time):
        if self.trigger:
            if self.duration <= 0:
                print("There's no pressure")
            if self.duration < time:
                print("YOu run out of time after firing for %s seconds", self.duration)
                self.duration = 0
            else:
                print("You shoot for %s seconds" % time)
                self.duration -= time
        else:
            print("there's no pressure")

mywatergun = WaterGun(5.2, 40, True)
yourwatergun = WaterGun(1.0, 1, False)
Wiebewatergun = WaterGun(999999999999, 99999999999, True)