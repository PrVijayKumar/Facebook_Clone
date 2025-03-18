from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import PostForm, PostUpdateForm, CommentForm, ReplyForm
from .models import PostModel, User, PostLikes, timezone, PostComments  # , NotEqual, Field
import json
import datetime
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
# from django.core import serializers
# from django.core.serializers.get_serializer

# def remove_circular_refs(ob, _seen=None):
#     if _seen is None:
#         _seen = set()
#     if id(ob) in _seen:
#         # circular reference, remove it.
#         return None
#     _seen.add(id(ob))
#     res = ob
#     if isinstance(ob, dict):
#         res = {
#             remove_circular_refs(k, _seen): remove_circular_refs(v, _seen)
#             for k, v in ob.items()}
#     elif isinstance(ob, (list, tuple, set, frozenset)):
#         res = type(ob)(remove_circular_refs(v, _seen) for v in ob)
#     # remove id again; only *nested* references count
#     _seen.remove(id(ob))
#     return res

# class MyEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, datetime.datetime):
#             if isinstance(o, datetime.datetime):
#                 return dict(year=o.year, month=o.month, day=o.day)
#             else:
#                 json.JSONEncoder.default(self, o)
#         elif isinstance(o, int):
#             return json.dumps(o)
#         elif isinstance(o, User):
#             return str(o)
#         else:
#             return o.__dict__


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if (isinstance(obj, datetime.datetime) or isinstance(obj, int) or isinstance(obj, User)):
            return str(obj)
        return super().default(obj)





# Create your views here.




def create_post(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            content = form.cleaned_data.get('content')

            obj = PostModel(
                    post_title=title,
                    post_description=description,
                    post_content=content,
                    post_user=request.user
                )
            print(request.user)
            obj.save()
            messages.success(request, 'Post sent successfully.')
            print("data submit")
            return HttpResponseRedirect('/user/dashboard')
    else:
        form = PostForm()
    context['form'] = form
    return render(request, "post/createpost.html", context)
    # return HttpResponse("Create post page")


def my_posts(request):
    context = {}
    c_user = request.user
    print(c_user)
    posts = PostModel.objects.filter(post_user=c_user.id).order_by('-post_date')
    likes = PostLikes.objects.filter(liked_by_id=request.user.id)
    ulikes = []
    for like in likes:
        ulikes.append(like.post_id_id)

    print(ulikes)

    context['posts'] = posts
    context['likes'] = ulikes
    return render(request, 'post/myposts.html', context)


def all_posts(request):
    context = {}
    posts = PostModel.objects.all().order_by('-post_date')
    likes = PostLikes.objects.all()
    context['posts'] = posts
    context['likes'] = likes
    return render(request, 'post/allposts.html', context)

def friend_posts(request):
    context = {}
    c_user = request.user
    posts = PostModel.objects.all().exclude(post_user=c_user.id).order_by('-post_date')
    context['posts'] = posts
    return render(request, 'post/friends_post.html', context)


# def edit_posts(request, id):
#     obj = PostModel.objects.get(pk=id)
#     context = {}
#     if request.method == 'POST':
#         form = PostUpdateForm(request.POST, request.FILES, initial={'post_content': obj.post_content, 'post_description': obj.post_description, 'post_title': obj.post_title})
#         if form.is_valid():
#             obj.post_title = form.cleaned_data.get('post_title')
#             obj.post_description = form.cleaned_data.get('post_description')
#             obj.post_content = form.cleaned_data.get('post_content')
#             obj.save()
#             messages.success(request, "Post Updated Successfully.")
#             return HttpResponseRedirect('/user/dashboard/')
#     else:
#         form = PostUpdateForm(instance=obj)
#         print(obj.post_content, obj.post_title, obj.post_description)
#     context = {
#         'form': form
#     }
#     return render(request, 'post/editpost.html', context)

# def edit_posts(request, id):
#     obj = PostModel.objects.get(pk=id)
#     context = {}
#     print(request.POST)
#     if request.method == 'POST':
#         form = PostUpdateForm(request.POST, request.FILES, initial={'post_content': obj.post_content, 'post_description': obj.post_description, 'post_title': obj.post_title})
#         if form.is_valid():
#             obj.post_title = form.cleaned_data.get('post_title')
#             obj.post_description = form.cleaned_data.get('post_description')
#             # print(request.POST['post_content'])
#             obj.post_content = form.cleaned_data.get('post_content')
#             obj.post_updated_date = timezone.now()
#             # print(obj.post_content)
#             obj.save()
#             messages.success(request, "Post Updated Successfully.")
#             # return HttpResponseRedirect('/post/myposts/')
#             # return HttpResponseRedirect(request.META['HTTP_REFERER'])
#             return JsonResponse("Hello from edit posts.")
#     else:
#         form = PostUpdateForm(instance=obj)
#         print(obj.post_content, obj.post_title, obj.post_description)
#     context = {
#         'form': form
#     }
#     # return render(request, 'post/editpost.html', context)
#     # return redirect(request.META['HTTP_REFERER'])
#     return JsonResponse("worked")



def del_post(request, id):
    print("hello")
    obj = PostModel.objects.get(pk=id)
    obj.delete()
    messages.success(request, "Post Deleted.")
    result = json.dumps({'result': 'Deleted', 'id': str(id)})
    return JsonResponse({'result': result})
    # return HttpResponseRedirect(reverse('post:mpost'))
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])


