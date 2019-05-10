import unittest  # Importing the unittest module
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
    

if __name__ == '__main__':
    unittest.main()