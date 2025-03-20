import requests
import json

URL = "http://127.0.0.1:8000/postapi/postinfo/"

# r = requests.get(url = URL)
# data = r.json()

# print(data)


# def get_data(id=None):
#     data = {}
#     if id is not None:
#         data = {'id': id}
#     json_data = json.dumps(data)
#     r = requests.get(url=URL, data=json_data)
#     data = r.json()
#     print(data)


# get_data(5)

def post_data():
    data = {
        'post_title': 'MP Post',
        'post_description': 'Bhopal is the capital of Madhya Pradesh',
        'post_user_id': 2
    }
    # Convert python data into json data
    json_data = json.dumps(data)
    # send request and get responst
    r = requests.post(url=URL, data=json_data)
    # conver json response into python data
    data = r.json()
    # print(type(data))
    print(data)

# post_data()

def update_data():
    data = {
        'id': 65,
        'post_title': 'My Nice article',
        # 'post_description': 'I am proud to be an Indian',
        'post_user_id': 2
    }

    # convert dict to json string
    json_data = json.dumps(data)

    # make put request
    r = requests.put(url=URL, data=json_data)

    #parse json reponse
    data = r.json()

    print(data)


update_data()

def delete_data():
    data = {'id': 66}

    # parse dict into json
    json_data = json.dumps(data)

    # making delete request
    r = requests.delete(url=URL, data=json_data)

    # parsing json data into python native data
    data = r.json()

    print(data)


# delete_data()
