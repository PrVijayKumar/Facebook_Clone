from django.urls import path, include
from user.api_views import views
urlpatterns = [
    # path('userinfo/<int:pk>', views.user_detail, name='ud'),
    # path('userinfo/', views.user_list, name='ul'),
    # path('userinfo/', views.user_api, name='ui'),
    path('userlist/', views.UserList.as_view(), name='ul'),
    path('createuser/', views.CreateUser.as_view(), name='cu'),
    path('userinfo/<int:pk>', views.UserInfo.as_view(), name='ui'),
    path('updateuser/<int:pk>', views.UpdateUser.as_view(), name='ui'),
    path('patchuser/<int:pk>', views.PatchUser.as_view(), name='pu'),
    path('deluser/<int:pk>', views.DeleteUser.as_view(), name='du'),
    # path('userinfo/<int:pk>/', views.UserAPI.as_view(), name='uip'),
    # path('createuser/', views.create_user, name='cu'),
]