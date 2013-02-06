from sys import argv

script, filename = argv

# Wouldn't be good in a real script to have dialogue be like this, 
# since there's no indication to noobs that if the file does not exist
# it will be created.
# Also, there's no confirm that things have happened.
# Also, it's not clear that 'erase' here means clearing the contents, 
# not deleting the file
print """We're going to erase %r." % filename
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN."""

raw_input("?")

print "Opening the file . . ."
target = open(filename, 'w')

# Better text would be to talk about clearing contents.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Original Method
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# My Condensed Method
# Probably even better to put it into an array or dictionary and iterate
target.write(("%s\n%s\n%s\n") % (line1,line2,line3))

print ("And finally we close it.")
target.close	30db