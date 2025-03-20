import requests
import json
# URL = "http://127.0.0.1:8000/postapi/createpost/"
URL = "http://127.0.0.1:8000/postapi/postinfo/"

post_info = {
    'post_title': 'Post about India',
    'post_description': 'Illegal Post',
    'post_user_id': 2,
}

json_data = json.dumps(post_info)

data = requests.post(url=URL, data=json_data)

json_data = data.json()

print(json_data)