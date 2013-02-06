separator = '-' * 10

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR', 
	'Florida': 'FL', 
	'California': 'CA', 
	'New York': 'NY', 
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco', 
	'MI': 'Detroit', 
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print separator
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print out some states
print separator
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the states then cities dicts
print separator
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print separator
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print separator
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time 
print separator
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

# safely get an abbreviation by state that might not be there
print separator
state = states.get('Texas', None)
if not state:
	print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city