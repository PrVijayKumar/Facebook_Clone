from django.urls import path, include
from post.api_views import views
urlpatterns = [
    # path('post_info/<int:pk>', views.post_info, name='pi'),
    # path('post_list/', views.post_info, name='pl'),
    # path('postinfo/', views.post_api, name='pi'),
    # path('postinfo/', views.PostApi, name='pi'),
    # path('postinfo/<int:pk>/', views.PostApi, name='pip'),
    # path('postinfo/', views.PostAPI.as_view(), name='pi'),
    # path('postinfo/<int:pk>/', views.PostAPI.as_view(), name='pip'),
    path('postinfo/', views.PostList.as_view(), name='pl'),
    path('postinfo/<int:pk>', views.PostDestroy.as_view(), name='pp'),
    # path('postinfo/<int:pk>', views.PostUpdate.as_view(), name='pl'),
    # path('postinfo/<int:pk>', views.PostRetrieve.as_view(), name='pl'),
    # path('postcreate/', views.PostCreate.as_view(), name='pc'),
    path('createpost/', views.create_post, name='cp'),
]