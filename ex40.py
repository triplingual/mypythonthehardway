class Song( object ):
	def __init__( self, lyrics ):
		self.lyrics = lyrics

	def sing_me_a_song( self ):
		for line in self.lyrics:
			print line

happy_bday = Song( [ "Happy birthday to you",
			"I don't want to get sued",
			"So I'll stop right there" ] )

bulls_on_parade = Song( [ "They rally round the family",
			"With pockets full of shells" ] )

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()



# my mods

class Accompaniment( Song ):
	def __init__( self, instrument, lyrics ):
		self.instrument = instrument
		self.lyrics = lyrics

	def sing_me_a_song( self ):
		for line in self.lyrics:
			print self.instrument + ": " + line

happy2 = Accompaniment( "guitar", [ "Happy birthday to you", "You live in a zoo" ] )
porter = Accompaniment( "piano", [ "Miss Otis regrets she's unable to lunch today", "Love for sale" ] )

happy2.sing_me_a_song()

porter.sing_me_a_song()