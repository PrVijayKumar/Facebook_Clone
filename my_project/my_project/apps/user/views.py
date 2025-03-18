from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm, AuthenticationForm #  , PostForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from post.models import PostModel, PostLikes

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('user:login-page')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = auth_login(request, user)
            messages.success(request, f"Welcome {username}")
            return redirect('/user/allposts/')
            # return render(request, '/user/allposts/', {'form': form})
        else:
            messages.info(request, 'Please sign in')
    form = AuthenticationForm()
    return render(request, "user/login.html", {'form': form, 'title': login})


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('user:login-page')

@login_required
def dashboard(request):
    # username = request.POST['username']
    # context = {}
    # return render(request, '/user/mypost.html', {'context': context})
    # return HttpResponse("Elocome")
    return render(request, 'user/allposts.html')

# def mypost(request):
#     context = {}
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             obj = PostModel.objects.create(
#                 post_title=title,
#                 post_content=content
#             )
#             obj.save()
#             print(obj)
#             messages.success(request, f'Post sent succesfully')
#             return HttpResponseRedirect("/user/dashboard")
#     else:
#         form = PostForm()
#     context['form'] = form
#     return render(request, 'user/post.html', context)

# def all_posts(request):
#     posts = PostModel.objects.all().order_by('-post_date')
#     context={}
#     context={
#         'posts': posts
#     }
#     return render(request, 'user/allposts.html', context)
def all_posts(request):
    context = {}
    ulikes = []
    posts = PostModel.objects.all().order_by('-post_date')
    # likes = PostLikes.objects.filter(liked_by=request.POST['user'])
    likes = PostLikes.objects.filter(liked_by=request.user.id)
    for like in likes:
        ulikes.append(like.post_id_id)
    # print(likes)
    print(ulikes)
    context['posts'] = posts
    context['likes'] = likes
    context = {
        'posts': posts,
        'likes': ulikes,
    }
    return render(request, 'user/allposts.html', context)
    # return HttpResponse("Hello from all posts")
