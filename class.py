class Person:
	pass #an empty block 

p = Person()
print(p)

#Methods

class Person:
	def say_hi(self):
		print ('hello, how are you?')

p = Person()
p.say_hi()

#__init__method

class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print ('Hello, my name is ', self.name)

p = Person("Swaroop")
p.say_hi()

#dog = dog("Nmae")
 >>> class gg:
...     def __init__(self,name,age,code,gender):
...             self.name = name
...             self.age = age
...             self.code  = code
...             self.gender   = gender
...     def sayname(self):
...             print ("hello, my name is ", self.name)
...     def sayage(self):
...             print ("hello, my age is ", self.age)
...     def saycode(self):
...             print ("helllo, my code is", self.code)
...     def saygender(self):
...             print ("hello, i'm ",self.gender)
...
>>> p = gg ("sitt thway", 20 , 1999, "male")
>>> p.sayage()
hello, my age is  20
>>> p.saygender()
hello, i'm  male

class Robot:
	"""Represents a robot,with a name."""

	populatoin = 0

	def __init__(self,name):
		"""Initializes the data."""

		self.name = name
		print ("(Initializing{})".format(self.name))

		Robot.population += 1

	def die(self):
		"""I am dying."""

		print ("{} is being destroyed!".format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print ("{} was the last one.".format(self.name))
		else:
			print ("There are stilll {:d} robots working.".format(Robot.population))
	def say_hi(self):
		"""Greeting by the robot.
		Yeah, they can do that."""

		print ("greetings, my sisters call me {}.".format(self.name))
	@classmethod
	def how_many(cls):
		"""Prints the current population."""
		print ("we have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

droid3 = Robot("Q35")
droid3.say_hi()
Robot.how_many()

print ("\nRobots can do some work here.\n")

print ("Robots have finish their work. so let's destory them")
droid1.die()
droid2.die()
droid3.die()

Robot.how_many()
