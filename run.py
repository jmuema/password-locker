#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(uname, pword):
    '''
    Function to create a new user
    '''
    new_user = User(uname, pword)
    return new_user
