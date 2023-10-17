from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
from django.urls import reverse
from django.http import JsonResponse

def home(request):
    template = loader.get_template('index.html')

    posts = Post.objects.all().values()
    comments = Comment.objects.all().values()

    context = {
        'posts': posts,
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def add_post(request):

    if request.method == 'POST':
        paragraph = request.POST.get('paragraph','')
        current_date = datetime.now()

        post = Post(paragraph=paragraph,likes=0,dislikes=0,date=current_date)
        post.save()


    return HttpResponse("Success")

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

    return HttpResponseRedirect('/home')

# Add this view to fetch comments
def get_comments(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id','')
        comments = Comment.objects.filter(post_id=post_id).values()

        return JsonResponse({'comments': list(comments)})

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
