import random
class User:
    '''
    Class that generates new users
    '''
    user_list=[]

    def __init__(self,username,password):
        '''
        defining properties for our object
        '''
        self.myusername=username
        self.mypassword=password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)