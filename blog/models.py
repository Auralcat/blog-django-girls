"""This is where you declare the models for the site"""

from django.db import models
from django.utils import timezone

class Post(models.Model):
    """Blog post"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Publishes a post"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
