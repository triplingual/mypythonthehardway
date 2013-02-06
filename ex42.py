## Animal is-a object (yes, sort of confusing); look at the extra credit.
class Animal( object ):
	pass

## Dog is-a Animal
class Dog( Animal ):
	def __init__( self, name ):
		## Dog has-a property called name
		self.name = name

## Cat is-a Animal
class Cat( Animal ):
	def __init__( self, name ):
		## Cat has-a property called name
		self.name = name

## Person is-a object (which is odd, because people are animals)
class Person( object ):
	def __init__( self, name ):
		## Person has-a property called name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee( Person ):
	def __init__( self, name, salary ):
		## Employee, as a Person, has a property called name
		super( Employee, self ).__init__( name )
		## Employee has-a property called salary that not all Persons have
		self.salary = salary

## Fish is-a object
class Fish( object ):
	pass

## Salmon is-a Fish
class Salmon( Fish ):
	pass

## Halibut is-a Fish
class Halibut( Fish ):
	pass

## rover is-a Dog
rover = Dog( "Rover" )

## satan is-a Cat
satan = Cat( "Satan" )

## mary is-a Person
mary = Person( "Mary" )

## mary has-a property called pet, which is set to satan
mary.pet = satan

## frank is an Employee with a salary of 120000
frank = Employee( "Frank", 120000 )

## frank has-a property called pet, which is set to rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()