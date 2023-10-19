from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
from django.urls import reverse
from django.http import JsonResponse

def home(request):
    try:
        template = loader.get_template('index.html')

        posts = Post.objects.all().values()
        comments = Comment.objects.all().values()

        context = {
            'posts': posts,
            'comments': comments,
        }
        return HttpResponse(template.render(context, request))
    except:
        print("An exception occurred")
    

@csrf_exempt
def add_post(request):

    if request.method == 'POST':
        paragraph = request.POST.get('paragraph','')
        current_date = datetime.now()

        post = Post(paragraph=paragraph,likes=0,dislikes=0,date=current_date,num_comments=0)
        post.save()


    return HttpResponse("Success")

#   POST
#   add a comment
@csrf_exempt
def add_comment(request):
    try:
        paragraph = request.POST.get('paragraph','')
        post_id = request.POST.get('post_id', '')

        current_date = datetime.now()

        comment = Comment(paragraph=paragraph, post_id=post_id,likes=0,dislikes=0,date=current_date)
        comment.save()

        #Increase comment count of post associated to the comment
        post = Post.objects.get(id=post_id)

        if post.num_comments == None:
            post.num_comments = 1
        else:
            post.num_comments += 1

        post.save()

        return HttpResponseRedirect('/home')

    except Exception as error:
        # handle the exception
        print("An exception occurred:", error)


def get_comments(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id','')
        comments = Comment.objects.filter(post_id=post_id).values()

        return JsonResponse({'comments': list(comments)})


def get_num_comments(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id','')
        post = Post.objects.get(id=post_id)

        return JsonResponse({'num_comments': post.num_comments})

@csrf_exempt
def like_post(request):
    if request.method == 'POST':
        post_id = request.Get.get('post_id','')
        post = Post.objects.get(id=post_id)

        post.likes += 1

        post.save()

        return JsonResponse({'post_likes': post.likes})

@csrf_exempt
def dislike_post(request):

    pass

@csrf_exempt
def like_comment(request):
    pass

@csrf_exempt
def dislike_comment(request):
    pass
