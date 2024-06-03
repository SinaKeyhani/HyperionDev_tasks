# This program is designed for users to choose between login and register options.
# Making sure we have access to the file.
# Defining each function.
# Print a menu to display which option users want to use.

def login(username, password):
    with open('/Users/ambl/Documents/Data_Bootcamp /Clasess/Tasks/Task 14/user.txt', 'r') as file:
        users = {}
        for line in file:
            user, passw = line.strip().split(', ')
            users[user] = passw

    while True:
        if username not in users:
            print('This username does not exist!!')
            username = input('Please enter your username again: ')
        elif password != users[username]:
            print('Password is incorrect!')
            password = input('Please enter your password again: ')
        else:
            print(f'Welcome {username}')
            break

def reg_user():
    with open('/Users/ambl/Documents/Data_Bootcamp /Clasess/Tasks/Task 14/user.txt', 'r') as file:
        users = {}
        for line in file:
            user, passw = line.strip().split(', ')
            users[user] = passw

    while True:
        new_username = input("Please enter your username: ")
        if new_username in users:
            print("This username is taken!")
            continue

        new_password = input("Please enter your password: ")
        confirm_password = input("Please confirm your password: ")

        if new_password != confirm_password:
            print("Passwords do not match!")
            continue

        print(f"New user added: {new_username}")

        with open("/Users/ambl/Documents/Data_Bootcamp /Clasess/Tasks/Task 14/user.txt", "a") as file:
            file.write(f"{new_username}, {new_password}\n")
        break

print('\nWelcome to the program. Please find the menu below:')
print('\nLogin - to login to your account')
print('\nRegister - to register a new account')

user_choice = input('\nPlease enter your choice: ').capitalize()

while True:
    if user_choice == 'Login':
        user_name = input('Please enter your username: ')
        pass_word = input('Please enter your password: ')
        login(user_name, pass_word)
        break
    elif user_choice == 'Register':
        reg_user()
        print('Welcome to the program')
        break
    else:
        print('Invalid input')
        user_choice = input('Please enter your choice (Login/Register): ').capitalize()
