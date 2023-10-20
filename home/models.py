from django.db import models
import random 

class User(models.Model):
  name = models.CharField(max_length=15)
  lastname = models.CharField(max_length=15)
  username = models.CharField(max_length=10)

class Post(models.Model):
    paragraph = models.CharField(max_length=250)
    num_likes = models.IntegerField()
    num_dislikes = models.IntegerField()
    date = models.TimeField()
    num_comments = models.IntegerField()

class Comment(models.Model):
    paragraph = models.CharField(max_length=250)
    post_id = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    date = models.TimeField()

class Post_Like(models.Model):
    post_id = models.IntegerField()
    session_id = models.CharField(max_length=32)


#                    GENERATE SESSION
def generate_session_id():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32))

class Session(models.Model):
    session_id = models.CharField(max_length=32, unique=True, default=generate_session_id)

