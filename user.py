import random


class User:
    '''
    Class that generates new users
    '''
    user_list = []

    def __init__(self, username, password):
        '''
        defining properties for our object
        '''
        self.myusername = username
        self.mypassword = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def generate_password():
        chars = "abcdefghijklmnopqrstuvwxyz/;'[]=)(*$@)"
        password = ""
        for i in range(10):
            password += random.choice(chars)
        return password  # computated functions give a return value

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list
