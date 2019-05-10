import unittest # Importing the unittest module
from credential import Credential # Importing the credential class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("twitter", "batman", "drknight") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.myaccountname,"twitter")
        self.assertEqual(self.new_credential.myusername,"batman")
        self.assertEqual(self.new_credential.mypassword,"drknight")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        '''
        test to check if we can check multiple objects within credenials list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("twitter","batman","drknight") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
    


if __name__ == '__main__':
    unittest.main()
