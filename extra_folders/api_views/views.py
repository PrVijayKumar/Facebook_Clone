from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from user.api_views.serializers import UserHyperlinkedSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io
# from django.views.decorators.csrf import csrf_exempt
# from django.views import View
# from django.utils.decorators import method_decorator
# import pdb

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
# from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets, status
# from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer, UserRegisterSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions, DjangoObjectPermissions
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from user.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from user.throttling import JackRateThrottle
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from user.mypaginations import MyPageNumberPagination, MyCursorPagination
from rest_framework.pagination import LimitOffsetPagination, CursorPagination
from user.forms import UserCreationForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
import logging
from rest_framework import permissions
# from .custompermission import MyPermission

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


logger = logging.getLogger(__name__)




class UserModelViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['username']
    throttle_classes = [AnonRateThrottle]
    pagination_class = MyCursorPagination

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)


class RegisterAPI(GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data
        })
    
class LoginAPI(GenericAPIView):
    serializer_class = AuthTokenSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data
        })
        # return super(LoginAPI, self).post(request)


class LogoutAPI(GenericAPIView):
    serializer_class = AuthTokenSerializer
    permission_class = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        try:
            return Response({
                'message': 'Successfully logged out'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class UserModelPermissions(DjangoObjectPermissions):
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
#         'HEAD': ['%(app_label)s.view_%(model_name)s'],
#         'POST': ['%(app_label)s.add_%(model_name)s'],
#         'PUT': ['%(app_label)s.change_%(model_name)s'],
#         'PATCH': ['%(app_label)s.change_%(model_name)s'],
#         'DELETE': ['%(app_label)s.delete_%(model_name)s'],
#     }

    # logger.info('in UserModelPermissions')
    # # permissions.SAFE_METHODS = ('GET', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS')
    # def has_permission(self, request, view):
    #     if request.method == 'GET':
    #         breakpoint()
    #         return True
    #     elif request.method == 'POST':
    #         return request.user.is_staff

    # def has_object_permission(self, request, view, obj):
    #     breakpoint()
    #     logger.info('in UserModelPermissions has_object_permission')
    #     print('permissions.SAFE_METHODS: ', permissions.SAFE_METHODS)
    #     if request.method in permissions.SAFE_METHODS:
    #         # return request.user == obj.owner or True # need to modify so can see own stuff
    #         # breakpoint()
    #         return request.user.id == obj.id or True  # need to modify so can see own stuff
    #     elif request.method == 'PATCH':
    #         # breakpoint()
    #         # return request.user == obj.owner
    #         return request.user.id == obj.id or request.user.is_staff
    #     elif request.method == 'DELETE':
    #         # return request.user == obj.owner
    #         return request.user.id == obj.id or request.user.is_staff
    #     elif request.method == 'PUT':
    #         return request.user.id == obj.id or request.user.is_staff
    #     return False
    #     # return request.user.id == obj.id

# class UserModelViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     # serializer_class = UserSerializer
#     serializer_class = UserHyperlinkedSerializer
#     pagination_class = MyCursorPagination
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # filter_backends = [OrderingFilter]
    # ordering_fields = ['username', 'email']
    # search_fields = ['username']
    # pagination_class = MyPageNumberPagination

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['username', 'email']
    # throttle_classes = [AnonRateThrottle, JackRateThrottle]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'userscope'

    # def get_queryset(self):
    #     user = self.request.user
    #     return User.objects.filter(pk=user.id)




# class UserModelViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [CustomAuthentication]
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [MyPermission]








# class UserModelViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAdminUser]


# class UserReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



# class UserViewSet(viewsets.ViewSet):
#     def list(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         print("**********list**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         id = pk
#         print("**********retrieve**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         if id is not None:
#             user = User.objects.get(pk=id)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
        
#     def create(self, request):
#         serializer = UserSerializer(data=request.data)
#         print("**********create**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'User Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         print("**********update**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'User Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self, request, pk):
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         print("**********partial update**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'User Update Partially'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk):
#         user = User.objects.get(pk=pk)
#         print("**********destroy**********")
#         print("basename:", self.basename)
#         print("action:", self.action)
#         print("detail:", self.detail)
#         print("suffix:", self.suffix)
#         print("name:", self.name)
#         print("description:", self.description)
#         user.delete()
#         return Response({'msg': 'User Deleted!!'})









# class ListCreateUser(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class ListCreateUser(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class RetrieveUpdateUser(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class RetrieveDestroyUser(RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



# class UserList(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class CreateUser(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UpdateUser(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class DeleteUser(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




"""class UserAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id = pk
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Updated !!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        id = pk
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User updated partially !!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        id = pk
        user = User.objects.get(id=id)
        user.delete()
        return Response({'msg': 'User Deleted !!'})"""



"""@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def UserAPI(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        users = User.objects.all()
        pdb.set_trace()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        id = pk
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Updated !!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id = pk
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Updated Partially'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = pk
        user = User.objects.get(id=id)
        user.delete()
        return Response({'msg': 'User Deleted!!'})"""

# @decorators(name='patch')
"""@method_decorator(csrf_exempt, name='dispatch')
class UserAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        pdb.set_trace()
        return JsonResponse(serializer.data, safe=False)
    
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
        return JsonResponse(res)"""



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

