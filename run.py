#!/usr/bin/env python3.6
from user import User
def create_account(fname,lname,phone,email):
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

print("Welcome to Password Locker")
print('What is your name')
new_user.username=input()
print ("")