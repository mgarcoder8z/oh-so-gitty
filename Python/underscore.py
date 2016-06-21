class MathClass(object):
    # all methods in a class receive self as an argument
    def filter(self, a):
        c = []
        for i in a:
            if i % 2 == 0:
                c.append(i)
        print(c)
    def map(self, a):
        c = []
        for i in a:
            c.append(i * 5)
        print(c)
    def sum(x, y):
        sum = x + y
        print(sum)
    def reduce(self, a):
        sum = 0
        for i in a:
            sum = sum + i
        print(sum)
    def find(self, a):
        for i in a:
            if i % 2 == 0:
                print(i)
                break
    def reject(self, prompt):
        try:
            value = int(raw_input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            return reject(prompt)
        if value < 0:
            print("Sorry, your response must not be negative.")
            return reject(prompt)
        else:
            return value
_ = MathClass()  # create instance of MathClass
_.filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # call filter method and pass in list of int values as argument
_.map([1,2,3,4,5,6])
_.reduce([1,2,3,4,5,6,7,8,9,10])
_.find([1,2,3,4,5])
_.reject("Please enter your age: ")
