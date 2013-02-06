my_name = 'Zed A. Shaw'
my_age = 35 # not a lie

# Imperial Units
my_height = 74 # inches
my_weight = 180 # Lbs

# Metric units
centimeters_per_inch = 2.54
centimeters_per_meter = 100
my_height_metric = my_height * centimeters_per_inch / centimeters_per_meter
my_weight_metric = my_weight / 2.2

my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
# print "He's %d inches tall." % my_height
print "He's %s meters tall." % my_height_metric
print "He's %d kilos heavy." % my_weight_metric
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % ( my_eyes, my_hair )
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky; try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
