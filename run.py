#!/usr/bin/env python3.6
from user import User
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

def main():
    print("Welcome to Password Locker !")
    print('What is your name')
    username=input()
    print (f"Welcome {username}, create your account")
    print(f"username :{username}")
    print('create a password')
    password=input()
    print('enter the password you just created in order to login to your account')
    login_password=input()
    if login_password==password:
        print('welcome')

if __name__ == '__main__':

    main()
