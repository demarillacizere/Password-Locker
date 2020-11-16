import unittest
from credentials import Credential
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
        self.new_credential = Credential("IG","Dema",'d30')
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.site_name,"IG")
        self.assertEqual(self.new_credential.username,"Dema")
        self.assertEqual(self.new_credential.password,"d30")
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
    
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credential to check if we can save multiple contact
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential('instagram',"user","12dgj")
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credentials(self):
            '''
            test_delete_contact to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_save_credential = Credential("instagram","user","tes333")
            test_save_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list),1) 

    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credential()
        new_credential = Credential('Twitter','user','1200')
        new_credential.save_credential()
        new_credential = Credential('Google','user2','we300')
        new_credential.save_credential()
        self.assertEqual(len(Credential.display_credentials()),3)
    def test_find_by_site(self):
        '''
        Test to check if the find_by_site method returns the correct credential
        '''
        self.new_credential.save_credential()
        new_credential = Credential('Twitter','user','1200')
        new_credential.save_credential()
        credential_exists = Credential.find_by_site('Twitter')
        self.assertEqual(credential_exists,new_credential)

if __name__ == '__main__':
    unittest.main()                