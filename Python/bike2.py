from __future__ import print_function
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        self.miles += 10
        return self
    def reverse(self):
        if self.miles <= 5:
            self.miles = 0
            return self
        else:
            self.miles -= 5
            return self
    def displayinfo(self):
        print("Price is ", self.price, "Max Speed is ",
        self.max_speed, "Total Miles are ", self.miles)
        return self
bike1 = Bike(200, "20mph")
bike1.ride().ride().ride().reverse().displayinfo();
bike2 = Bike(400, "25mph")
bike2.ride().ride().reverse().reverse().displayinfo();
bike3 = Bike(300, "15mph")
bike3.ride().reverse().reverse().displayinfo();
