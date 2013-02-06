from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

input = raw_input("Which do you like best? %s, %s, or %s : " % (first, second, third))

print "You said that you like %s the best." % input
