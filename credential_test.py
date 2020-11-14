import unittest
from credential import Credential
import pyperclip

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("","",'')
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account,"")
        self.assertEqual(self.new_credential.username,"")
        self.assertEqual(self.new_credential.password,"")
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the contact list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []