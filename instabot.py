from self_info import *
from get_user_info import *
from get_own_post import *
from like_user_post import *
from comment_user_post import *
from get_user_post import *
from like_list import *
from comment_list import *
from hash_tag import *

def insta_bot():
    while True:
        print "Welcome to instaBot!\n"
        print "Menu options:\n"
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        print "5.Like the recent post of a user\n"
        print "6.Make a comment on the recent post of a user\n"
        print "7.list of likes on recent post of a user\n"
        print "8.list of comments o a recnet post of a user\n"
        print "9.user hash tag details \n "
        print "10.Exit \n"

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
        elif choice == 7 :
            insta_username = raw_input("Enter the username of the user:")
            like_list(insta_username)
        elif choice == 8:
            insta_username = raw_input("Enter the username of the user:")
            comment_list(insta_username)
        elif choice == 9:
            insta_username = raw_input("Enter the user name: ")
            analyse_user(get_user_id(insta_username))
        elif choice == 10:
            exit()
        else:
            print "wrong choice"
