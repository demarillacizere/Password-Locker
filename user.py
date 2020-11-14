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

    @classmethod
    def check_authentication(password):
        '''
        Method that checks if the account password entered is correct
        Args:
            password: checking if the password entered matches the password saved 
        Returns :
            Boolean: True or false depending if the password is correct or not
        '''
        for user in cls.users_list:
            if user.password == password:
                    return True

        return False
    