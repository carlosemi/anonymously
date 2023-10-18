from django.db import models

class User(models.Model):
  name = models.CharField(max_length=15)
  lastname = models.CharField(max_length=15)
  username = models.CharField(max_length=10)

class Post(models.Model):
    paragraph = models.CharField(max_length=250)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    date = models.TimeField()
    num_comments = models.IntegerField()


class Comment(models.Model):
    paragraph = models.CharField(max_length=250)
    post_id = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    date = models.TimeField()