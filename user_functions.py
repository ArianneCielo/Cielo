def register_user():
	user_name = input("Enter your user name:")
	email = input('Enter email:')

	return {'user_name': user_name,'email':email,'new_user':user_name}

def edit_user(existing_user):
	if existing_user:
		print(f'\nEditing user:{existing_user}')
		new_user_name = input('Enter new username:')
		new_email = input('enter new email:')

		return {'user_name':new_user_name,'email':new_email}

	else:
		print('\nNo user to edit.')
		return {'user_name':'','email':''}

