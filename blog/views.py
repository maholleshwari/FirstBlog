from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import post
from .forms import PostForm


def post_list(request):
    posts = post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    postc=get_object_or_404(post, pk=pk)
    post.objects.get(pk=pk)
    return render(request,'blog/post_detail.html',{'postc':postc})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return  redirect('post_detail',pk=post.pk)
        else:
            form =PostForm()
            return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    postv= get_object_or_404(post , pk=pk)
    if request.method == "POST":
        form =PostForm(request.POST,instance=postv)
        if form.is_valid():
            postv=form.save(commit=False)
            postv.author = request.user
            postv.save()
            return  redirect('post_details',pk=postv.pk)
        else:
            form=PostForm(instance=postv)
            return render(request,'blog/post_edit.html',{'form':form})

def post_draft_list(request):
    posts = post.objects.filter(publish_date__isnull=True).order_by('createdDate')
    return render(request,'blog/post_draft_list.html',{'posts':posts})

def post_publish(request,pk):
    postn =get_object_or_404(post,pk=pk)
    postn.publish()
    return redirect('post_detail',pk=pk)

def publish(self):
    self.publish_date =timezone.now()
    self.save()

def post_remove(request,pk):
    postb =get_object_or_404(post,pk=pk)
    postb.delete()
    return  redirect('post_list')
