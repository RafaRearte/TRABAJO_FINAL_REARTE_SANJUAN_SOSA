from datetime import date
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=500)
    text = models.TextField(max_length=4000)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    date = models.DateField(default=date.today)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return '%s - %s' % (self.post.title, self.author)