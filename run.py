#!/usr/bin/env python3.6
from user import User
from credentials import Credential
def create_account(username,password):
    '''
    Function to create a new account
    '''
    new_user = User(username,password)
    return new_user
def save_account(user):
    '''
    Function to save new user
    '''
    User.save_user(user)

def verify_user(username,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = User.check_user(username,password)
	return checking_user

def create_credential(account,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account,username,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def find_credential(site_name):
    '''
    Function that finds a credential by site name and returns the credential
    '''
    return Credential.find_by_site(site_name)
def check_existing_credentials(credential):
    '''
    Function that check if a credentials for a certain site exists and return a Boolean
    '''
    return Credential.credentials_exist(credential)
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def delete_credential(credential):
    '''
    Function to delete credential
    '''
    credential.delete_credential()

def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)

def main():
    print(' ')
    print("Hello! Welcome to Password Locker")
    while True:
        print('')
        print("-"*60)
        print('use these codes to navigate: \n ca-Create an account \n li-Log In \n ex-ezit')
        short_code = input("Enter a choice: ").lower().strip()
        if short_code== 'ex':
            break
        elif short_code == 'ca':
            print('-'*60)
            print(' ')
            print('To create a new account:')
            username= input('Enter your username - ').strip()
            password = input('Enter your password - ').strip()
            save_account(create_account(username,password))
            print(' ')
            print(f'New account created for: {username} using password: {password}')
        elif short_code =='li' :
            print('-'*60)
            print(' ')
            print('To login, enter your account details:')
            user_name = input('Enter your username - ').strip()
            password = input('Enter your password - ').strip()
            user_exists = verify_user(user_name,password)
            if user_exists == user_name:
                print('Use the following short codes to navigate your account')
            while True:
                print("Use : ac - add new credentials, dc - display credentials, fc -find a credential, del -delete a credential, ex -exit the contact list ")

                short_code = input().lower()

                if short_code == 'ac':
                        print("New Credential")
                        print("-"*10)

                        print ("Site name (eg: twitter,facebook...) ....")
                        site = input()
                        print("username ...")
                        username = input()
                        while True:
                            print(' ')
                            print('-'*60)
                            print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                            psw_choice = input('Enter an option: ').lower().strip()
                            print('-'*60)
                            if psw_choice == 'ep':
                                print(' ')
                                password = input('Enter your password: ').strip()
                                break
                            elif psw_choice == 'gp':
                                password = generate_password()
                                break
                            elif psw_choice == 'ex':
                                break
                            else:
                                print("")
                        save_credential(create_credential(site,username,password)) # create and save new contact.
                        print ('\n')
                        print(f"New Credential {site} added")
                        print(f'Username....{username}')
                        print(f'Password....{password}')
                        print ('\n')

                elif short_code == 'dc':

                        if display_credentials():
                                print("Here is a list of all your saved credentials")
                                print('\n')

                                for credential in display_credentials():
                                        print(f"{credential.site_name} account")
                                        print(f"username.......{credential.username}")
                                        print(f"username.......{credential.password}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any credentials saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the account you want to search for")

                        search_name = input()
                        if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"{search_credential.site_name}")
                                print('-' * 20)

                                print(f"username.......{search_credential.username}")
                                print(f"password.......{search_credential.password}")
                        else:
                                print("That credential does not exist")
                elif short_code == 'del':
                    print("enter the site name of the credential you want to delete")
                    search_name=input()
                    if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            delete_credential(search_credential)

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                    print("I really didn't get that. Please use the short codes")

            else:
                print(' ')
                print('Ooops! Wrong details entered. Try again or create an account')

        else:
            print('-'*60)
            print(' ')
            print('Ooops! Wrong option entered. Try again.')
		
if __name__ == '__main__':

    main()