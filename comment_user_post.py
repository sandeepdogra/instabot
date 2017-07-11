import requests
from constant import BASE_URL, APP_ACCESS_TOKEN
from get_user_post import get_user_post
def comment_user_post(insta_username):
    media_id = get_user_post(insta_username)
    print media_id
    message = raw_input("Enter your Message: ")
    payload = {"access_token":APP_ACCESS_TOKEN, 'text': message}
    request_url = (BASE_URL + 'media/%s/comments') % media_id
    print "POST request_url : %s" % (request_url)
    post_a_comment = requests.post(request_url, payload).json()

    print post_a_comment
    if post_a_comment['meta']['code'] == 200:
        print "Post comment Successfully"
    else:
        print "Unable to comment on posts"
