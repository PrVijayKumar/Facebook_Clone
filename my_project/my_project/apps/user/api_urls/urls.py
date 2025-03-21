from django.urls import path, include
from user.api_views import views
urlpatterns = [
    # path('userinfo/<int:pk>', views.user_detail, name='ud'),
    # path('userinfo/', views.user_list, name='ul'),
    # path('userinfo/', views.user_api, name='ui'),
    path('userinfo/', views.UserAPI.as_view(), name='ui'),
    path('userinfo/<int:pk>/', views.UserAPI.as_view(), name='uip'),
    # path('createuser/', views.create_user, name='cu'),
]