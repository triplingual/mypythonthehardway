ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there aren't 10 things in that list. Let's fix that."

stuff = ten_things.split( ' ' )
more_stuff = [ "Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy" ]

while len( stuff ) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append( next_one )
	print "There's %d items now." % len( stuff )

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[ 1 ]
print stuff[ -1 ] # whoa! fancy
print stuff.pop()
print ' '.join( stuff ) # what? cool!
print '#'.join( stuff[ 3:5 ] ) # super stellar!

"""
Using Zed's example -- 

' '.join(things) isn't simply "Join things with ' ' between them."
It is (or seems to be to me now):
	Create an instance of class String with ' ' as its content
	Execute the join function of the String class, passing the ' ' string and the 'things' list as the args
	The join function takes each member of the list arg and concatenates it with first the initial arg (' ', in this case) and the eventual output String (that begins as an empty string), excepting the first list member, which gets concatenated directly with the default string. Alternately, you could say that each member is concatenated with the output string in front and the initial arg at the end.
"""