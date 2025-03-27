# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from post.models import PostModel
from post.serializers import PostSerializer, CreatePostSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from user.serializers import UserSerializer
import pdb
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
# from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView

# from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# from rest_framework import viewsets, status
# from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from user.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from user.throttling import JackRateThrottle
from rest_framework.generics import ListAPIView
# from user.api_views.custompermission import MyPermission
class PostList(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'postscope'


# class PostModelViewSet(viewsets.ModelViewSet):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle, JackRateThrottle]


# class PostModelViewSet(viewsets.ModelViewSet):
#     queryset = PostModel.objects.all()
    # serializer_class = PostSerializer
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [CustomAuthentication]
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [MyPermission]





# class PostModelViewSet(viewsets.ModelViewSet):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAdminUser]

# class PostReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer


# class PostViewSet(viewsets.ViewSet):
#     def list(self, request):
#         posts = PostModel.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         print("**********List**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         print("**********Retrieve**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         id = pk
#         if id is not None:
#             post = PostModel.objects.get(pk=id)
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
        
#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         print("**********Create**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Post Created!!'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         post = PostModel.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data)
#         print("**********Update**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Post Updated!!'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self, request, pk):
#         post = PostModel.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         print("**********Partial Update**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Post Updated Partially!!'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk):
#         post = PostModel.objects.get(pk=pk)
#         print("**********Destroy**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         post.delete()
#         return Response({'msg': 'Post Deleted!!'})




# class ListCreatePost(ListCreateAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

# class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer



# class CreateListPost(ListCreateAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

# class RetrieveUpdatePost(RetrieveUpdateAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

# class RetrieveDestroyPost(RetrieveDestroyAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer



# code for concrete api view


# class PostList(ListAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer


# class PostCreate(CreateAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(RetrieveAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

# class UpdatePost(UpdateAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

# class DeletePost(DestroyAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer








"""class PostAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            post = PostModel.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        posts = PostModel.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id = pk
        post = PostModel.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post Updated !!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        id = pk
        post = PostModel.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post Updated Partially !!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        id = pk
        post = PostModel.objects.get(id=id)
        post.delete()
        return Response({'msg': 'Post Deleted !!'})"""


"""@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def PostApi(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            post = PostModel.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        posts = PostModel.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        post = PostModel.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post Updated!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        post = PostModel.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post Updated Partially !!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = pk
        post = PostModel.objects.get(id=id)
        post.delete()
        return Response({'msg': 'Post Deleted !!'})"""























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

# @api_view(['GET', 'POST'])
# @authentication_classes([])
# @permission_classes([])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg': 'This is a GET Request'})
    
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'This is a POST Request', 'data': request.data})
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
    