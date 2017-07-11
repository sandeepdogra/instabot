import requests
from constant import APP_ACCESS_TOKEN,BASE_URL
def comment_list(insta_username):
    request_url = (BASE_URL + '/media/{media-id}/comments?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment = requests.get(request_url).json()
    if comment['meta']['code'] == 200 :
        print comment
