the_count = [ 1, 2, 3, 4, 5 ]
fruits = [ 'apples', 'oranges', 'pears', 'apricots' ]
change = [ 1, 'pennies', 2, 'dimes', 3, 'quarters' ]

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also notice we can go through mixed lists, too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists; first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# me: note that the second item in the range function implies stoppage before reaching it
for i in range( 0, 6 ):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append( i )

# now we can print out that list, too
for i in elements:
	print "Element was: %d" % i


# getting cray cray with it

print "The list named 'elements' has %d items in it." % len(elements)
print "The second item in that list is %r" % elements[1]
# set a list item value
elements[1] = 1024
print "The second item in that list is now %r" % elements[1]
# change the data type of an item's value
elements[1] = "The quick brown fox jumps over the lazy red dog."
print "The second item in that list is now %r" % elements[1]
# change the data type of an item's value to a list of letters
elements[1] = sorted( list( "the quick brown fox jumps over the lazy red dog." ) )
print "The second item in that list is now %r" % elements[1]

# get content from a file
myfile = open( "mathematical_operators.txt" )
filewords = sorted( myfile.read().split( ' ' ) )
for i in filewords:
	print i
