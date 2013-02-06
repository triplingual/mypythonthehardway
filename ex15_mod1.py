from sys import argv

script, filename = argv

txt = open(filename)

#print "Here's your file %r:" % filename
print "Here's your file %r:" % txt.name
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

var_lots = 'Lots and lots of fun to have in here.'
print "There are %s lines in the file." % len(txt_again.readlines())
txt_again.seek(0)
print "There are %s instances of the phrase 'Lots and lots of fun to have in here.' in this file. " % txt_again.readlines().count(var_lots)
txt_again.seek(0)
print txt_again.read()
