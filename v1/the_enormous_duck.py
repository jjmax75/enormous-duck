"""
A text based adventure game built with Python by John Behan
May 2014, version 1
For my beautiful daughter Khetmani
I love you very much
"""

from os import system, name as os_name
from sys import exit

#variables to store player information
name = ""
gender = ""
gender_subject = ""
gender_possessive = ""
gender_object = ""
turns = 0
parent = ""
parent_name = ""
parent_subject = ""
inventory = []
age = 0
clear = ""
visited = {'gate':0, 'playground':0, 'exercise':0, 'ice_cream':0, 'pond':0,\
'petting_zoo':0}
naughty = {'playground':0, 'pond':0, 'petting_zoo':0, 'ice_cream_stand':0}
talk_npc = {'plane':0}
task_1 = {'completed':0, 'first':0, 'second':0, 'third':0, 'reward':0}

running = os_name
	
if running == "nt":
	clear = "cls"
	system(clear)
elif running == "posix":
	clear = "clear"
	system(clear)
else:
	print "Unknown system"

def intro():
	global name, gender, gender_subject, gender_object, age, parent, \
	parent_subject, parent_name, gender_possessive
	
	print "Hello there, welcome to our little adventure game. "
	print "What's your name?"
	name = raw_input("> ").capitalize()
	
	print "Hi", name
	print "That's a very nice name"
	
	while gender == "":
		print "Are you a boy or a girl?"
		answer = raw_input("> ")
	
		if "b" in answer:
			gender = "boy"
			gender_subject = "he"
			gender_possessive = "his"
			gender_object = "him"
		elif "g" in answer:
			gender = "girl"
			gender_subject = "she"
			gender_possessive = "her"
			gender_object = "her"
		else:
			gender = ""

	global age
	while age == 0:
		print "How old are you?"
		answer = raw_input("> ")	
		
		if answer.isdigit():
			age = answer
		else:
			print "You need to enter a number for your age"
			print "anything greater than 0"	
				
	if age <= 6:
		print age, "is quite young. If you need help with this game"
		print "you can ask your parents or another grown up"
	else:
		print "You're a big", gender, "now.", age, "is the perfect age to "
		print "play this adventure game."
	
	while parent == "":
		print "Last question! Who takes you to the park usually? \
		\nYour mum or your dad?"
		answer = raw_input("> ").upper()
		
		if "M" in answer:
			parent = "Mum"
			parent_subject = "her"
		elif "D" in answer:
			parent = "Dad"
			parent_subject = "his"
		else:
			parent = ""
	
	print "OK, I lied a little!"
	print "One more question, what's your {}'s name?".format(parent)
	parent_name = raw_input("> ").capitalize()
	
	print "Great! Let's get started"
	
	gate()
	
def gate():
	global visited
	system(clear)
	
	print "The Park Gate"
	if visited['gate'] == 0:
		print "One day a little {0} named {1} went to the park to play.\n" \
		"It was a beautiful December day. The sun was in the sky but it\n" \
		"wasn't	too hot because of a nice fresh breeze. {1} was in a very\n" \
		"good mood, {2} always liked going to the park. {1} was a big {0}\n" \
		"now, {7} years old, and {3} {6} let {5} run around and\n" \
		"explore the park on {3} own. {4}, {1}'s {6},  would wait for {5} at\n"\
		"the exercise area. {4} was going to do some fitness training while {1}\n" \
		"had fun exploring the park.".format(gender, name, gender_subject, \
		gender_possessive, parent_name, gender_object, parent, age)
		
		visited['gate'] = 1
		
	print "You are standing at the Park Gate."
	print "You can GO NORTH to the Playground."
	print "You can GO EAST to the Exercise Area."
	print "You can GO SOUTH to the Road"
	print "You can GO WEST to the Car Park"
	print "What do you want to do?"
	answer = raw_input("> ").lower()
	instruction(answer, gate)
	
def playground():
	global visited
	global naughty
	
	print "The Playground"
	print "This is the playground area of the park. There are lots of kids\n"\
	"here enjoying the swings, roundabouts and slides. Some are playing in\n"\
	"the sandpit."
	
	if naughty['playground'] == 0:
		print "Some NAUGHTY KIDS are misbehaving pretty badly. They are making a\n"\
		"lot of noise and running into other kids there. Some are even\n"\
		"using remote control planes that they fly really low around the\n"\
		"heads of the adults and other kids that are in the playground.\n"\
		"These KIDS are so NAUGHTY and don't care who they annoy"
	
	print "You can GO NORTH to the Pond."
	print "You can GO EAST to the Park Keeper's Office"
	print "You can GO SOUTH to the Park Gate"
	print "You can GO WEST to The Large Field"
	print "What do you want to do?"
	answer = raw_input("> ").lower()
	visited['playground'] = 1
	instruction(answer, playground)

