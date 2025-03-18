import requests

URL = "http://127.0.0.1:8000/postapi/createpost/"

post_info = {
    'post_title': 'Neemuch Post',
    'post_description': 'Its a very nice post about facebook.',
    'post_user_id': 2,
}

data = requests.post(url=URL, json=post_info)

json_data = data.json()

print(json_data)