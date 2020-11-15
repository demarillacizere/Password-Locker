import pyperclip
import random
import string
class Credential:
    '''
    class that generates new instances of credentials
    '''
    credential_list=[]
    def __init__(self,accountname,username,password):
        self.account=accountname
        self.username=username
        self.password=password

    def save_credential(self):

        '''
        save_credentials method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)    
    
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
		Function to generate an 8 character password for a credential
		'''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)   

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in an account name and returns its credentials.

        Args:
            account: account name to search for
        Returns :
            Credentials of an account name that matches the search .
        '''

        for credential in cls.credential_list:
            if credential.account == account:
                return credential   

    @classmethod
    def credentials_exist(cls,name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            name: Platform name to search if it its credentials are saved
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credential in cls.credential_list:
            if credential.account == name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list              
                