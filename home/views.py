from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Comment, Session, Post_Like, Comment_Like
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
from django.urls import reverse
from django.http import JsonResponse
import random
from django.utils import timezone
import pytz
from django.utils.timesince import timesince

def home(request):
    try:

        template = loader.get_template('index.html')

        posts = Post.objects.all().values()
        comments = Comment.objects.all().values()

        for x in posts:
            x['date'] = check_date(x['date'])

        context = {
            'posts': posts,
            'comments': comments,
        }
        return HttpResponse(template.render(context, request))
    except Exception as error:
        # handle the exception
        print("An exception occurred:", error)
    

def get_session_id(request):
    try:
        session_id = request.COOKIES.get('session_id')

        
        if session_id is None:
            # Save the session ID to the database
            session = Session()
            session.save()

            # Get the generated session ID
            session_id = session.session_id

        # Set the cookie with the session ID
        response = JsonResponse({'session_id': session_id})
        response.set_cookie('session_id', session_id)

        print(session_id)
        print("Cookie done")

        return response

    except Exception as error:
        # handle the exception
        print("An exception occurred:", error)


@csrf_exempt
def add_post(request):

    phoenix_tz = pytz.timezone('America/Phoenix')
    timezone.activate(phoenix_tz)

    if request.method == 'POST':
        paragraph = request.POST.get('paragraph','')
        # current_date = datetime.now().astimezone(phoenix_tz)
        current_date = datetime.now().astimezone(phoenix_tz).strftime("%Y-%m-%d %H:%M:%S")

        post = Post(paragraph=paragraph,num_likes=0,num_dislikes=0,date=current_date,num_comments=0)
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

        comment = Comment(paragraph=paragraph, post_id=post_id,num_likes=0, num_dislikes=0,date=current_date)
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

#   GET
#   Get all the comments for a particular post
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
        post_id = request.POST.get('post_id','')
        session_id = request.POST.get('session_id','')

        post_like = Post_Like.objects.filter(id=post_id,session_id=session_id)

        print(post_like)

        # If the query set is empty, then like the post, else return False value
        # to show that the post was already liked
        if not post_like:
            post_like = Post_Like(post_id=post_id, session_id=session_id)
            post_like.save()

            #Update the post number of likes
            post = Post.objects.get(id=post_id)

            post.num_likes += 1
            post.save()

            return JsonResponse({'post_likes': post.num_likes})
        else:
            return HttpResponse("False")

@csrf_exempt
def dislike_post(request):

    pass

@csrf_exempt
def like_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id','')
        comment_id = request.POST.get('comment_id', '')
        session_id = request.POST.get('session_id','')

        comment_like = Comment_Like.objects.filter(post_id=post_id,comment_id=comment_id,session_id=session_id)

        print(comment_like)

        # If the query set is empty, then like the comment, else return False value
        # to show that the comment was already liked
        if not comment_like:

            comment_like = Comment_Like(post_id=post_id,comment_id=comment_id,session_id=session_id)
            comment_like.save()

            #Update the comment number of likes
            comment = Comment.objects.get(id=comment_id,post_id=post_id)

            comment.num_likes += 1
            comment.save()

            return JsonResponse({'comment_num_likes': comment.num_likes})
        else:
            return HttpResponse("False")

@csrf_exempt
def dislike_comment(request):
    pass

def check_date(date):
    try:
        print("Database date:")
        print(date)

        # Convert the UTC date to the local time zone
        local_date = timezone.localtime(date)

        print("Local date:")
        print(local_date)

        now = timezone.localtime(timezone.now())

        print("Now date using:")
        print(now)

        diff = now - local_date

        print("Diff: ", diff)

        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds // 60) % 60

        if days > 0:
            if days == 1:
                return f"{days} day ago"
            else:
                return f"{days} days ago"
        elif hours > 0:
            if hours == 1:
                return f"{hours} hour ago"
            else:
                return f"{hours} hours ago"
        elif minutes > 0:
            if minutes == 1:
                return f"{minutes} minute ago"
            else:
                return f"{minutes} minutes ago"
        else:
            return "recently"

    except Exception as e:
        print(f"An error occurred: {e}")
        return "recently"