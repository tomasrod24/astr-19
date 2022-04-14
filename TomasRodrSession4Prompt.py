''' 
Write a Python program that declares a class describing your favorite animal. Have the data members of the class 
represent the following physical parameters of the animal: length of the arms (float), length of the legs (float), 
number of eyes (int), does it have a tail? (bool), is it furry? (bool). 
Write an initialization function that sets the values of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
'''

#import sys
class favAnimal:
	def print(self):
		print(f"Length of the arms = {self.length_arms}") #float
		print(f"Length of the legs = {self.length_legs}") #float
		print(f"Number of eyes = {self.num_eyes}")        #int
		print(f"Does it have a tail? {self.tailYoN}")     #bool
		print(f"Is it furry? {self.furryYoN}")            #bool

	def __init__(self, lArms = 15.0, lLegs = 20.0, numEyes = 2, tail = True, furry = True):
		self.length_arms = lArms
		self.length_legs = lLegs
		self.num_eyes = numEyes
		self.tailYoN = tail
		self.furryYoN = furry

def main():

	lArms = 15.0
	lLegs = 20.0
	numEyes = 2
	tail = True
	furry = True

	if(tail & furry == True):
		tail = "Yes"
		furry = "Yes"
	else:
		tail = "No"
		furry = "No"


	our_Animal = favAnimal(lArms = lArms, lLegs = lLegs, numEyes = numEyes, tail = tail, furry = furry)

	our_Animal.print()

if __name__ == '__main__':
	main()


