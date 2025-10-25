""" M. Bock 9/26/2019 Dictionary Sample Program – this program is very similar to the lab.
As you adapt it to the new content, you will have to add a new feature "edit" to change an existing entry.
Edit has to be added to the menus, and a function has to be added and called. In addition,
note the program features that change case of strings.
You may have to adapt this code to fit capitalization of your new program. """



def main():
    try:
        users = {'hhassan': 'hassan hassan', 'jsmith': 'jake smith', 'acooper': 'ann cooper'}
        display_menu()
        while True:
            command = input('Command: ').lower()
            if command == 'view':
                view(users)
            elif command == 'add':
                add(users)
            elif command == 'del':
                delete(users)
            elif command == 'edit':
                edit(users)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')

def display_menu():
    print('COMMAND MENU')
    print('view - View user name')
    print('add - Add a user')
    print('edit - Edit a user')
    print('del - Delete a user')
    print('exit - Exit program')
    print()


def view(users):
    display_usernames(users)
    username = input('Enter username to view: ')
    username = username.lower()

    if(not username in users):
        print('There is no user with that username. \n')
        return
        
    name = users[username]
    print('The user\'s full name is: ' + name.title() + '.\n')


def add(users):
    username = input("Enter new username to add: ").lower()
    full_name = input("Enter full name: ").lower()

    if(username in users):
        print("User with username " + username + " already exists!\n")
        return
    
    users[username] = full_name
    print("Successfully created user " + username + " (" + full_name.title() + ")\n")

def delete(users):
    display_usernames(users)
    username = input("Enter username to delete: ").lower()

    if(not username in users):
        print("User with username " + username + " does not exist!\n")
        return
    
    full_name = users.pop(username)
    print("Successfully deleted user " + username + " (" + full_name.title() + ")\n")

def edit(users):
    display_usernames(users)
    username = input("Enter username to edit: ").lower()

    if(not username in users):
        print("User with username " + username + " does not exist!\n")
        return
    
    users[username] = input("New full name (" + users[username].title() + "): ").lower() or users[username]
    
    print("Successfully edited user with username " + username + "\n")
    print("Updated record:")
    print("Full name: " + users[username].title() + "\n")


def display_usernames(users):
    """Displays the keys from the passed-in dictionary"""
    usernames = list(users.keys())
    usernames.sort()
    line = 'Usernames: '
    for username in usernames:
        line += username + ' '
    print(line)


if __name__ == '__main__':
    main()