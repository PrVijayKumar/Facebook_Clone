from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('login/', views.login, name='login-page'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    # path('mypost/', views.mypost, name='mypost'),
    path('allposts/', views.all_posts, name='apost'),


]