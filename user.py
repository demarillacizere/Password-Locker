class User:
    """ 
    A class that generates a passsword locker account credentials (username and password)
    """
    users_list=[]

    def __init__(self,username,password):
        self.username=name
        self.password=password

    def save_user(self):
         '''
        save_user method saves user account credentials into users_list
        '''

        User.users_list.append(self)   