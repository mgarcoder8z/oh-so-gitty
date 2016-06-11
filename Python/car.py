from __future__ import print_function
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def tax(self):
        if self.price > 10000:
            self.tax = 0.15
            return (self.tax)
        else:
            self.tax = 0.12
            return (self.tax)
    def displayall(self):
        print("Price: ",self.price,"\n","Speed: ",
              self.speed,"\n","Fuel: ",self.fuel,"\n","Mileage: ",self.mileage,"\n","Tax: ",self.tax,"\n")
Nova = Car(2000, "60mph", "Full", "15mpg")
Nova.tax()
Nova.displayall()
Civic = Car(2000, "70mph", "Not Full", "10mpg")
Civic.tax()
Civic.displayall()
Beetle = Car(30000, "80mph", "Kind of Full", "20mpg")
Beetle.tax()
Beetle.displayall()
Lexus = Car(60000, "100mph", "Full", "25mpg")
Lexus.tax()
Lexus.displayall()
BMW = Car(100000, "105mph", "Full", "20mpg")
BMW.tax()
BMW.displayall()
