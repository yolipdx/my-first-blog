""" import django databse and utils """
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """ model Post """
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ publish the blog """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
