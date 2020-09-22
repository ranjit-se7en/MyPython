##__init__ is a constructor

class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("kenwood", 99)
print(kenwood.make)
print(kenwood.price)


kenwood.price = 1222
print(kenwood.price)

hamilton = Kettle("hamilton", 1232)
print(hamilton.make)
print(hamilton.price)

print("Models {0} = {1}, {2} = {3}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
#hamilton.switch_on()
print(hamilton.on)

#Kettle.switch_on(hamilton)
print(hamilton.on)

print("*" * 80)

kenwood.power = 22.3
print(kenwood.power)

print(hamilton.on)
Kettle.switch_on(hamilton)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

Kettle.power_source = "charcoal"

print()

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print()

print(Kettle.__dict__)
print(hamilton.__dict__)
print(kenwood.__dict__)



