import requests
from constant import BASE_URL, APP_ACCESS_TOKEN
from get_user_post import get_user_post

def like_user_post(insta_username):
    # fuction is created for like post of user

    media_id = get_user_post(insta_username)
    print media_id
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    post_a_like = requests.post(request_url, payload).json()

    if post_a_like['meta']['code'] == 200:
        print "Post Liked Successfully"
    else:
        print "Unable to like post"
