from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt
from datetime import date

def home(request):
    template = loader.get_template('index.html')

    posts = Post.objects.all().values()
    comments = Comment.objects.all().values()

    context = {
        'posts': posts,
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

#   POST
#   add a comment
@csrf_exempt
def add_comment(request):
    paragraph = request.POST.get('paragraph','')
    post_id = request.POST.get('post_id', '')
    print(paragraph, post_id)

    day = date.today()

    comment = Comment(paragraph=paragraph, post_id=post_id,likes=0,dislikes=0)
    comment.save()

    return HttpResponse("Success")

@csrf_exempt
def add_post(request):
    paragraph = request.POST.get('paragraph','')
    print(paragraph)

    day = date.today()

    post = Post(paragraph=paragraph,likes=0,dislikes=0)
    post.save()

    return HttpResponse("Success")

@csrf_exempt
def like_post(request):
    pass

@csrf_exempt
def dislike_post(request):

    pass

@csrf_exempt
def like_comment(request):
    pass

@csrf_exempt
def dislike_comment(request):
    pass
