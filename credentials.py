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