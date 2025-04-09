"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import serializers, viewsets, routers
from user.models import User

# Serializer define the API representation
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # Viewset define the behaviour of Views
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Router are used for automatic routing


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)



urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('post/', include('post.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('postapi/', include('post.api_urls.urls')),
    # path('userapi/', include('user.api_urls.urls')),
    path('api/', include('api_urls.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
