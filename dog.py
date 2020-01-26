class dog:
	def __init__(self,name,color,owner,age):
		self.name = name
        self.color = color
        self.owner = owner
        self.age = age
    def name(self):
        print ("Dog's name is", self.name)
    def color(self):
       	print ("Dog's color is", self.color)
    def owner(self):
       	print ("Dog's owner is", self.owner)
    def age(self):
      	print ("dog's age is ", self.age)

dog = dog("aung net", "black", "bobo", 5)

