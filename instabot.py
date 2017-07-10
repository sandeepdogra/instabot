#all global variables are here
import requests
#instagram api access token
APP_ACCESS_TOKEN = '804302568.f825c9e.71d2e1af5a4b45f8b0cdfed1988ae40f'
#instagram api base url
BASE_URL = 'https://api.instagram.com/v1/'


from self_info import *
from get_user_info import *
from get_own_post import *
from like_user_post import *
from comment_user_post import *
from get_user_post import *


def start_bot():
    while True:
        print "Welcome to instaBot!\n"
        print "Menu options:\n"
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        print "5.Like the recent post of a user\n"
        print "6.Make a comment on the recent post of a user\n"
        print "7.Exit"

        choice = int(raw_input("Enter you choice: "))
        if choice == 1:
            self_info()
        elif choice == 2:
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == 3:
            get_own_post()
        elif choice == 4:
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == 5:
           insta_username = raw_input("Enter the username of the user: ")
           like_user_post(insta_username)
        elif choice == 6:
           insta_username = raw_input("Enter the username of the user: ")
           comment_user_post(insta_username)
        elif choice == 7:
            exit()
        else:
            print "wrong choice"

start_bot()