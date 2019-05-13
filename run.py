#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(uname, pword):
    '''
    Function to create a new user
    '''
    new_user = User(uname, pword)
    return new_user


def create_credential(aname,uname,pword):

    new_credential = Credential(aname, uname, pword)
    return new_credential


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def save_credentials(credential):

    credential.save_credential()


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)


def check_existing_credentials(username):
    '''
    Function that check if a credential exists with that number and return a Boolean
    '''
    return Credential.credential_exist(username)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


def generate_password():
    '''
    Function to generate random password
    '''
    return User.generate_password()


def main():
    print("Welcome to your password storage app. What is your name?")
    my_name = input()

    print(f"Welcome {my_name}! ")
    print('\n')

    while True:
        print("Use the short codes to have a good experience the password storage app:\nca- create an account (For first-time users)\nla- log into an account\nex- exit an account")
        shortcode = input().lower()
        print('\n')

        if shortcode == 'ca':
            print("Your username:")
            u_name = input()
            print("Do you want to autogenerate a password (Choose 'y' or 'n') ?")
            while True:
                choice = input().lower()
                if choice == 'y':
                    accountpassword = User.generate_password()
                    print(f"This is your password- {accountpassword}")
                    break
                elif choice == 'n':
                    print("Enter your password for the account")
                    accountpassword = input()
                    print(f"This is your password- {accountpassword}")
                    break
                else:
                    print(" Please choose 'y' or 'n' ")
            # create and save new user.
            save_users(create_user(u_name,accountpassword))
            print('\n')
            print(f"***{u_name} your account has been created! Welcome.***")
            print('\n')


        elif shortcode == 'la':
            print("Enter your username")
            u_name = input()
            print("Enter your password")
            p_word = input()

            if not User.user_list:   #code to check if user list is empty
                print('\n')
                print("***You are not in the system***")

            for user in User.user_list:

                if u_name == user.myusername and p_word == user.mypassword:

                    print('''
                    ***
                    Login Successful.
                    ***
                    ''')
                    print('\n')

                    print(f"Welcome {u_name}! So, what would you like to do?")

                    while True:
                        print("Use these short codes : cc - create new credentials, dc - display credenials,  del- delete user credenials, lv -exit the user list")

                        short_code = input().lower()

                        if short_code == 'cc':
                            # print("-" * 10)

                            print("Enter your Account name:")
                            a_name = input()
                            print("Enter your username:")
                            u_name = input()
                            print("Do you want to autogenerate a password (Choose 'y' or 'n') ?")
                            while True:
                                choice = input().lower()
                                if choice == 'y':
                                    credentialpassword = Credential.generate_password()
                                    print(f"This is your password- {credentialpassword}")
                                    break
                                elif choice == 'n':
                                        print("Enter your password for the account")
                                        credentialpassword = input()
                                        print(f"This is your password- {credentialpassword}")
                                        break
                                else:
                                        print(" Please choose 'y' or 'n' ")
                                # create and save new credenials.
                            save_credentials(create_credential(
                                a_name, u_name, credentialpassword))

                            print ('\n')
                            print(f"*** New credentials saved for {u_name} ***")
                            print ('\n')

                        elif short_code == 'dc':
                            if display_credentials():
                                print('\n')

                            # loops through credential object & gets each user
                                for credential in display_credentials():
                                    print(f"***Here is a list of {my_name}'s credentials: {credential.myaccountname}-{credential.myusername}-{credential.mypassword}***")
                                    print('\n')
                            else:
                                print("***No user credentials saved***")
                                print('\n')

                        elif short_code == 'del':
                            print("Enter your account username so that account can be deleted")

                            search_username= input()
                            if check_existing_credentials(search_username):
                                search_credential = find_credential(search_username)
                                delete_credential(search_credential)
                                print(f"{search_username} is deleted")

                            else:
                                print("***That username doesn't exist***")

                        elif short_code == "lv":
                                print("***Till we meet again, Goodbye!***")
                                break

                        else:
                            print("***Back to the shortcodes. Choose one.***")
                            print('\n')

                else:
                    print("***Username or Email isn't valid. Try again or Sign Up as a New User***")
                    print('\n')

        elif shortcode == "ex":
                print("Until next time")
                print('\n')
                break

        else:
            print("***Back to the shortcodes. Choose one.***")

if __name__ == '__main__':

    main()
