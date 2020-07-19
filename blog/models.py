from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class User(models.Model):
    email = models.EmailField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Blog(TimeStamp):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title


