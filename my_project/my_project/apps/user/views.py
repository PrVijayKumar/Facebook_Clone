from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm, AuthenticationForm #  , PostForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from post.models import PostModel, PostLikes
from rest_framework import viewsets
# from .serializers import UserHyperlinkedSerializer
from .models import User
from email.mime.image import MIMEImage
import pathlib
from user.tasks import user_reg_email
# from django.template.loader import render_to_string
# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer = UserHyperlinkedSerializer



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            result = user_reg_email.delay(username, email)
            messages.success(request, f'Account created for {username}')
            return redirect('user:login-page')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def login(request):

    # send_mail(
    #     'Testing',
    #     'Hy Vijay Choudhary How are you',
    #     'vijaychoudhary@thoughtwin.com',
    #     ['vijay24082000@gmail.com'],
    #     fail_silently=False
    # )

    # text_content = "Hello Vijay Following is your Secret Key"

    # html_content = "<H1>Professor</H1><p>To Become a Professor you should have good <b>communication skills</b> and <i>command on your subject</i></p>"

    # msg = EmailMultiAlternatives(
    #     'Testing Multi Alternatives',
    #     text_content,
    #     'vijaychoudhary@thoughtwin.com',
    #     ['vijay24082000@gmail.com'],
    # )

    # msg.attach_alternative(html_content, 'text/html')
    # num = msg.send()
    # print("Number of mails", num)

    # message1 = (
    #     "First Message",
    #     "Hello mail for understanding send_mass_mail",
    #     "vijaychoudhary@thoughtwin.com",
    #     ["vijay24082000@gmail.com"]
    # )

    # message2 = (
    #     "Second Message",
    #     "Hello sending multple mails at once without opening connection again and again",
    #     "vijaychoudhary@gmail.com",
    #     ["gaurav@thoughtwin.com", "divyanshyadav@thoughtwin.com"]
    # )

    # num = send_mass_mail((message1, message2), fail_silently=False)

    # print(num)

    # email = EmailMessage(
    #     "Example Mail",
    #     "I am learning email through django",
    #     "vijaychoudhary@thoughtwin.com",
    #     ["vijay24082000@gmail.com"],
    #     reply_to=["vijaychoudhary@thoughtwin"],
    #     headers={"My-Header": "This is a header"}
    # )
    # breakpoint()
    # print(pathlib.Path(__file__).parent.parent.parent.resolve()/'media/images'/'crow_1JMfgUW.png')
    path = pathlib.Path(__file__).parent.parent.parent.resolve()/'media/images'/'449195169_1720433388491215_1556072659052802667_n_2axw1hM.png'
    # img_data = open(path, 'rb').read()
    # msgImg = MIMEImage(img_data, 'png')

    # email.attach(msgImg)
    # email.attach_file('../../../media/images/449195169_1720433388491215_1556072659052802667_n_2axw1hM.png')
    # num = email.send(fail_silently=False)
    # print(email.message())
    # print(email.recipients())
    # print(num)
    


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
