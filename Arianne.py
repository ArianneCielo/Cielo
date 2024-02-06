var1_a = input('Enter 1st number:')
var2_b = input('Enter 2nd number:')

if var1_a.isdigit() and var2_b.isdigit():
	var1 = int(var1_a)
	var2 = int(var2_b)

	addition = var1+var2
	subtraction = var1-var2
	multiplication = var1*var2
	division = var1/var2

	print(f'The sum is: {addition}')
	print(f'The difference is: {subtraction}')
	print(f'The qoutient is: {division}')
	print(f'The product is: {multiplication}')

else:
	print('Number nga lang ilalagay mo, papansin ka?')
	