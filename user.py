class User:
    """ 
    A class that generates a passsword locker account credentials (username and password)
    """
    users_list=[]

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_user(self):
        '''
        save_user method saves user account credentials into users_list
        '''

        User.users_list.append(self)   

    @classmethod
    def check_user(cls,username,password):
        '''
		Method that checks if the name and password entered match entries in the users_list
		'''
        for user in cls.users_list:
            current_user = ''
            if(user.username == username and user.password == password):
                current_user = user.username
		    
        return current_user
    