def det_post(request, id):
    obj = PostModel.objects.get(pk=id)
    context = {
        'post': obj
    }
    return render(request, 'post/detpost.html', context)


def like_post(request, id):
    fuser = User.objects.get(pk=request.POST['uid'])
    obj = PostModel.objects.get(pk=id)
    likes = PostLikes()
    print("working")
    # likes = PostLikes.object.get()
    if int(request.POST['flag']) == 1:
        obj.post_likes += 1
        likes.liked_by = fuser
        print(likes.liked_by)
        likes.post_id = obj
        likes.save()
    else:
        obj.post_likes -= 1
        likes = PostLikes.objects.filter(post_id=id).filter(liked_by=fuser)
        print(likes)
        likes.delete()
        # likes.save()
    obj.save()
    
    print(obj.post_likes)
    return HttpResponse(obj.post_likes)
    # return HttpResponse("post worked")


def edit_posts(request, id):
    obj = PostModel.objects.get(pk=id)
    context = {}
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, initial={'post_content': obj.post_content, 'post_description': obj.post_description, 'post_title': obj.post_title})
        # print(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            obj.post_title = form.cleaned_data.get('post_title')
            obj.post_description = form.cleaned_data.get('post_description')
            # print(request.POST['post_content'])
            obj.post_content = form.cleaned_data.get('post_content')
            obj.post_updated_date = timezone.now()
            # print(obj.post_content)
            obj.save()
            # messages.success(request, "Post Updated Successfully.")
            # return HttpResponseRedirect('/post/myposts/')
            # return HttpResponseRedirect(request.META['HTTP_REFERER'])
            # print(MyEncoder().encode(obj))
            # print(isinstance(obj.post_likes, int))
            # x = json.dumps(obj.post_likes)
            # print(type(x))
            # print(obj.post_content)
            # json.dumps(cls=MyEncoder)
            # x=0
            # y=json.dumps(x)
            # print(type(y), type(x))

            # data = serializers.serialize("json", obj)
            # # XMLSerializer = serializers.get_serializer("xml")
            # # xml_serializer = XMLSerializer()
            # # xml_serializer.serialize(obj)
            # # data = xml_serializer.getvalue()
            # print(data)

            result = serialize("json", [obj], cls=LazyEncoder)
            # x = serializers.serialize("json", [obj], indent=2,
            #                       use_natural_foreign_keys=True,
            #                       use_natural_primary_keys=True,)

            # print(x)
            return JsonResponse({"result": result})
    else:
        form = PostUpdateForm(instance=obj)
        print(obj.post_content, obj.post_title, obj.post_description)
    context = {
        'form': form
    }
    # return render(request, 'post/editpost.html', context)
    # return redirect(request.META['HTTP_REFERER'])
    return JsonResponse({"result": "worked"})


