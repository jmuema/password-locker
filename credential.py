import random

class Credential:

    '''
    Class that creates new instance of credentials
    '''
    credential_list=[]

    def __init__(self, accountname, username, password):
        self.myaccountname = accountname
        self.myusername = username
        self.mypassword = password

    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''

        # appends every new value in the credential list
        Credential.credential_list.append(self)
   