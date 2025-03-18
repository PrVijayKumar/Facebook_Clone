from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('createpost/', views.create_post, name='cpost'),
    path('myposts/', views.my_posts, name='mpost'),
    path('allposts/', views.all_posts, name="apost"),
    path('fposts/', views.friend_posts, name="fpost"),
    path('myposts/edit/<int:id>', views.edit_posts, name="epost"),
    path('myposts/dpost/<int:id>', views.del_post, name="dpost"),
    path('myposts/detpost/<int:id>', views.det_post, name="detpost"),
    path('lpost/<int:id>', views.like_post, name="lpost"),
    path('comments/<int:id>', views.comment_post, name="comment"),
    path('fcomments/<int:id>', views.fetch_comments, name="fcomments"),
    path('freplies/<int:id>', views.fetch_replies, name="fr"),
    path('cedit/<int:id>', views.edit_comment, name="ec"),
    path('cdelete/<int:id>', views.delete_comment, name="dc"),
]
