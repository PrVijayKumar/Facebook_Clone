from django.http import HttpResponse, JsonResponse
from user.serializers import UserSerializer, CreateUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from user.models import User
import io
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
import pdb


# @decorators(name='patch')
@method_decorator(csrf_exempt, name='dispatch')
class UserAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            user = User.objects.get(id=id)
            data = UserSerializer(user)
            return JsonResponse(data)
        users = User.objects.all()
        data = UserSerializer(users)
        return JsonResponse(data, safe=False)
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = UserSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'User Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.errors, safe=False)
    
    def put(self, request, *args, **kwargs):
        pdb.set_trace()
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'User Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.errors, safe=False)
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        user = User.objects.get(id=id)
        user.delete()
        res = {'msg': 'User Deleted!!'}
        return JsonResponse(res)



# Model Object - Single Student Data

# def user_detail(request, pk):
#     user = User.objects.get(id=2)
#     print(user)
#     serializer = UserSerializer(user)
#     print(serializer)
#     print(serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     print(json_data)
#     return HttpResponse(json_data, content_type='application/json')

# Query Set - Users List
# def user_list(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')


# Create User using API
# csrf problem will arise
# to handle csrf we will use csrf_exempt decorator
# @csrf_exempt
# def create_user(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = CreateUserSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'User Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="applicaton/json")
#         return JsonResponse(serializer.errors, safe=False)
    

# # post method requires csrf token so to avoid csrf token we will need decorator csrf_exempt
# @csrf_exempt
# def user_api(request):
#     if request.method == 'GET':
#         # get json data from request.body
#         json_data = request.body
#         # store json data in buffer
#         stream = io.BytesIO(json_data)
#         # parse json data into python native data type
#         python_data = JSONParser().parse(stream)
#         # check if id is None
#         id = python_data.get('id', None)
#         if id is not None:
#             user = User.objects.get(id=id)
#             # convert model instance to python native data type using serializer class
#             serializer = UserSerializer(user)
#             # render python native data into json using JSONRenderer
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type="application/json")
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         # json_data = JSONRenderer().render(serializer.data)
#         return JsonResponse(serializer.data, safe=False)
    

#     # defining procedure for post request
#     if request.method == 'POST':
#         json_data = request.body
#         # store incoming data in buffer
#         stream = io.BytesIO(json_data)
#         # parse incoming data to native python data type
#         pythondata = JSONParser().parse(stream)
#         # convert native python data to complex data type or model instance
#         serializer = UserSerializer(data=pythondata)
#         # check if data is valid or not
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'User Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
#         return JsonResponse(serializer.errors, safe=False)
    

#     # procedure to handle put request
#     if request.method == 'PUT':
#         json_data = request.body
#         # store json data in buffer
#         stream = io.BytesIO(json_data)
#         # parse json data into python native data type
#         pythondata = JSONParser().parse(stream)
#         # get id of the object to be updated
#         id = pythondata.get('id')
#         #Get the object
#         user = User.objects.get(id=id)
#         # use serializer to update data of the instance
#         serializer = UserSerializer(user, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'User updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
#         return JsonResponse(serializer.errors, safe=False)
        
#     # code to handle delete request
#     if request.method == 'DELETE':
#         json_data = request.body
#         # store json_data in the buffer
#         stream = io.BytesIO(json_data)
#         # parse json data into python native data type
#         pythondata = JSONParser().parse(stream)
#         # getting id of the object
#         id = pythondata.get('id')
#         # getting object to be deleted
#         user = User.objects.get(id=id)
#         user.delete()
#         res = {'msg': 'User Deleted!!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type="application/json")

