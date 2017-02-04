from django.shortcuts import   render
from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    author=models.ForeignKey('auth.user')
    title=models.CharField(max_length=200)
    text=models.TextField()
    createdDate=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)



    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title