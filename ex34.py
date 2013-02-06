animals = [ 'bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus' ]

print animals
score = 2
print float( 2/8 )

print "Your score is %d of 8, or %d percent." % ( score, (score/8)*100 )

print "The animal at 1 is a . . . "
animal_input = raw_input( "> " )
print "You said the animal at 1 is a " + animal_input
if animal_input == animals[ 1 ]:
	score = 1
print "The correct answer is '%s'.\n" % animals[ 1 ]

print "The 3rd animal is a  . . . "
animal_input = raw_input( "> " )
print "You said the 3rd animal is a " + animal_input
if animal_input == animals[ 2 ]:
	score += 1
print "The correct answer is '%s'.\n" % animals[ 2 ]

print "The 1st animal is a  . . . "
animal_input = raw_input( "> " )
print "You said the 1st animal is a " + animal_input
if animal_input == animals[ 0 ]:
	score += 1
print "The correct answer is '%s'.\n" % animals[ 0 ]

print "The animal at 3 is a  . . . "
animal_input = raw_input( "> " )
print "You said the animal at 3 is a " + animal_input
if animal_input == animals[ 3 ]:
	score += 1
print "The correct answer is '%s'.\n" % animals[ 3 ]

print "The 5th animal is a  . . . "
animal_input = raw_input( "> " )
print "You said the 5th animal is a " + animal_input
if animal_input == animals[ 4 ]:
	score += 1
print "The correct answer is '%s'.\n" % animals[ 4 ]

print "The animal at 2 is a  . . . "
animal_input = raw_input( "> " )
print "You said the animal at 2 is a " + animal_input
if animal_input == animals[ 2 ]:
	score += 1
print "The correct answer is '%s'.\n" % animals[ 2 ]

print "The 6th animal is a  . . . "
animal_input = raw_input( "> " )
print "You said the 6th animal is a " + animal_input
if animal_input == animals[ 1 ]:
	score += 1
print "The correct answer is '%s'.\n" % animals[ 5 ]

print "The animal at 4 is a  . . . "
animal_input = raw_input( "> " )
print "You said the animal at 4 is a " + animal_input
if animal_input == animals[ 1 ]:
	score += 1
print "The correct answer is '%s'.\n" % animals[ 4 ]

print "Your score is %d of 8, or %d percent." % ( score, (score/8)*100 )