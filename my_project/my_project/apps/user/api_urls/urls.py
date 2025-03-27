from django.urls import path, include
from user.api_views import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from user.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
router = DefaultRouter()

# router.register('userapi', views.UserViewSet, basename='user')
router.register('userapi', views.UserModelViewSet, basename='user')
# router.register('userapi', views.UserReadOnlyModelViewSet, basename='user')
urlpatterns = [
    # path("user/", views.LCUserAPI.as_view(), name='lcu'),
    # path("user/<int:pk>", views.PRUDUserAPI.as_view(), name='puser'),
    # path("user/", views.UserList.as_view(), name="ul"),
    # path("createuser/", views.CreateUser.as_view(), name="cu"),
    # path("userdetail/<int:pk>/", views.UserDetail.as_view(), name="ud"),
    # path("updateuser/<int:pk>/", views.UpdateUser.as_view(), name="uu"),
    # path("deleteuser/<int:pk>/", views.DeleteUser.as_view(), name="du"),
    # path('user/', views.ListCreateUser.as_view(), name='lcu'),
    # path('user/<int:pk>/', views.RetrieveUpdateUser.as_view(), name='ru'),
    # path('rduser/<int:pk>/', views.RetrieveDestroyUser.as_view(), name='rdu'),
    # path('user/', views.ListCreateUser.as_view(), name='lcu'),
    # path('user/<int:pk>/', views.RetrieveUpdateDestroyUser.as_view(), name='rdup'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="rest_framework2")),
    # path('gettoken/', obtain_auth_token),
    # path('gettoken/', CustomAuthToken.as_view()),
    path('gettoken/', TokenObtainPairView.as_view(), name="token_obtain"),
    path('refreshtoken/', TokenRefreshView.as_view(), name="token_refresh"),
    path('verifytoken/', TokenVerifyView.as_view(), name='refresh_token'),
]
# print(path('gettoken/', obtain_auth_token))