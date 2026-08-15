current_users = ['Leo', 'Ryan', 'Admin', 'Jim', 'Andy']
new_users = ['Samuel', 'Leo', 'Karen', 'Cindy', 'Danny']
for id in new_users:
    if id in current_users:
        print(f'{id} is not available')
    else:
        print(f'{id} is valid')

