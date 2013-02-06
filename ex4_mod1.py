# Number of cars owned
cars = 100

# Seats per car
space_in_a_car = 4.0

# Available drivers
drivers = 30

# Known passengers
passengers = 90

# Cars without drivers
cars_not_driven = cars - drivers

# Cars with drivers
cars_driven = drivers

# Number of people we can drive safely
carpool_capacity = cars_driven * space_in_a_car

# How many people need to be in each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
