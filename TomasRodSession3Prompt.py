'''3) Session 3 Prompt: Write a Python program that defines
a function f(x) that returns x**3 + 8. In the main function of the program,
call f(x) with x = 9 and print the result.  Use an if statement that executes 
if the result is larger than 27 and prints “YAY!”. '''

import numpy as np 

def f(x): 				#defining a function f(x) that returns x**3 + 8
	return x**3 + 8

def main():
	x = 9
	print(f(x))
	if(x**3 + 8 > 27):
		print("YAY!")


if __name__ == '__main__':
	main()

