import unittest 
from user import User
import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("","")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"")
        self.assertEqual(self.new_user.password,"")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)


if __name__ == '__main__':
    unittest.main()    