def comment_post(request, id):
    result = None
    reply = None
    try:
        reply = request.POST['com_reply']
    except:
        reply = None
    post = PostModel.objects.get(pk=id)
    if request.method == 'POST':
        if reply is not None:
            print(request.user, request.POST['com_reply'])
            com_reply = User.objects.get(username=request.POST['com_reply'])
            print(com_reply)
            form = ReplyForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                obj = PostComments(
                    comment_desc=form.cleaned_data.get('comment_desc'),
                    com_user=request.user,
                    post=post,
                    reply_on_comment=form.cleaned_data.get('reply_on_comment'),
                    com_reply=com_reply,
                )
                obj.save()
                result = serialize('json', [obj], cls=LazyEncoder)
            print(form)
        else:
            form = CommentForm(request.POST, initial={'com_user': request.user})
            if form.is_valid():
                obj = PostComments(
                    comment_desc=form.cleaned_data.get('comment_desc'),
                    com_user=request.user,
                    post=post,
                )
                obj.save()
                print("Object Id", obj.id)
                result = serialize('json', [obj], cls=LazyEncoder)
            else:
                print("error")
                obj = PostComments()
                result = 'error'
    else:
        result = "error"
    return JsonResponse({'result': result})


def fetch_comments(request, id):
    comments = PostComments.objects.filter(post_id=id).filter(com_reply=None).order_by("-com_date")
    users = User.objects.all().values_list('id', 'username')
    print(list(users))
    rlist = []
    for comment in comments:
        rlist.append(comment.id)
    mylist = []
    for a in rlist:
        checklist = PostComments.objects.filter(reply_on_comment=a)
        if not checklist:
            pass
        else:
            mylist.append(a)
    print(mylist)
    rlist = json.dumps(mylist)
    # print(comments)
    # result= 'error'
    # result = serialize('json', [comments], cls=LazyEncoder)  this line will not work because comments 
    # is a set of objects so no need to pass it as dictionary
    result = serialize('json', comments, cls=LazyEncoder)
    # users = serialize('json', users, cls=LazyEncoder)
    try:
        # users = serialize('json', list(users), cls=LazyEncoder)
        users = json.dumps(list(users))
    except:
        print("Error")
    print(users)
    return JsonResponse({'result': result, 'users': users, 'rlist': rlist})

def fetch_replies(request, id):
    result = None
    replies = PostComments.objects.filter(reply_on_comment=id).order_by('-com_date')
    rstatus = replies.values_list('id')
    rlist = []
    for r in rstatus:
        rlist.append(r[0])
    print(rlist)
    mylist = []
    for a in rlist:
        comments = PostComments.objects.filter(reply_on_comment=a)
        print(comments)
        if not comments:
            pass
        else:
            mylist.append(a)
    print(mylist)
    rlist = json.dumps(mylist)
    users = User.objects.values('id', 'username')
    result = serialize('json', replies, cls=LazyEncoder)
    # users = serialize('json', list(users), cls=LazyEncoder)
    users = json.dumps(list(users))
    # print(result)
    return JsonResponse({'result': result, 'users': users, 'rlist': rlist})


def edit_comment(request, id):
    result = None
    com = PostComments.objects.get(id=id)
    print(com)
    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'comment_desc': com.comment_desc})
        if form.is_valid():
            com.comment_desc = form.cleaned_data.get('comment_desc')
            com.save()
            result = serialize('json', [com], cls=LazyEncoder)
    else:
        result = "Error"
    return JsonResponse({'result': result})


def delete_comment(request, id):
    comments = PostComments.objects.filter(reply_on_comment=id)
    comments.delete()
    comment = PostComments.objects.get(id=id)
    comment.delete()
    result = json.dumps({'result': 'Deleted', 'id': str(id)})
    return JsonResponse({'result': result})
