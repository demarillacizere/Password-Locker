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

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact     
                