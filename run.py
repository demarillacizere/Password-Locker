#!/usr/bin/env python3.6
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
    User.save_user()

def check_password(password):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.check_password(password)

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

def delete_credential(credential):
    '''
    Function to generate credential
    '''
    credential.delete_credential() 

def find_credential(accountname):
    '''
    Function that finds a credential by account name and returns the contact
    '''
    return Credential.find_by_account(accountname)
def check_existing_credentials(credential):
    '''
    Function that check if a credentials for a certain platform exists and return a Boolean
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

def main():
    print("Welcome to Password Locker !")
    print('What is your name')
    username=input()
    print (f"Welcome {username}, create your account")
    print(f"username :{username}")
    print('create a password')
    password=input()
    # save_account(create_account(username,password))
    print('enter the password you just created in order to login to your account')
    if password==input():
        print('Use the following short codes to navigate your account')
        while True:
            print("Use : ac - add new credentials,gc - generate a new password for credential, dc - display credentials, fc -find a credential, del -delete a credential, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'ac':
                    print("New Credential")
                    print("-"*10)

                    print ("Account name (eg: twitter,facebook...) ....")
                    account = input()

                    print("username ...")
                    username = input()

                    print("password ...")
                    passwordr = input()


                    save_credential(create_credential(account,username,password)) # create and save new contact.
                    print ('\n')
                    print(f"New Credential {account} {username} {password} added")
                    print ('\n')

            elif short_code  =='gc':
                print("New Credential")
                print("-"*10)

                print ("Account name (eg: twitter,facebook...) ....")
                account = input()

                print("username ...")
                username = input()

                password = generate_password()
                print(f"the password for your new {account} account is {password}")


                save_credential(create_credential(account,username,password)) # create and save new contact.
                print ('\n')
                print(f"New Credential {account} {username} {password} added")
                print ('\n')
            elif short_code == 'dc':

                    if display_credentials():
                            print("Here is a list of all your saved credentials")
                            print('\n')

                            for credential in display_credentials():
                                    print(f"{credential.account} {credential.username} .....{credential.password}")

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
                            print(f"{search_credential.account} {search_credential.username}")
                            print('-' * 20)

                            print(f"username.......{search_credential.username}")
                            print(f"password.......{search_credential.password}")
                    else:
                            print("That credential does not exist")
            elif short_code == 'del':
                print()
                 delete_credential()

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                                print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()
