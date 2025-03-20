from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from post.models import PostModel
from post.serializers import PostSerializer, CreatePostSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from user.serializers import UserSerializer
import pdb

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response


# @api_view()
# @authentication_classes([])
# @permission_classes([])
# def hello_world(request):
#     pdb.set_trace()
#     print('userinfo')
#     print(request.user)
#     return Response({'msg': 'This is a get request'})


# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
# def hello_world(request):
#     print(request.data)
#     return Response({'msg':'This is a post request.'})

@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'This is a GET Request'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is a POST Request', 'data': request.data})
# def post_info(request, pk):
#     post = PostModel.objects.get(id=pk)
#     serializer = PostSerializer(post)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type="application/json")
#     return JsonResponse(serializer.data)

# def post_list(request):
#     posts = PostModel.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return JsonResponse(serializer.data, safe=False)

# View to store post info using api
# here we will use csrf_exempt decorator to allow storing data without csrf
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # parse the json data to python native data type
        pythondata = JSONParser().parse(stream)

        # Now convert native data type to complex data type using serializer class
        serializer = CreatePostSerializer(data=pythondata)
        # Now check if incoming data is valid
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Post Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.errors, safe=False)
    

# api to send information of post
# @csrf_exempt
# def post_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         # store json data in buffer
#         stream = io.BytesIO(json_data)
#         # parse json data into python native data type
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             post = PostModel.objects.get(id=id)
#             # convert complex type into python native data type
#             serializer = PostSerializer(post)
#             # render native data to json data
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         posts = PostModel.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     if request.method == 'POST':
#         json_data = request.body
#         # store json_data into the buffer
#         stream = io.BytesIO(json_data)
#         # parse json data into python native data type
#         pythondata = JSONParser().parse(stream)
#         # convert native data into complex data or model instance
#         pdb.set_trace()
#         # user = User.objects.get(id=pythondata.get('post_user_id'))
#         # serializer = UserSerializer(user)
#         # pythondata['post_user'] = serializer.data
#         # pythondata.pop('post_user_id')
#         serializer = PostSerializer(data=pythondata)
#         breakpoint()
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Post Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(serializer.errors, safe=False)
    

#     # Define procedure for put request
#     if request.method == 'PUT':
#         json_data = request.body
#         # store json_data in buffer
#         stream = io.BytesIO(json_data)
#         breakpoint()
#         # parse json data into python native data type
#         pythondata = JSONParser().parse(stream)
#         # Getting id of the post to be updated
#         id = pythondata.get('id')
#         #Getting the post to be updated
#         post = PostModel.objects.get(id=id)
#         # Use serializer to update the data of post using api
#         breakpoint()
#         serializer = PostSerializer(post, data=pythondata, partial=True)
#         pdb.set_trace()
#         print("breakpoint")
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Post Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(serializer.errors, safe=False)
    
#     # code to handle delete request
#     if request.method == 'DELETE':
#         json_data = request.body
#         # storing json data into buffer
#         stream = io.BytesIO(json_data)
#         # parsing json data into python native data type
#         pythondata = JSONParser().parse(stream)
#         # getting id of the post to be deleted
#         id = pythondata.get('id')
#         # getting post to be deleted
#         post = PostModel.objects.get(id=id)
#         post.delete()
#         res = {'msg': 'Post Deleted!!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type="application/json")
    