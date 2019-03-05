class bundle_of_sleeping_darts(object):
    def __init__(self, capacity=10, distance=30):
        self.capacity = capacity
        self.range = distance
        self.len = 12.7
        self.needle = True
        self.clean = True
        self.thrown = 0

    def throw(self):
        if self.capacity > 0:
            print("you threw one of your %s darts" % self.capacity)
            self.capacity -= 1
            self.thrown += 1

    def pickup(self):
        if self.capacity < 10:
            self.thrown -= 1
            print("you picked up one of your %s thrown darts" % self.thrown)
            self.capacity += 1