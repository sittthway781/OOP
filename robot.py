class Robot:
	"""Represents a robot,with a name."""

	population = 0

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
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

droid3 = Robot("Q35")
droid3.say_hi()
Robot.how_many()

droid4 = Robot("h32")
droid4.say_hi()
Robot.how_many()


print ("\nRobots can do some work here.\n")

print ("Robots have finish their work. so let's destory them")
droid1.die()
droid2.die()
droid3.die()
droid4.die()

Robot.how_many()