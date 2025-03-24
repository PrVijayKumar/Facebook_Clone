from django.urls import path, include
from user.api_views import views
urlpatterns = [
    path("user/", views.LCUserAPI.as_view(), name='lcu'),
    path("user/<int:pk>", views.PRUDUserAPI.as_view(), name='puser'),
]