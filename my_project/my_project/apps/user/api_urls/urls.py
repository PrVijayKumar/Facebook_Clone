from django.urls import path, include
from user.api_views import views
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
    path('user/', views.ListCreateUser.as_view(), name='lcu'),
    path('user/<int:pk>/', views.RetrieveUpdateDestroyUser.as_view(), name='rdup'),
]