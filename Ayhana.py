from random import randint
import math

a = math.sqrt(121)
b = randint(0,100)

def add(a,b):
	return a + b
def subtract(a,b):
	return a - b 
def multiply(a,b):
	return a * b 
def divide(a,b):
	return a / b 

def exit_program():
	print('Exiting program.')
	exit()

print('A for Addition')
print('B for Subtraction')
print('C for Multiplication')
print('D for Division')
print('Q to Quit program')

while True:
	operation = input('Select operation you would like to perform next:').lower()

	if operation in ['Q','q']:
		exit_program()

	if operation in ['A','a']:
		print(a,'+',b,'=',add(a,b))
	elif operation in ['B','b']:
		print(a,'-',b,'=',subtract(a,b))
	elif operation in ['C','c']:
		print(a,'*',b,'=',multiply(a,b))
	elif operation in ['D','d']:
		if b !=0:
			print(a,'/',b,'=',divide(a,b))
		else:
			print('cannot divide by 0')
	else:
		print('A, B, C, D, and Q nga lang pwede teh, papansin ka')