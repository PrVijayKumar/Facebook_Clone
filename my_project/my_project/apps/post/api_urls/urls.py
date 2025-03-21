from django.urls import path, include
from post.api_views import views
urlpatterns = [
    # path('post_info/<int:pk>', views.post_info, name='pi'),
    # path('post_list/', views.post_info, name='pl'),
    # path('postinfo/', views.post_api, name='pi'),
    path('postinfo/', views.PostApi, name='pi'),
    path('postinfo/<int:pk>/', views.PostApi, name='pip'),
    path('createpost/', views.create_post, name='cp'),
]