class Gate(object):
	def enter():
		print "This is the Gate to the park"
		
		command = raw_input("> ")

class Office(object):
	def enter():
		print "This is the Park office"
		
		command = raw_input("> ")
		
class Pond(object):
	def enter():
		print "This is the Pond"
		
		command = raw_input("> ")
		
class IceCream(onject):
	def enter():
		print "This is the Ice Cream stand"
		
		command = raw_input("> ")

class Playground(object):
	def enter():
		print "This is the Playground"
		
		command = raw_input("> ")

class Field(object):
	def enter():
		print "This is the large Field"
		
		command = raw_input("> ")
		
class Zoo(object):
	def enter():
		print "This is the Zoo"
		
		command = raw_input("> ")

class Finish(object):
	def enter():
		print "This is the Finish"
		
		command = raw_input("> ")

# a grid of the map for this game
# the player will only be able to move on grid points with a '1'
# every time the player gives a direction, this grid will be checked
grid = [
	[0, 0, 0, 0, 0],
	[0, 1, 1, 1, 0],
	[0, 1, 1, 1, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0]
]

# this holds the grid position of each location and points to the class
scenes = {
	(3, 2): Gate(),
	(2, 3): Office(),
	(1, 2): Pond(),
	(1, 1): IceCream(),
	(2, 2): Playground(),
	(2, 1): Field(),
	(1, 3): Zoo(),
	(0, 0): Finish()
}