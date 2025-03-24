from django.urls import path, include
from post.api_views import views
urlpatterns = [
    path('postinfo/', views.LCPostAPI.as_view(), name='pi'),
    path('postinfo/<int:pk>/', views.PRUDPostAPI.as_view(), name='pu'),
    path('createpost/', views.create_post, name='cp'),
]