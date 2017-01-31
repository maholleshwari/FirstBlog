from django.shortcuts import render
from django.utils import timezone
from .models import post


def post_list(request):
    posts = post.objects.filter(publish_date=timezone.now()).order_by('publishr_date')
    return render(request,'blog/post_list.html',{'posts':posts})