def exercise():
	print "The Exercise Area"
	exit()
	
def field():
	print "The Large Field"
	exit()

def road(location):
	print "That's the way to the road, you can't go there"
	print "It's not safe"
	print "Hit the enter key to continue"
	raw_input()
	location()
	
def car_park(location):
	print "That's the way to the car park, you can't go there"
	print "It's not safe"
	print "Hit the enter key to continue"
	raw_input()
	location()

def pond():
	global visited
	
	print "The Pond"
	print "You are at the pond. The sun is sparkling on the water and you\n"\
	"can see many fish swimming under the surface. There are many, many\n"\
	"ducks paddling around in the water or waddling on the side."
	
	if visited['pond'] == 0:
		meet_duck_pt1()
	else:
		print "From here you can\n"\
		"GO EAST to The Petting Zoo\n"\
		"GO SOUTH to The Playground\n"\
		"GO WEST to The Ice Cream Stand\n"
		answer = raw_input("> ").lower()
		instruction(answer, pond)
	
def meet_duck_pt1():
	print "You hear a rustle from behind a tree!\n\n"
	print "What do you do?"
	print "RUN away or LOOK behind the tree"
	answer = raw_input("> ").lower()
	instruction(answer, meet_duck_pt1)

def meet_duck_pt2():
	print "The Enormous Duck steps out from behind the tree. The duck is at\n"\
	"least as big as your {0} but with all the features of a duck. He has a\n"\
	"big yellow duck beak, green, white, brown and black feathers, and two\n"\
	"great big duck feet.\n\n".format(parent)
	print "He quacks at you \"Hello {0}, I've been waiting to meet you for\n"\
	"so long now. I've seen you at the park many times before but I was\n"\
	"always too shy to say hello. You seem like a very kind person and I\n"\
	"hope you can help me with something. Will you help me please?\""\
	.format(name)
	answer = raw_input("> ").lower()
	instruction(answer, meet_duck_pt2)
	
def duck_story():
	global visited
	
	print "\"Great\" The Enormous Duck starts his story with a big QUACK!\n"\
	"\"Quack, quack, well you see my fellow ducks and I live in\n"\
	"this park, it is our home, but a group of children have been making\n"\
	"life very hard for us lately. They throw litter on the ground,\n"\
	"which dirties the water and the area around here. This makes me\n"\
	"very sad. They also make so much noise that often I have a very bad\n"\
	"headache and I must take duck medicine to feel better. I don't\n"\
	"like to take medicine. Sometimes they come here and make these\n"\
	"things buzz through the air, the racket is awful, buzz buzz buzz\n"\
	"BUZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\n"\
	"all day long. I would like you to go to these children and get\n"\
	"them to stop causing problems for us.\"\n\n"
	print "\"You're a very kind person but I also think you are very\n"\
	"strong and clever. I know you can do this for me.#\n\n\""
	print "What a peculiar meeting but you feel so excited.\n"\
	"The Enormous Duck seems really friendly and you are so sad to hear\n"\
	"about the problems he is having.\n"
	"You've made your mind up, you'll figure out how to fix these"
	"problems for The Enormous Duck.\n You say \"OK, let's get started'\""\
	"\"Great!\" says The Enormous Duck, \"I knew you would help me\n\""\
	"The Enormous Duck looks very happy and that makes you feel very\n"\
	"happy too. \"Remember that if you need any help you can always\n"\
	"come to me at any time or you can go and see the Park Keeper or\n"\
	"or your {}. OK, let's get started!\"\n".format(parent)
	print "There are three places in the park where these kids are being\n"\
	"a nuisance.\n"\
	"EAST at The Petting Zoo\n"\
	"SOUTH at The Playground\n"\
	"WEST at The Ice Cream Stand\n"\
	"Go to each of these locations and complete some tasks to solve the\n"\
	"there.\n"\
	"If you need any help you can always come back here to talk with me\n"\
	"Or you could go to the Park Keeper's office which is near The Playground\n"\
	"Or you may be able to get some help from your {} at The Exercise Area"\
	.format(parent)
	print "Where do you want to go next?\n"\
	"EAST, SOUTH or WEST?"
	answer = raw_input("> ").lower()
	visited['pond'] = 1
	instruction(answer, pond)

