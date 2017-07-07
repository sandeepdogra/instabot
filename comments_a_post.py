import requests
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_user_post import get_user_post
username = "kirangarg95"
def post_a_comment(insta_username):
    post_id = get_user_post(insta_username)
    # print media_id
    request_url = (BASE_URL + ''
                            'media/%s/comments') % (post_id)
    message = raw_input("Enter your Message: ")
    payload = {"access_token": APP_ACCESS_TOKEN, 'text':message}
    print 'POST request url : %s' % (request_url)
    post_a_comment = requests.post(request_url, payload).json()

    if post_a_comment['meta']['code'] == 200:
        print "Post comment Successfully"
    else:
        print "Unable to comment on post"
post_a_comment(username)