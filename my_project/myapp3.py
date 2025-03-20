import requests
import json

URL = "http://127.0.0.1:8000/userapi/userinfo/"
# URL = "http://127.0.0.1:8000/postapi/postinfo/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data(58)


def post_data():
    data = {
        'username': 'Sunil',
        'email': 'abhay@gmail.com',
        'is_staff': False,
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()


def update_data():
    data = {
        'id': 6,
        'username': 'Mohan',
        'is_staff': True
    }

    # convert it into json
    json_data = json.dumps(data)

    r = requests.put(url=URL, data=json_data)

    data = r.json()
    print(data)


# update_data()

def delete_data():
    data = {'id': 4}
    # convert data into json string
    json_data = json.dumps(data)

    # sending delete request to delete the object
    r = requests.delete(url=URL, data=json_data)

    # parsing json string to native python data type
    data = r.json()

    print(data)

# delete_data()