from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

router = DefaultRouter()

# router.register('userhapi/', UserViewSet, basename='users')
app_name = "user"

urlpatterns = [
    path('login/', views.login, name='login-page'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    # path('mypost/', views.mypost, name='mypost'),
    path('allposts/', views.all_posts, name='apost'),
    # path('userhapi/', include(router.urls)),

]