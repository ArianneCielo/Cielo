from user_functions import register_user, edit_user
                                                                                                                                                                        
user = ''
user_email = ''

while True:

	user_input = input(''' 
1.) Show User
2.) Create User
3.) Clear User
4.) Edit User
0.) Exit

What do you want to do?: '''
)

	if user_input == '1':

		if user != '':
			print(f'\n{user} - {user_email}')
		else:
			print('\nNo user found')

	elif user_input == '2':

		new_user = register_user()
		user = new_user['user_name']
		user_email = new_user['email']

		print(f'\nNew User Created! Welcome {new_user["new_user"]}')

	elif user_input == '3':
		
		user = ''
		user_email = ''

	elif user_input == '4':

		editted_user = edit_user(user)

		user = editted_user['user_name']
		user_email = editted_user['email']

	else:
		break