def petting_zoo():
	print "The Petting Zoo"
	exit()

def ice_cream():
	print "The Ice Cream Stand"
	exit()

def park_keeper():
	print "The Park Keeper's Office"
	exit()
	
def task_1():
	print "This is task 1"
	exit()

def cannot_go(location):
	print "I'm sorry you cannot go that way"
	print "Hit the enter key to continue"
	raw_input()
	location()

def dont_understand(command, location):
	print "I'm sorry I don't understand: {}".format(command)
	print "Hit the enter key to continue"
	raw_input()
	location()
	
def online_help(location):
	print "Help for the {} location".format(location.__name__)
	print "Hit the enter key to continue"
	raw_input()
	location()
	
def instruction(command, location):
	
	if "help" in command:
		online_help(location)
		
	if "repeat" in command:
		location()
		
	if location.__name__ == "gate":
		if "north" in command:
			playground()
		elif "east" in command:
			exercise()
		elif "south" in command:
			road(location)
		elif "west" in command:
			car_park(location)
		else:
			dont_understand(command, location)
	
	if location.__name__ == "playground":
		if "north" in command:
			pond()
		elif "east" in command:
			park_keeper()
		elif "south" in command:
			gate()
		elif "west" in command:
			field()
		elif "talk" in command:
			talk("playground", command)
		else:
			dont_understand(command, location)
		
	if location.__name__ == "meet_duck_pt1":
		if "run" in command:
			print "You turn to run away. You hear a voice saying:\n"\
			"\"Please don't be afraid!\"\n"\
			"\"I won't hurt you\"\n"\
			"You turn around to see an Enormous Duck!"
			meet_duck_pt2()
		elif "look" in command:
			print "You approach the tree slowly....\n"\
			"You peek around the tree and see.....\n"\
			"An Enormous Duck!"
			meet_duck_pt2()
		else:
			dont_understand(command, location)
			
	if location.__name__ == "meet_duck_pt2":
		if "y" in command:
			duck_story()
		elif "n" in command:
			print "The Enormous Duck looks very sad and disappointed.\n"
			print "He asks again - \"Please, can you help me?\""
			answer = raw_input("> ").lower()
			if "y" in answer:
				duck_story()
			elif "n" in answer:
				print "\"I'm sad to hear that\"\n"\
				"Take care I hope you have a happy day\"\n"\
				"With that, The Enormous Duck waddles away with one loud QUACK!\n"\
				"You go to the exercise area and meet your {0}"\
				"As you go home that day, and for many many days after you\n"\
				"think about The Enormous Duck and his strange request.\n"\
				"You also wonder about what might have happened had you said\n"\
				"yes and helped the poor creature put that day".format(parent)
				exit()
			else:
				dont_understand(answer, location)
	
	if location.__name__ == "pond":
		if "east" in command:
			petting_zoo()
		elif "south" in command:
			playground()
		elif "west" in command:
			ice_cream()
		elif "north" in command:
			cannot_go(location)
		else:
			dont_understand(answer, location)

def talk(location, command):
	global talk_npc
	
	if location == "playground":
		if ("naughty" in command or "kids" in command) and talk_npc['plane'] == 0:
			print "You talk to the naughty kids\n"\
			"{0} - \"Why are you playing with the remote control planes here?\"\n"\
			"Naughty Kid(NK) - \"Because it's fun!\"\n"\
			"{0} - \"But don't you see that there are other people here and\n"\
			"they don't like what you are doing?\"\n"\
			"NK - \"Yeah....but....where are we supposed to play if not here?\""\
			.format(name)
			print "You think about this.\n"\
			"Where are these kids supposed to play if they can't play in the\n"\
			"playground? They don't seem that bad really, they'd probably\n"\
			"play somewhere else if they could. Maybe if you find somewhere\n"\
			"else for them to play they'd move there and not cause any more\n"\
			"problems."
			talk_npc['plane'] = 1
			playground()
		elif "naughty" or "kids" in command and talk_npc['plane'] == 1:
			print "NK - \"Hi, good to see you again, did you find anywhere\n"\
			"else for us to play yet?\""
			playground()
		else:
			print "I can't talk to that"
			playground()
	
intro()