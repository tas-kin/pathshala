from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .import forms 

@login_required
def discussion(request):
   posts=Post.objects.all().order_by('date')
   return render(request,"classroom/discussion.html",{'posts':posts})	


@login_required
def post_details(request,slug):
	post=Post.objects.get(slug=slug)  
	return render(request,"classroom/post_details.html",{'post':post})


@login_required
def post_create(request):
	if request.method=='POST':
	  form=forms.CreatePost(request.POST,request.FILES)
	  if form.is_valid():
	  	instance=form.save(commit=False)
	  	instance.author=request.user
	  	instance.save()
	  	return redirect('classroom:list')
	else:
	  form=forms.CreatePost()
	return render(request,"classroom/post_create.html",{'form':form})