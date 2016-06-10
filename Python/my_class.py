from __future__ import print_function
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        self.miles += 10
    def reverse(self):
        if self.miles <= 5:
            self.miles = 0
        else:
            self.miles -= 5
    def displayinfo(self):
        print("Price is ", self.price, "Max Speed is ",
              self.max_speed, "Total Miles are ", self.miles)
bike1 = Bike(200, "20mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()
bike2 = Bike(400, "25mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()
bike3 = Bike(100, "15mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()
