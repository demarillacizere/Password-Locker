class Credential:
    '''
    class that generates new instances of credentials
    '''
    credential_list=[]
    def __init__(self,accountname,username,password):
        self.account=accountname
        self.username=username
        self.password=password