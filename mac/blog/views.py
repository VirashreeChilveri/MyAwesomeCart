from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.

# def index(request):
#     return HttpResponse("Index blog")

def index(request):
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html',{'myposts':myposts})
    # postID = Blogpost.objects.all()
    # all_posts = []
    #
    # for id in postID:
    #     all_posts.append(id)
    #
    # params = {'all_posts' : all_posts }
    # return render(request, 'blog/index.html', params)

def __str__(self):
    return self.title


def blogpost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog/blogpost.html',{'post':post})