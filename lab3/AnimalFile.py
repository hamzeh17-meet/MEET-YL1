class Animal(object):
	def __init__(self,sound,name,age):
		self.sound=sound
		self.name=name
		self.age=age

	def eat(self,food):
		print("the animal is eating " + food)
	
