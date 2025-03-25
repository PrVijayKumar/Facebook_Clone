from django.urls import path, include
from post.api_views import views
urlpatterns = [
    # path('postinfo/', views.LCPostAPI.as_view(), name='pi'),
    # path('postinfo/<int:pk>/', views.PRUDPostAPI.as_view(), name='pu'),
    # path('postlist/', views.PostList.as_view(), name='pl'),
    # path('postcreate/', views.PostCreate.as_view(), name='pc'),
    # path('createpost/', views.create_post, name='cp'),
    # path('postinfo/<int:pk>/', views.PostDetail.as_view(), name='pi'),
    # path('postupdate/<int:pk>/', views.UpdatePost.as_view(), name='pu'),
    # path('deletepost/<int:pk>/', views.DeletePost.as_view(), name='dp'),
    # path('post/', views.CreateListPost.as_view(), name='lcp'),
    # path('post/<int:pk>/', views.RetrieveUpdatePost.as_view(), name='rup'),
    # path('rdpost/<int:pk>/', views.RetrieveDestroyPost.as_view(), name='rdpost'),
    path('post/', views.ListCreatePost.as_view(), name='lcp'),
    path('post/<int:pk>/', views.RetrieveUpdateDestroyPost.as_view(), name='rudp'),
]