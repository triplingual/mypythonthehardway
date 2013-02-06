# Assign values to initial variables
x = "There are %d types of people." % 10 # Is 10 treated as a string here?
binary = "binary" 
do_not = "don't"
# First interpolation of simple strings into a slightly less simple string
y = "Those who know %s and those who %s." % (binary, do_not)

# First printout of variable values
print x
print y

# Add some air
print

# Printout repeats of previous
print "I said: %r." % x
print "I also said: '%s'." % y

# Add some air
print

# Printout meta-commentary, illustrate deferred interpolation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# Add some air
print

# Illustration of simple string concatenation
w = "This is the left side of . . . "
e = "a string with a right side."

print w + e
